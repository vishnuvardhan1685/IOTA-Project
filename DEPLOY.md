# 🚀 Quick Vercel Deployment Guide

## Step 1: Install Vercel CLI (if not already installed)
```bash
npm install -g vercel
```

## Step 2: Login to Vercel
```bash
vercel login
```

## Step 3: Deploy from this directory
```bash
cd "/Users/vishnuvardhan_1685/Desktop/IOTA Project"
vercel
```

## Step 4: Follow the prompts
- Set up and deploy? **Y**
- Which scope? Select your account
- Link to existing project? **N** (first time)
- Project name? Press Enter (or type custom name)
- Directory? Press Enter (current directory)
- Override settings? **N**

## Step 5: Deploy to Production
```bash
vercel --prod
```

## 🎉 Done!
Your API will be live at: `https://your-project-name.vercel.app`

## Quick Test
```bash
curl https://your-project-name.vercel.app/health
```

## View in Browser
- API Docs: `https://your-project-name.vercel.app/docs`
- API Info: `https://your-project-name.vercel.app/`

---

## Alternative: Deploy from GitHub

1. Push to GitHub:
```bash
git add .
git commit -m "Deploy to Vercel"
git push origin main
```

2. Visit [vercel.com](https://vercel.com)
3. Click "New Project"
4. Import your repository
5. Deploy!

---

## Test Your Deployed API

```bash
# Replace YOUR_URL with your Vercel URL
curl -X POST "YOUR_URL/predict" \
  -H "Content-Type: application/json" \
  -d '{"soil_moisture": 450, "temperature": 28, "air_humidity": 65}'
```

Expected response: `{"prediction": 0}` or `{"prediction": 1}`
