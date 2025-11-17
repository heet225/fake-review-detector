#!/bin/bash

# Fake Review Detector - Startup Script

echo "========================================"
echo "  Fake Review Detector"
echo "========================================"
echo ""

# Navigate to project directory
cd "$(dirname "$0")/project"

# Check if dependencies are installed
echo "Checking dependencies..."
python3 -c "import flask, sklearn, pandas, nltk" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Dependencies not found. Installing..."
    pip install -r ../requirements.txt
fi

# Check if model files exist
if [ ! -f "svm_model.pkl" ] || [ ! -f "vectorizer.pkl" ]; then
    echo ""
    echo "Model files not found. Training model..."
    echo "This may take a few moments..."
    python3 trainsvm.py
    echo ""
fi

# Start Flask application
echo "Starting Flask application..."
echo ""
echo "========================================"
echo "  Access the app at: http://127.0.0.1:5000"
echo "  Press CTRL+C to quit"
echo "========================================"
echo ""

python3 app.py
