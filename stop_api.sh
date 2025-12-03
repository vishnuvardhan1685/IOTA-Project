#!/bin/bash

# Stop all running instances of the API

echo "🛑 Stopping Water Pump Prediction API..."
echo "========================================"

# Stop Python processes
echo "Stopping Python processes..."
pkill -f "main.py"

# Stop Docker containers
if docker ps | grep -q "pump-api"; then
    echo "Stopping Docker container..."
    docker stop pump-api
    docker rm pump-api
fi

# Stop Docker Compose
if [ -f "docker-compose.yml" ]; then
    echo "Stopping Docker Compose services..."
    docker-compose down 2>/dev/null
fi

# Kill ngrok
if pgrep -x "ngrok" > /dev/null; then
    echo "Stopping ngrok..."
    pkill ngrok
fi

# Kill cloudflared
if pgrep -x "cloudflared" > /dev/null; then
    echo "Stopping cloudflared..."
    pkill cloudflared
fi

echo ""
echo "✅ All services stopped!"
echo ""

# Check if anything is still running on port 8000
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null ; then
    echo "⚠️  Something is still running on port 8000"
    echo "Process details:"
    lsof -i :8000
    echo ""
    read -p "Force kill? (y/n): " force
    if [ "$force" = "y" ]; then
        lsof -ti:8000 | xargs kill -9
        echo "✅ Force killed!"
    fi
else
    echo "✅ Port 8000 is now free"
fi
