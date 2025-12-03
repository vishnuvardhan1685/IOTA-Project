# 🚀 QUICK DEPLOYMENT GUIDE

Your Water Pump Prediction API is ready to deploy! Here are your options:

---

## ⚡ FASTEST METHOD: Make API Public in 2 Minutes

### Step 1: Start the API
```bash
./quick_deploy.sh
```

### Step 2: Install ngrok (if not installed)
```bash
# For Mac
brew install ngrok

# Or download from: https://ngrok.com/download
```

### Step 3: Expose API Publicly
```bash
ngrok http 8000
```

You'll get a public URL like: `https://abc123.ngrok.io`

✅ **Done!** Your API is now accessible from anywhere!

---

## 🎯 ALL DEPLOYMENT OPTIONS

### Option 1: Local Network (Easiest)
```bash
python main.py
```
Access at: `http://localhost:8000`

### Option 2: Public URL with ngrok (Quick & Easy)
```bash
# Start API
python main.py

# In new terminal
ngrok http 8000
```
Get public URL instantly!

### Option 3: Docker (Production Ready)
```bash
# Build and run
docker build -t water-pump-api .
docker run -d -p 8000:8000 water-pump-api
```

### Option 4: Docker Compose (Easiest Docker)
```bash
docker-compose up -d
```

### Option 5: Production Server
```bash
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Option 6: Background Service
```bash
nohup python main.py > api.log 2>&1 &
```

---

## 📋 HELPFUL SCRIPTS

| Script | Purpose |
|--------|---------|
| `./quick_deploy.sh` | Quick start with ngrok |
| `./deploy.sh` | Interactive deployment menu |
| `./stop_api.sh` | Stop all running instances |

---

## 🌐 CLOUD DEPLOYMENT (Free Options)

### Railway.app (Recommended - Free & Easy)
1. Visit [railway.app](https://railway.app)
2. Click "Start New Project"
3. Connect GitHub or deploy from template
4. Railway auto-detects FastAPI
5. Get instant deployment URL!

### Render.com (Also Free)
1. Visit [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect GitHub repo
4. Build: `pip install -r requirements.txt`
5. Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Deploy!

### Heroku (Classic)
```bash
# Install Heroku CLI
brew install heroku

# Login
heroku login

# Create app
heroku create water-pump-api

# Deploy
git init
git add .
git commit -m "Deploy"
git push heroku main
```

---

## 🧪 TEST YOUR DEPLOYED API

```bash
# Replace URL with your deployed URL
curl -X POST "YOUR_URL/predict" \
  -H "Content-Type: application/json" \
  -d '{"soil_moisture": 450, "temperature": 28, "air_humidity": 65}'
```

Expected response: `{"prediction": 0}` or `{"prediction": 1}`

---

## 📦 FILES CREATED FOR DEPLOYMENT

✅ `requirements.txt` - Python dependencies
✅ `Dockerfile` - Docker container definition
✅ `docker-compose.yml` - Docker Compose config
✅ `Procfile` - Heroku/Railway deployment
✅ `runtime.txt` - Python version specification
✅ `.dockerignore` - Docker build exclusions
✅ `deploy.sh` - Interactive deployment script
✅ `quick_deploy.sh` - Quick ngrok deployment
✅ `stop_api.sh` - Stop all services

---

## 🔧 COMMON COMMANDS

```bash
# Start API locally
python main.py

# Check if running
curl http://localhost:8000/health

# Stop API
./stop_api.sh

# View logs (if running in background)
tail -f api.log

# Build Docker image
docker build -t water-pump-api .

# Run Docker container
docker run -d -p 8000:8000 water-pump-api

# Check Docker logs
docker logs pump-api
```

---

## 🎓 RECOMMENDED FOR BEGINNERS

**Best Option**: Railway.app or Render.com
- ✅ Completely free
- ✅ No credit card required
- ✅ Auto-deployment from GitHub
- ✅ Free SSL/HTTPS
- ✅ Custom domain support
- ✅ Easy to use

**For Local/Demo**: ngrok
- ✅ Instant public URL
- ✅ No configuration needed
- ✅ Perfect for testing
- ⚠️ URL changes on restart (free plan)

---

## 💡 NEXT STEPS

1. **Choose your deployment method** from above
2. **Deploy the API**
3. **Test with the public URL**
4. **Share your API endpoint!**

### Example Usage After Deployment:
```python
import requests

# Replace with your deployed URL
API_URL = "https://your-api-url.com/predict"

response = requests.post(API_URL, json={
    "soil_moisture": 450,
    "temperature": 28,
    "air_humidity": 65
})

print(response.json())  # {"prediction": 1}
```

---

## 🆘 NEED HELP?

- API not starting? Check `api.log`
- Port already in use? Run `./stop_api.sh`
- Model files missing? Run `python model_training.py`
- Docker issues? Make sure Docker is running

---

## 📊 WHAT'S RUNNING?

Check current status:
```bash
# Check port 8000
lsof -i :8000

# Check Docker containers
docker ps

# Check logs
tail -f api.log
```

---

**Ready to deploy? Choose a method and get started! 🚀**
