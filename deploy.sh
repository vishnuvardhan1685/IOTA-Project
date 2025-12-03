#!/bin/bash

# Water Pump Prediction API - Quick Deployment Script

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║     Water Pump Prediction API - Deployment Script           ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Color codes
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored messages
print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

# Check if model files exist
echo "Checking for required files..."
if [ ! -f "pump_prediction_model.pkl" ] || [ ! -f "scaler.pkl" ]; then
    print_error "Model files not found!"
    echo "Please run 'python model_training.py' first to generate model files."
    exit 1
fi
print_success "Model files found"

# Check if main.py exists
if [ ! -f "main.py" ]; then
    print_error "main.py not found!"
    exit 1
fi
print_success "main.py found"

echo ""
echo "Select deployment method:"
echo "1) Local Development Server (uvicorn)"
echo "2) Production Server (gunicorn with multiple workers)"
echo "3) Docker Container"
echo "4) Docker Compose"
echo "5) Expose via ngrok (public URL)"
echo "6) Background Service (nohup)"
echo "7) Check if API is running"
echo "8) Stop running API"
echo ""
read -p "Enter your choice (1-8): " choice

case $choice in
    1)
        print_info "Starting local development server..."
        uvicorn main:app --host 0.0.0.0 --port 8000 --reload
        ;;
    
    2)
        print_info "Starting production server with 4 workers..."
        if ! command -v gunicorn &> /dev/null; then
            print_error "gunicorn not installed. Installing..."
            pip install gunicorn
        fi
        gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
        ;;
    
    3)
        print_info "Building Docker image..."
        docker build -t water-pump-api .
        if [ $? -eq 0 ]; then
            print_success "Docker image built successfully"
            print_info "Starting Docker container..."
            docker run -d -p 8000:8000 --name pump-api water-pump-api
            if [ $? -eq 0 ]; then
                print_success "Container started successfully!"
                print_info "API is running at http://localhost:8000"
                print_info "Check logs: docker logs pump-api"
            else
                print_error "Failed to start container"
            fi
        else
            print_error "Failed to build Docker image"
        fi
        ;;
    
    4)
        print_info "Starting with Docker Compose..."
        if ! command -v docker-compose &> /dev/null; then
            print_error "docker-compose not installed!"
            exit 1
        fi
        docker-compose up -d
        if [ $? -eq 0 ]; then
            print_success "Services started successfully!"
            print_info "API is running at http://localhost:8000"
            print_info "Check logs: docker-compose logs -f"
        fi
        ;;
    
    5)
        print_info "Exposing API via ngrok..."
        if ! command -v ngrok &> /dev/null; then
            print_error "ngrok not installed!"
            echo "Install from: https://ngrok.com/download"
            exit 1
        fi
        
        # Start API in background
        print_info "Starting API server..."
        nohup uvicorn main:app --host 0.0.0.0 --port 8000 > api.log 2>&1 &
        API_PID=$!
        sleep 3
        
        print_success "API started (PID: $API_PID)"
        print_info "Exposing via ngrok..."
        ngrok http 8000
        ;;
    
    6)
        print_info "Starting as background service..."
        nohup uvicorn main:app --host 0.0.0.0 --port 8000 > api.log 2>&1 &
        API_PID=$!
        print_success "API started in background (PID: $API_PID)"
        echo $API_PID > api.pid
        print_info "API is running at http://localhost:8000"
        print_info "Logs: tail -f api.log"
        print_info "Stop: kill $API_PID or ./deploy.sh and select option 8"
        ;;
    
    7)
        print_info "Checking API status..."
        response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/health 2>/dev/null)
        if [ "$response" = "200" ]; then
            print_success "API is running at http://localhost:8000"
            # Get API info
            curl -s http://localhost:8000/ | python -m json.tool
        else
            print_error "API is not running"
        fi
        ;;
    
    8)
        print_info "Stopping API..."
        
        # Kill Python processes
        pkill -f "main.py"
        
        # Stop Docker containers
        if docker ps | grep -q "pump-api"; then
            docker stop pump-api
            docker rm pump-api
            print_success "Docker container stopped"
        fi
        
        # Stop Docker Compose
        if [ -f "docker-compose.yml" ]; then
            docker-compose down 2>/dev/null
        fi
        
        # Kill ngrok if running
        pkill -f ngrok
        
        print_success "All services stopped"
        ;;
    
    *)
        print_error "Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                    Deployment Complete!                      ║"
echo "╚══════════════════════════════════════════════════════════════╝"
