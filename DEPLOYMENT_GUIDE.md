# Deployment Guide for Water Pump Prediction API

This guide covers multiple deployment options for your FastAPI application.

---

## 📦 Prerequisites

Before deploying, ensure you have:
1. All model files (`pump_prediction_model.pkl` and `scaler.pkl`)
2. Python 3.9 or higher
3. All dependencies listed in `requirements.txt`

---

## 🚀 Deployment Options

### Option 1: Local Production Server (Recommended for Testing)
### Option 2: Docker Container (Recommended for Production)
### Option 3: Cloud Platforms (AWS, Google Cloud, Azure)
### Option 4: Heroku (Simple Cloud Deployment)
### Option 5: Railway/Render (Modern Cloud Platforms)

---

## Option 1: Local Production Server

### Step 1: Install Production Server
```bash
pip install uvicorn gunicorn
```

### Step 2: Run with Uvicorn (Single Worker)
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Step 3: Run with Gunicorn (Multiple Workers)
```bash
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Step 4: Run as Background Service (Linux/Mac)
```bash
nohup uvicorn main:app --host 0.0.0.0 --port 8000 > api.log 2>&1 &
```

### Step 5: Access Your API
- Local: `http://localhost:8000`
- Network: `http://YOUR_LOCAL_IP:8000`

---

## Option 2: Docker Deployment (Recommended)

### Why Docker?
- ✅ Consistent environment across all platforms
- ✅ Easy to scale and manage
- ✅ Isolated dependencies
- ✅ Simple deployment to cloud platforms

### Step 1: Build Docker Image
```bash
docker build -t water-pump-api .
```

### Step 2: Run Docker Container
```bash
docker run -d -p 8000:8000 --name pump-api water-pump-api
```

### Step 3: Check Container Status
```bash
docker ps
docker logs pump-api
```

### Step 4: Stop/Start Container
```bash
docker stop pump-api
docker start pump-api
```

### Step 5: Remove Container
```bash
docker rm -f pump-api
```

---

## Option 3: Cloud Platforms

### AWS EC2 Deployment

1. **Launch EC2 Instance**
   - Choose Ubuntu 20.04 LTS
   - Instance type: t2.micro (free tier) or t2.small
   - Configure security group: Allow inbound traffic on port 8000

2. **Connect to EC2**
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-ip
   ```

3. **Install Dependencies**
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv -y
   ```

4. **Upload Files**
   ```bash
   scp -i your-key.pem -r * ubuntu@your-ec2-ip:~/app/
   ```

5. **Setup and Run**
   ```bash
   cd ~/app
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

6. **Access API**
   - `http://your-ec2-public-ip:8000`

### AWS Lambda + API Gateway

1. Use AWS SAM or Serverless Framework
2. Package your application with Mangum adapter
3. Deploy to Lambda with API Gateway trigger

### Google Cloud Run

1. Build and push Docker image to Google Container Registry
2. Deploy to Cloud Run
3. Automatically scales and provides HTTPS endpoint

---

## Option 4: Heroku Deployment

