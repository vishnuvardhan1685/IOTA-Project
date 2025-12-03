import joblib
import numpy as np

# Load the trained model and scaler
model = joblib.load('pump_prediction_model.pkl')
scaler = joblib.load('scaler.pkl')

def predict_pump_status(soil_moisture, temperature, air_humidity):
    """
    Predict whether the water pump should be ON or OFF based on input parameters.
    
    Parameters:
    - soil_moisture: Soil moisture reading
    - temperature: Air temperature in Celsius
    - air_humidity: Air humidity percentage
    
    Returns:
    - prediction: 0 (Pump OFF) or 1 (Pump ON)
    - probability: Confidence level of the prediction
    """
    # Prepare input data
    input_data = np.array([[soil_moisture, temperature, air_humidity]])
    
    # Scale the input
    input_scaled = scaler.transform(input_data)
    
    # Make prediction
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0]
    
    return prediction, probability

# Test with sample data from the dataset
print("="*60)
print("TESTING THE MODEL WITH SAMPLE PREDICTIONS")
print("="*60)

test_cases = [
    {"soil_moisture": 400, "temperature": 33, "air_humidity": 77, "description": "Low soil moisture, high temp & humidity"},
    {"soil_moisture": 800, "temperature": 32, "air_humidity": 50, "description": "High soil moisture, moderate temp & humidity"},
    {"soil_moisture": 500, "temperature": 25, "air_humidity": 60, "description": "Medium soil moisture, low temp"},
    {"soil_moisture": 900, "temperature": 35, "air_humidity": 60, "description": "Very high soil moisture"},
]

for i, test in enumerate(test_cases, 1):
    print(f"\n{'-'*60}")
    print(f"Test Case {i}: {test['description']}")
    print(f"{'-'*60}")
    
    soil_moisture = test['soil_moisture']
    temperature = test['temperature']
    air_humidity = test['air_humidity']
    
    prediction, probability = predict_pump_status(soil_moisture, temperature, air_humidity)
    
    print(f"\nInput Values:")
    print(f"  - Soil Moisture: {soil_moisture}")
    print(f"  - Temperature: {temperature}°C")
    print(f"  - Air Humidity: {air_humidity}%")
    
    print(f"\n{'='*60}")
    if prediction == 1:
        print(f"PREDICTION: Pump should be ON 🟢")
        print(f"Confidence: {probability[1]*100:.2f}%")
    else:
        print(f"PREDICTION: Pump should be OFF 🔴")
        print(f"Confidence: {probability[0]*100:.2f}%")
    print(f"{'='*60}")
    
    print(f"\nProbability Distribution:")
    print(f"  - Pump OFF (0): {probability[0]*100:.2f}%")
    print(f"  - Pump ON (1): {probability[1]*100:.2f}%")

print(f"\n{'='*60}")
print("Testing complete! Run 'predict.py' for interactive predictions.")
print(f"{'='*60}")
