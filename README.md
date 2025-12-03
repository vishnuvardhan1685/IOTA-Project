# Water Pump Prediction API - Vercel Deployment

🚀 **FastAPI ML Model deployed on Vercel**

## 📋 Project Structure

```
IOTA Project/
├── api/
│   └── index.py                           # Main FastAPI application (Vercel entry point)
├── pump_prediction_model.pkl              # Trained ML model
├── scaler.pkl                             # Feature scaler
├── requirements.txt                       # Python dependencies
├── vercel.json                           # Vercel configuration
└── README.md                             # This file
```

## 🚀 Deploy to Vercel

### Method 1: Deploy from GitHub (Easiest ⭐)

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/IOTA-Project.git
   git push -u origin main
   ```

2. **Deploy on Vercel**
   - Visit [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will auto-detect and deploy!
   - Get your live URL: `https://your-project.vercel.app`

### Method 2: Deploy with Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   vercel
   ```

4. **Deploy to Production**
   ```bash
   vercel --prod
   ```

## 🔗 API Endpoints

Once deployed, your API will be available at: `https://your-project.vercel.app`

| Endpoint | Method | Description | Response |
|----------|--------|-------------|----------|
| `/` | GET | API info | API details |
| `/health` | GET | Health check | Status |
| `/predict` | POST | Single prediction | `{"prediction": 0 or 1}` |
| `/predict/batch` | POST | Batch predictions | `{"predictions": [0,1,1]}` |
| `/model/info` | GET | Model information | Model details |
| `/model/statistics` | GET | Model statistics | Statistics |
| `/docs` | GET | Interactive API docs | Swagger UI |

## 📝 API Usage Examples

### Single Prediction

```bash
curl -X POST "https://your-project.vercel.app/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "soil_moisture": 450,
    "temperature": 28,
    "air_humidity": 65
  }'
```

**Response:**
```json
{"prediction": 1}
```

- `0` = Pump OFF (soil has enough moisture)
- `1` = Pump ON (soil needs watering)

### Batch Prediction

```bash
curl -X POST "https://your-project.vercel.app/predict/batch" \
  -H "Content-Type: application/json" \
  -d '{
    "sensors": [
      {"soil_moisture": 400, "temperature": 33, "air_humidity": 77},
      {"soil_moisture": 800, "temperature": 32, "air_humidity": 50}
    ]
  }'
```

**Response:**
```json
{"predictions": [1, 0]}
```

## 🔧 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
uvicorn api.index:app --reload

# Access at http://localhost:8000
# Docs at http://localhost:8000/docs
```

## 📦 Model Details

- **Algorithm**: Logistic Regression
- **Accuracy**: 99.83%
- **Training Samples**: 2,400
- **Test Samples**: 600

### Input Features:
- **Soil Moisture**: 0-1000
- **Temperature**: -10 to 50°C
- **Air Humidity**: 0-100%

### Output:
- **0**: Pump OFF
- **1**: Pump ON

## 📱 Integration Examples

### Python
```python
import requests

url = "https://your-project.vercel.app/predict"
data = {
    "soil_moisture": 450,
    "temperature": 28,
    "air_humidity": 65
}

response = requests.post(url, json=data)
prediction = response.json()["prediction"]
print(f"Pump should be: {'ON' if prediction == 1 else 'OFF'}")
```

### JavaScript/Node.js
```javascript
const response = await fetch('https://your-project.vercel.app/predict', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    soil_moisture: 450,
    temperature: 28,
    air_humidity: 65
  })
});

const data = await response.json();
console.log(`Pump: ${data.prediction === 1 ? 'ON' : 'OFF'}`);
```

### Arduino/ESP32
```cpp
#include <HTTPClient.h>
#include <ArduinoJson.h>

HTTPClient http;
http.begin("https://your-project.vercel.app/predict");
http.addHeader("Content-Type", "application/json");

// Create JSON payload
String payload = "{\"soil_moisture\":" + String(soilMoisture) + 
                 ",\"temperature\":" + String(temperature) + 
                 ",\"air_humidity\":" + String(humidity) + "}";

int httpCode = http.POST(payload);
if (httpCode == 200) {
  String response = http.getString();
  // Parse JSON to get prediction value
  DynamicJsonDocument doc(1024);
  deserializeJson(doc, response);
  int prediction = doc["prediction"];
  
  // Control pump
  digitalWrite(PUMP_PIN, prediction == 1 ? HIGH : LOW);
}
http.end();
```

## 🌟 Vercel Features

✅ **Serverless** - No server management
✅ **Auto-scaling** - Handles traffic automatically
✅ **Global CDN** - Fast response times worldwide
✅ **HTTPS** - Automatic SSL certificates
✅ **Free tier** - Perfect for small projects
✅ **Zero config** - Just push and deploy
✅ **Monitoring** - Built-in analytics

## 🛠️ Troubleshooting

### Build Failed?
- Check `requirements.txt` has correct dependencies
- Ensure model files (`.pkl`) are in root directory
- Verify `vercel.json` is properly configured

### Model Not Loading?
- Verify `pump_prediction_model.pkl` and `scaler.pkl` exist
- Check file paths in `api/index.py`
- Review Vercel build logs

### API Not Responding?
- Check Vercel deployment logs
- Test `/health` endpoint first
- Verify CORS settings if calling from browser

### 413 Payload Too Large?
- Vercel has 4.5MB limit for serverless functions
- Use batch endpoint for multiple predictions
- Split large requests into smaller batches

## 📊 Vercel Dashboard

After deployment, monitor your API:
- **Analytics**: Track requests and response times
- **Logs**: View real-time logs
- **Deployments**: Manage versions
- **Settings**: Configure domains and environment variables

## 🔒 Security Best Practices

1. **Rate Limiting**: Consider adding rate limiting for production
2. **API Keys**: Add authentication if needed
3. **CORS**: Restrict origins in production
4. **Input Validation**: Already implemented via Pydantic

## 📈 Performance

- **Cold Start**: ~2-3 seconds (first request)
- **Warm Response**: ~100-200ms
- **Model Loading**: Cached after first load
- **Concurrent Requests**: Automatically scaled

## 🎯 Next Steps

1. ✅ Push code to GitHub
2. ✅ Deploy on Vercel
3. ✅ Get your API URL
4. ✅ Test endpoints
5. ✅ Integrate into your IoT system
6. ✅ Monitor usage

## 📄 Files Explanation

- **`api/index.py`**: Main FastAPI application (Vercel entry point)
- **`vercel.json`**: Vercel deployment configuration
- **`requirements.txt`**: Python package dependencies
- **`pump_prediction_model.pkl`**: Trained logistic regression model
- **`scaler.pkl`**: StandardScaler for feature normalization
- **`.vercelignore`**: Files to exclude from deployment

## 💡 Tips

- Use `/docs` endpoint to test API interactively
- Check `/health` to verify model is loaded
- Monitor Vercel dashboard for usage stats
- Enable branch deployments for testing

---

**🚀 Ready to Deploy?**

```bash
# Quick deploy command
vercel --prod
```

**📊 Model Accuracy**: 99.83%
**⚡ Response Time**: < 200ms
**🌍 Deployment**: Vercel Edge Network

---

**Need Help?** Check Vercel documentation at [vercel.com/docs](https://vercel.com/docs)
