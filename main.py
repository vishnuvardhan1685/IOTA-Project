from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
import numpy as np
from typing import Dict, List
import pandas as pd
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(
    title="Water Pump Prediction API",
    description="ML-powered API to predict water pump status based on environmental sensors",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model and scaler
try:
    model = joblib.load('pump_prediction_model.pkl')
    scaler = joblib.load('scaler.pkl')
    print("✅ Model and scaler loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None
    scaler = None

# Pydantic models for request/response
class SensorInput(BaseModel):
    soil_moisture: float = Field(..., description="Soil moisture reading", ge=0, le=1000)
    temperature: float = Field(..., description="Air temperature in Celsius", ge=-10, le=50)
    air_humidity: float = Field(..., description="Air humidity percentage", ge=0, le=100)
    
    class Config:
        json_schema_extra = {
            "example": {
                "soil_moisture": 450.5,
                "temperature": 28.5,
                "air_humidity": 65.2
            }
        }

class PredictionResponse(BaseModel):
    prediction: int = Field(..., description="0 = Pump OFF, 1 = Pump ON")

class BatchSensorInput(BaseModel):
    sensors: List[SensorInput] = Field(..., description="List of sensor readings")

class ModelInfo(BaseModel):
    model_type: str
    accuracy: float
    features: List[str]
    target: str
    version: str

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Water Pump Prediction API",
        "version": "1.0.0",
        "status": "online",
        "model_loaded": model is not None,
        "endpoints": {
            "predict": "/predict",
            "predict_batch": "/predict/batch",
            "model_info": "/model/info",
            "health": "/health",
            "docs": "/docs"
        }
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    """Check if the API and model are healthy"""
    if model is None or scaler is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    return {
        "status": "healthy",
        "model_loaded": True,
        "timestamp": datetime.now().isoformat()
    }

# Model info endpoint
@app.get("/model/info", response_model=ModelInfo)
async def get_model_info():
    """Get information about the trained model"""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    return ModelInfo(
        model_type="Logistic Regression",
        accuracy=99.83,
        features=["Soil Moisture", "Temperature", "Air Humidity"],
        target="Pump Data (0=OFF, 1=ON)",
        version="1.0.0"
    )

# Single prediction endpoint
@app.post("/predict", response_model=PredictionResponse)
async def predict_pump_status(sensor_data: SensorInput):
    """
    Predict whether the water pump should be ON or OFF based on sensor readings.
    
    - **soil_moisture**: Soil moisture reading (0-1000)
    - **temperature**: Air temperature in Celsius (-10 to 50)
    - **air_humidity**: Air humidity percentage (0-100)
    
    Returns prediction with confidence levels.
    """
    if model is None or scaler is None:
        raise HTTPException(status_code=503, detail="Model not loaded. Please ensure model files exist.")
    
    try:
        # Prepare input data
        input_data = np.array([[
            sensor_data.soil_moisture,
            sensor_data.temperature,
            sensor_data.air_humidity
        ]])
        
        # Scale the input
        input_scaled = scaler.transform(input_data)
        
        # Make prediction
        prediction = int(model.predict(input_scaled)[0])
        
        # Return only 0 or 1
        return PredictionResponse(
            prediction=prediction
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

# Batch prediction endpoint
@app.post("/predict/batch")
async def predict_batch(batch_data: BatchSensorInput):
    """
    Predict pump status for multiple sensor readings at once.
    
    Accepts a list of sensor readings and returns predictions for each.
    """
    if model is None or scaler is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        predictions = []
        
        for sensor_data in batch_data.sensors:
            # Prepare input data
            input_data = np.array([[
                sensor_data.soil_moisture,
                sensor_data.temperature,
                sensor_data.air_humidity
            ]])
            
            # Scale and predict
            input_scaled = scaler.transform(input_data)
            prediction = int(model.predict(input_scaled)[0])
            
            predictions.append(prediction)
        
        return {
            "predictions": predictions
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Batch prediction error: {str(e)}")

# Model statistics endpoint
@app.get("/model/statistics")
async def get_model_statistics():
    """Get detailed model statistics and feature importance"""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    feature_names = ['Soil Moisture', 'Temperature', 'Air Humidity']
    coefficients = model.coef_[0].tolist()
    
    feature_importance = [
        {
            "feature": name,
            "coefficient": round(coef, 4),
            "importance": "Strong" if abs(coef) > 5 else "Moderate" if abs(coef) > 0.5 else "Weak"
        }
        for name, coef in zip(feature_names, coefficients)
    ]
    
    return {
        "model_type": "Logistic Regression",
        "accuracy": 99.83,
        "training_samples": 2400,
        "test_samples": 600,
        "feature_importance": feature_importance,
        "intercept": round(float(model.intercept_[0]), 4)
    }

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting Water Pump Prediction API...")
    print("📚 API Documentation: http://localhost:8000/docs")
    print("🔍 Alternative docs: http://localhost:8000/redoc")
    uvicorn.run(app, host="0.0.0.0", port=8000)
