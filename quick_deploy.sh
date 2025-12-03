#!/bin/bash

# Quick Start - Deploy API and Make it Publicly Accessible

echo "🚀 Water Pump Prediction API - Quick Public Deployment"
echo "========================================================"
echo ""

# Check if API is already running
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null ; then
    echo "✅ API is already running on port 8000"
else
    echo "📦 Starting API server..."
    cd "/Users/vishnuvardhan_1685/Desktop/IOTA Project"
    nohup "/Users/vishnuvardhan_1685/Desktop/IOTA Project/.venv/bin/python" main.py > api.log 2>&1 &
    sleep 3
    echo "✅ API started successfully!"
fi

echo ""
echo "🌐 Your API is accessible at:"
echo "   Local: http://localhost:8000"
echo "   Docs:  http://localhost:8000/docs"
echo ""

# Check if ngrok is installed
if command -v ngrok &> /dev/null; then
    echo "🔗 Creating public URL with ngrok..."
    echo "   Press Ctrl+C to stop"
    echo ""
    ngrok http 8000
else
    echo "⚠️  ngrok not found. Install it to create a public URL:"
    echo ""
    echo "   For Mac: brew install ngrok"
    echo "   Or visit: https://ngrok.com/download"
    echo ""
    echo "   After installing, run: ngrok http 8000"
    echo ""
    echo "💡 Alternative: Use Cloudflare Tunnel"
    echo "   brew install cloudflared"
    echo "   cloudflared tunnel --url http://localhost:8000"
fi
