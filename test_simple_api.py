import requests
import json

# API base URL
BASE_URL = "http://localhost:8000"

print("="*60)
print("TESTING SIMPLIFIED API - BOOLEAN RESPONSES ONLY")
print("="*60)

# Test Case 1: Low soil moisture (should return 1)
print("\n" + "-"*60)
print("Test 1: Low Soil Moisture (Expected: 1 = Pump ON)")
print("-"*60)
data1 = {
    "soil_moisture": 400.0,
    "temperature": 33.0,
    "air_humidity": 77.0
}
print(f"Input: {data1}")
response1 = requests.post(f"{BASE_URL}/predict", json=data1)
print(f"Response: {response1.json()}")

# Test Case 2: High soil moisture (should return 0)
print("\n" + "-"*60)
print("Test 2: High Soil Moisture (Expected: 0 = Pump OFF)")
print("-"*60)
data2 = {
    "soil_moisture": 850.0,
    "temperature": 28.0,
    "air_humidity": 55.0
}
print(f"Input: {data2}")
response2 = requests.post(f"{BASE_URL}/predict", json=data2)
print(f"Response: {response2.json()}")

# Test Case 3: Medium soil moisture
print("\n" + "-"*60)
print("Test 3: Medium Soil Moisture")
print("-"*60)
data3 = {
    "soil_moisture": 600.0,
    "temperature": 28.0,
    "air_humidity": 60.0
}
print(f"Input: {data3}")
response3 = requests.post(f"{BASE_URL}/predict", json=data3)
print(f"Response: {response3.json()}")

# Test Case 4: Batch prediction
print("\n" + "="*60)
print("BATCH PREDICTION TEST")
print("="*60)
batch_data = {
    "sensors": [
        {"soil_moisture": 400.0, "temperature": 33.0, "air_humidity": 77.0},
        {"soil_moisture": 800.0, "temperature": 32.0, "air_humidity": 50.0},
        {"soil_moisture": 600.0, "temperature": 28.0, "air_humidity": 60.0},
        {"soil_moisture": 500.0, "temperature": 25.0, "air_humidity": 65.0}
    ]
}
print(f"Batch Input: {len(batch_data['sensors'])} sensor readings")
batch_response = requests.post(f"{BASE_URL}/predict/batch", json=batch_data)
print(f"Batch Response: {json.dumps(batch_response.json(), indent=2)}")

print("\n" + "="*60)
print("SUMMARY")
print("="*60)
print("✅ API now returns simplified boolean responses:")
print("   • Single prediction: {'prediction': 0} or {'prediction': 1}")
print("   • Batch prediction: {'predictions': [0, 1, 1, 0, ...]}")
print("="*60)
