import requests
import json

# API base URL
BASE_URL = "http://localhost:8000"

def test_root():
    """Test the root endpoint"""
    print("\n" + "="*60)
    print("Testing Root Endpoint")
    print("="*60)
    response = requests.get(f"{BASE_URL}/")
    print(f"Status Code: {response.status_code}")
    print(json.dumps(response.json(), indent=2))

def test_health():
    """Test the health check endpoint"""
    print("\n" + "="*60)
    print("Testing Health Check Endpoint")
    print("="*60)
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(json.dumps(response.json(), indent=2))

def test_model_info():
    """Test the model info endpoint"""
    print("\n" + "="*60)
    print("Testing Model Info Endpoint")
    print("="*60)
    response = requests.get(f"{BASE_URL}/model/info")
    print(f"Status Code: {response.status_code}")
    print(json.dumps(response.json(), indent=2))

def test_single_prediction():
    """Test single prediction endpoint"""
    print("\n" + "="*60)
    print("Testing Single Prediction - Low Soil Moisture")
    print("="*60)
    
    # Test case 1: Low soil moisture (should predict Pump ON)
    data = {
        "soil_moisture": 400.0,
        "temperature": 33.0,
        "air_humidity": 77.0
    }
    
    response = requests.post(f"{BASE_URL}/predict", json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Input: {data}")
    print("\nResponse:")
    print(json.dumps(response.json(), indent=2))
    
    print("\n" + "="*60)
    print("Testing Single Prediction - High Soil Moisture")
    print("="*60)
    
    # Test case 2: High soil moisture (should predict Pump OFF)
    data = {
        "soil_moisture": 850.0,
        "temperature": 28.0,
        "air_humidity": 55.0
    }
    
    response = requests.post(f"{BASE_URL}/predict", json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Input: {data}")
    print("\nResponse:")
    print(json.dumps(response.json(), indent=2))

def test_batch_prediction():
    """Test batch prediction endpoint"""
    print("\n" + "="*60)
    print("Testing Batch Prediction")
    print("="*60)
    
    data = {
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
            },
            {
                "soil_moisture": 600.0,
                "temperature": 28.0,
                "air_humidity": 60.0
            }
        ]
    }
    
    response = requests.post(f"{BASE_URL}/predict/batch", json=data)
    print(f"Status Code: {response.status_code}")
    print("\nResponse:")
    print(json.dumps(response.json(), indent=2))

def test_model_statistics():
    """Test model statistics endpoint"""
    print("\n" + "="*60)
    print("Testing Model Statistics Endpoint")
    print("="*60)
    response = requests.get(f"{BASE_URL}/model/statistics")
    print(f"Status Code: {response.status_code}")
    print(json.dumps(response.json(), indent=2))

def main():
    """Run all tests"""
    print("\n🧪 Starting API Tests...")
    print("Make sure the API is running at http://localhost:8000")
    
    try:
        # Test all endpoints
        test_root()
        test_health()
        test_model_info()
        test_single_prediction()
        test_batch_prediction()
        test_model_statistics()
        
        print("\n" + "="*60)
        print("✅ All tests completed successfully!")
        print("="*60)
        
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to the API.")
        print("Please make sure the API is running with: python main.py")
    except Exception as e:
        print(f"\n❌ Error during testing: {e}")

if __name__ == "__main__":
    main()
