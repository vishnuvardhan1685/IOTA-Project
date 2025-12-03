# Water Pump Prediction API

A FastAPI-based REST API for predicting water pump status using machine learning (Logistic Regression).

## 🚀 Quick Start

### 1. Start the API Server

```bash
python main.py
```

The API will start at `http://localhost:8000`

### 2. View API Documentation

Once the server is running, visit:
- **Interactive Docs**: http://localhost:8000/docs (Swagger UI)
- **Alternative Docs**: http://localhost:8000/redoc (ReDoc)

### 3. Test the API

In a new terminal, run:
```bash
python test_api.py
```

## 📡 API Endpoints

### Root Endpoint
```http
GET /
```
Get API information and available endpoints.

**Example Response:**
```json
{
  "message": "Water Pump Prediction API",
  "version": "1.0.0",
  "status": "online",
  "model_loaded": true,
  "endpoints": { ... }
}
```

---

### Health Check
```http
GET /health
```
Check if the API and model are healthy.

**Example Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "timestamp": "2025-12-04T10:30:00"
}
```

---

### Model Information
```http
GET /model/info
```
Get information about the trained model.

**Example Response:**
```json
{
  "model_type": "Logistic Regression",
  "accuracy": 99.83,
  "features": ["Soil Moisture", "Temperature", "Air Humidity"],
  "target": "Pump Data (0=OFF, 1=ON)",
  "version": "1.0.0"
}
```

---

### Single Prediction
```http
POST /predict
```
Predict pump status for a single sensor reading.

**Request Body:**
```json
{
  "soil_moisture": 400.0,
  "temperature": 33.0,
  "air_humidity": 77.0
}
```

**Example Response:**
```json
{
  "prediction": 1,
  "prediction_label": "Pump ON 🟢",
  "confidence": 100.0,
  "probability_off": 0.0,
  "probability_on": 100.0,
  "input_values": {
    "soil_moisture": 400.0,
    "temperature": 33.0,
    "air_humidity": 77.0
  },
  "timestamp": "2025-12-04T10:30:00"
}
```

---

### Batch Prediction
```http
POST /predict/batch
```
Predict pump status for multiple sensor readings at once.

**Request Body:**
```json
{
  "sensors": [
    {
      "soil_moisture": 400.0,
      "temperature": 33.0,
      "air_humidity": 77.0
    },
    {
      "soil_moisture": 800.0,
      "temperature": 32.0,
      "air_humidity": 50.0
    }
  ]
}
```

**Example Response:**
```json
{
  "total_predictions": 2,
  "predictions": [
    {
      "input": { "soil_moisture": 400.0, "temperature": 33.0, "air_humidity": 77.0 },
      "prediction": 1,
      "prediction_label": "Pump ON 🟢",
      "confidence": 100.0,
      "probability_off": 0.0,
      "probability_on": 100.0
    },
    {
      "input": { "soil_moisture": 800.0, "temperature": 32.0, "air_humidity": 50.0 },
      "prediction": 0,
      "prediction_label": "Pump OFF 🔴",
      "confidence": 99.81,
      "probability_off": 99.81,
      "probability_on": 0.19
    }
  ],
  "timestamp": "2025-12-04T10:30:00"
}
```

---

### Model Statistics
```http
GET /model/statistics
```
Get detailed model statistics and feature importance.

**Example Response:**
```json
{
  "model_type": "Logistic Regression",
  "accuracy": 99.83,
  "training_samples": 2400,
  "test_samples": 600,
  "feature_importance": [
    {
      "feature": "Soil Moisture",
      "coefficient": -9.9097,
      "importance": "Strong"
    },
    {
      "feature": "Temperature",
      "coefficient": 0.0036,
      "importance": "Weak"
    },
    {
      "feature": "Air Humidity",
      "coefficient": -0.0144,
      "importance": "Weak"
    }
  ],
  "intercept": 0.1234
}
```

---

## 💻 Usage Examples

### Using cURL

**Single Prediction:**
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "soil_moisture": 450.5,
    "temperature": 28.5,
    "air_humidity": 65.2
  }'
```

**Batch Prediction:**
```bash
curl -X POST "http://localhost:8000/predict/batch" \
  -H "Content-Type: application/json" \
  -d '{
    "sensors": [
      {"soil_moisture": 400, "temperature": 33, "air_humidity": 77},
      {"soil_moisture": 800, "temperature": 32, "air_humidity": 50}
    ]
  }'
```

### Using Python

```python
import requests

# Single prediction
response = requests.post(
    "http://localhost:8000/predict",
    json={
        "soil_moisture": 450.5,
        "temperature": 28.5,
        "air_humidity": 65.2
    }
)
print(response.json())
```

### Using JavaScript/Fetch

```javascript
// Single prediction
fetch('http://localhost:8000/predict', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    soil_moisture: 450.5,
    temperature: 28.5,
    air_humidity: 65.2
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

---

## 📦 Dependencies

```
fastapi
uvicorn
pydantic
joblib
numpy
scikit-learn
pandas
requests (for testing)
```

Install all dependencies:
```bash
pip install fastapi uvicorn pydantic joblib numpy scikit-learn pandas requests
```

---

## 🔧 Configuration

### Change Port

Edit `main.py` and modify the last line:
```python
uvicorn.run(app, host="0.0.0.0", port=8000)  # Change 8000 to your desired port
```

### CORS Settings

The API allows all origins by default. To restrict origins, edit `main.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Add your allowed origins
    ...
)
```

---

## 🎯 Model Details

- **Algorithm**: Logistic Regression
- **Accuracy**: 99.83%
- **Primary Feature**: Soil Moisture (coefficient: -9.91)
- **Decision Logic**: 
  - Low soil moisture → Pump ON
  - High soil moisture → Pump OFF

---

## 📝 Input Validation

The API validates input parameters:
- **soil_moisture**: 0 to 1000
- **temperature**: -10°C to 50°C
- **air_humidity**: 0% to 100%

Invalid inputs will return a 422 error with details.

---

## 🚀 Deployment

### Using Uvicorn directly:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Production deployment:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

---

## 📊 Response Format

All predictions include:
- **prediction**: Binary value (0 or 1)
- **prediction_label**: Human-readable label
- **confidence**: Confidence level (0-100%)
- **probability_off**: Probability of Pump OFF
- **probability_on**: Probability of Pump ON
- **input_values**: Echo of input data
- **timestamp**: ISO format timestamp

---

## 🛠️ Troubleshooting

### Model not loading?
Make sure these files exist in the same directory as `main.py`:
- `pump_prediction_model.pkl`
- `scaler.pkl`

Run `python model_training.py` to regenerate them.

### Port already in use?
Change the port in `main.py` or kill the process using the port:
```bash
lsof -ti:8000 | xargs kill -9
```

---

## 📚 Additional Resources

- **FastAPI Documentation**: https://fastapi.tiangolo.com/
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

**Created**: December 2025  
**API Version**: 1.0.0  
**Model Accuracy**: 99.83%
