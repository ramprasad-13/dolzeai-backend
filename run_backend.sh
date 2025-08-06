#!/bin/bash

# run_backend.sh
# A script to set up and run the Reely AI FastAPI backend.

echo "--- Starting Reely AI Backend Setup ---"

# Ensure the script is run from the 'backend' directory where main.py is located.
if [ ! -f "main.py" ] || [ ! -f "requirements.txt" ]; then
    echo "Error: This script must be run from within the 'backend' directory."
    exit 1
fi

# Define the path to the virtual environment's python executable
VENV_PYTHON="venv/bin/python"

# Step 1: Check if the virtual environment exists.
# If it doesn't, create it and install dependencies using its specific python/pip.
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating and setting it up..."
    
    # Create the virtual environment using python3
    python3 -m venv venv
    
    # Install required packages using the venv's pip
    echo "Installing dependencies from requirements.txt..."
    "$VENV_PYTHON" -m pip install -r requirements.txt
    
    echo "Setup complete."
fi

# Step 2: Run the FastAPI server using the venv's python executable.
# This is the most reliable method as it doesn't depend on shell activation.
echo "Starting FastAPI server on http://localhost:8000..."
echo "Press CTRL+C to stop the server."

"$VENV_PYTHON" -m uvicorn main:app --reload --port 8000

echo "Server stopped."