### Step 1: Create Heroku Account
Sign up at [heroku.com](https://heroku.com)

### Step 2: Install Heroku CLI
```bash
# Mac
brew tap heroku/brew && brew install heroku

# Ubuntu/Debian
curl https://cli-assets.heroku.com/install.sh | sh
```

### Step 3: Login to Heroku
```bash
heroku login
```

### Step 4: Create Heroku App
```bash
heroku create water-pump-prediction-api
```

### Step 5: Deploy
```bash
git init
git add .
git commit -m "Initial deployment"
git push heroku main
```

### Step 6: Access Your API
```bash
heroku open
```

Your API will be at: `https://water-pump-prediction-api.herokuapp.com`

---

## Option 5: Railway / Render Deployment

### Railway

1. Visit [railway.app](https://railway.app)
2. Connect your GitHub repository
3. Railway auto-detects FastAPI
4. Click "Deploy"
5. Get your deployment URL

### Render

1. Visit [render.com](https://render.com)
2. Create new Web Service
3. Connect your GitHub repository
4. Select Python environment
5. Build command: `pip install -r requirements.txt`
6. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
7. Click "Deploy"

---

## 🔒 Production Best Practices

### 1. Use Environment Variables
```python
import os
PORT = int(os.getenv("PORT", 8000))
```

### 2. Enable CORS Properly
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],  # Specific domains
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

### 3. Add Rate Limiting
```bash
pip install slowapi
```

### 4. Enable HTTPS
Use Let's Encrypt for free SSL certificates or use cloud provider's HTTPS

### 5. Monitor Your API
- Use logging
- Set up health checks
- Monitor response times

### 6. Backup Model Files
Keep backups of `.pkl` files in cloud storage

---

## 🌐 Making API Publicly Accessible (From Local)

### Using ngrok (Quick Testing)

1. **Install ngrok**
   ```bash
   # Mac
   brew install ngrok
   
   # Or download from ngrok.com
   ```

2. **Start Your API**
   ```bash
   python main.py
   ```

3. **Expose with ngrok**
   ```bash
   ngrok http 8000
   ```

4. **Get Public URL**
   ngrok provides a public URL like: `https://abc123.ngrok.io`

### Using Cloudflare Tunnel (Free Alternative)

1. **Install cloudflared**
   ```bash
   # Mac
   brew install cloudflare/cloudflare/cloudflared
   ```

2. **Start Tunnel**
   ```bash
   cloudflared tunnel --url http://localhost:8000
   ```

3. **Get Public URL**
   Provides a URL like: `https://xyz.trycloudflare.com`

---

## 📊 Performance Optimization

### 1. Use Multiple Workers
```bash
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

### 2. Enable Caching
For repeated predictions, consider caching results

### 3. Load Balancing
Use nginx or cloud load balancers for high traffic

### 4. Database for Logging
Store predictions in a database for analytics

---

## 🔍 Testing Deployed API

```bash
# Test health endpoint
curl https://your-api-url.com/health

# Test prediction
curl -X POST "https://your-api-url.com/predict" \
  -H "Content-Type: application/json" \
  -d '{"soil_moisture": 450, "temperature": 28, "air_humidity": 65}'
```

---

## 📝 Deployment Checklist

- [ ] Create `requirements.txt`
- [ ] Create `Dockerfile`
- [ ] Create `Procfile` (for Heroku)
- [ ] Test locally with production settings
- [ ] Set up environment variables
- [ ] Configure CORS properly
- [ ] Enable logging
- [ ] Set up monitoring
- [ ] Configure domain name (optional)
- [ ] Enable HTTPS
- [ ] Test all endpoints
- [ ] Set up automatic backups
- [ ] Document API endpoints

---

## 💰 Cost Comparison

| Platform | Free Tier | Cost | Ease | Scalability |
|----------|-----------|------|------|-------------|
| Local Server | ✅ Free | $0 | ⭐⭐⭐⭐⭐ | ⭐ |
| Docker (Local) | ✅ Free | $0 | ⭐⭐⭐⭐ | ⭐⭐ |
| ngrok | ✅ Limited | $0-$8/mo | ⭐⭐⭐⭐⭐ | ⭐ |
| Heroku | ✅ Yes | $0-$7/mo | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Railway | ✅ $5 free | $0-$10/mo | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Render | ✅ Yes | $0-$7/mo | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| AWS EC2 | ✅ 1 year | $5-$50/mo | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Google Cloud | ✅ $300 credit | $5-$50/mo | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## 🆘 Troubleshooting

### Port Already in Use
```bash
# Find process using port 8000
lsof -i :8000
# Kill it
kill -9 <PID>
```

### Model Files Not Found
Ensure `.pkl` files are in the same directory as `main.py`

### Module Not Found
```bash
pip install -r requirements.txt
```

### Permission Denied
```bash
chmod +x main.py
```

---

**Next Steps**: Choose your deployment method and follow the specific guide above!
