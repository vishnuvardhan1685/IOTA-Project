# Simplified Water Pump Prediction API

The FastAPI has been updated to return **only boolean values (0 or 1)** in the response.

## 🎯 Response Format

### Single Prediction
**Endpoint:** `POST /predict`

**Response:**
```json
{
  "prediction": 0  // or 1
}
```

- `0` = Pump OFF
- `1` = Pump ON

### Batch Prediction
**Endpoint:** `POST /predict/batch`

**Response:**
```json
{
  "predictions": [1, 0, 1, 0]
}
```

Returns an array of 0s and 1s for each sensor reading.

---

## 📋 Quick Examples

### Example 1: Low Soil Moisture (Pump ON)
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"soil_moisture": 400, "temperature": 33, "air_humidity": 77}'
```

**Response:**
```json
{"prediction": 1}
```

---

### Example 2: High Soil Moisture (Pump OFF)
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"soil_moisture": 850, "temperature": 28, "air_humidity": 55}'
```

**Response:**
```json
{"prediction": 0}
```

---

### Example 3: Batch Prediction
```bash
curl -X POST "http://localhost:8000/predict/batch" \
  -H "Content-Type: application/json" \
  -d '{
    "sensors": [
      {"soil_moisture": 400, "temperature": 33, "air_humidity": 77},
      {"soil_moisture": 800, "temperature": 32, "air_humidity": 50},
      {"soil_moisture": 500, "temperature": 25, "air_humidity": 65}
    ]
  }'
```

**Response:**
```json
{"predictions": [1, 0, 1]}
```

---

## 🚀 Starting the API

```bash
python main.py
```

The API will run at: `http://localhost:8000`

---

## 📡 Available Endpoints

| Endpoint | Method | Description | Response |
|----------|--------|-------------|----------|
| `/predict` | POST | Single prediction | `{"prediction": 0 or 1}` |
| `/predict/batch` | POST | Multiple predictions | `{"predictions": [0, 1, ...]}` |
| `/health` | GET | Health check | Status info |
| `/model/info` | GET | Model information | Model details |
| `/model/statistics` | GET | Model statistics | Feature importance |
| `/docs` | GET | Interactive API docs | Swagger UI |
| `/redoc` | GET | Alternative docs | ReDoc |

---

## 💡 Understanding the Response

- **`1` (Pump ON)**: Soil moisture is low, pump needs to turn on to water the soil
- **`0` (Pump OFF)**: Soil moisture is sufficient, pump should remain off

The model makes this decision primarily based on soil moisture levels:
- Soil Moisture < ~650 → Pump ON (1)
- Soil Moisture > ~650 → Pump OFF (0)

---

## 🔧 Integration Examples

### Python
```python
import requests

response = requests.post(
    "http://localhost:8000/predict",
    json={
        "soil_moisture": 450,
        "temperature": 28,
        "air_humidity": 65
    }
)
prediction = response.json()["prediction"]
print(f"Pump should be: {'ON' if prediction == 1 else 'OFF'}")
```

### JavaScript
```javascript
fetch('http://localhost:8000/predict', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    soil_moisture: 450,
    temperature: 28,
    air_humidity: 65
  })
})
.then(res => res.json())
.then(data => {
  console.log(data.prediction === 1 ? 'Pump ON' : 'Pump OFF');
});
```

### Arduino/ESP32/IoT Device
```cpp
// Pseudo-code for IoT devices
String jsonData = "{\"soil_moisture\":" + String(soilValue) + 
                  ",\"temperature\":" + String(tempValue) + 
                  ",\"air_humidity\":" + String(humValue) + "}";

HTTPClient http;
http.begin("http://localhost:8000/predict");
http.addHeader("Content-Type", "application/json");
int httpCode = http.POST(jsonData);

if (httpCode == 200) {
  String response = http.getString();
  // Parse JSON: {"prediction": 0} or {"prediction": 1}
  int pumpStatus = /* extract prediction from response */;
  digitalWrite(PUMP_PIN, pumpStatus == 1 ? HIGH : LOW);
}
```

---

## ✅ Benefits of Simplified Response

1. **Minimal bandwidth**: Only 1 byte of information needed
2. **Easy parsing**: Simple JSON structure
3. **IoT-friendly**: Perfect for constrained devices
4. **Clear logic**: Binary decision (ON/OFF)
5. **Fast processing**: No extra data to transmit

---

## 📊 Model Performance

- **Accuracy**: 99.83%
- **Precision**: 100% for both classes
- **Training samples**: 2,400
- **Test samples**: 600

---

**Last Updated**: December 4, 2025  
**API Version**: 2.0.0 (Simplified)
