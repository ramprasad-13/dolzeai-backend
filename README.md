Reely AI - Backend (FastAPI)
This directory contains the Python backend for the Reely AI application, built with the FastAPI framework. It provides the API endpoints that the frontend consumes for authentication and AI-powered content generation tasks via the Gemini LLM.

🚀 Getting Started
Prerequisites
Python 3.9+: Ensure you have a compatible version of Python installed.

Firebase Service Account: A firebase-service-account.json key file is required for verifying user tokens.

Gemini API Key: A valid API key for the Google Gemini LLM.

⚙️ Local Setup and Installation
1. Navigate to the Backend Directory
All commands should be run from within the backend folder.

cd backend

2. Configure Environment Variables
You need to set up two crucial configuration files:

Create a .env file for your Gemini API Key. This file should contain a single line:

# backend/.env
GOOGLE_API_KEY="YOUR_GEMINI_API_KEY_HERE"

Add your Firebase Service Account Key:

In your Firebase project settings, go to the "Service Accounts" tab and click "Generate new private key".

This will download a JSON file. Move this file into the backend directory and rename it to firebase-service-account.json.

Important: These files contain sensitive information. It is critical that you add .env and firebase-service-account.json to your .gitignore file to prevent them from being committed to your repository.

3. Run the Server
A shell script is provided to automate the setup and execution process. This is the recommended way to run the server locally.

Make the script executable (you only need to do this once):

chmod +x run_backend.sh

Start the backend server:

./run_backend.sh

This script will automatically:

Create a Python virtual environment (venv) if one doesn't exist.

Install all required Python packages from requirements.txt.

Start the FastAPI server with auto-reload at http://localhost:8000.

☁️ Deployment
This backend is configured for deployment on Render. The Procfile included in this directory tells Render how to run the application in a production environment.

When deploying, you must set the GOOGLE_API_KEY and the contents of firebase-service-account.json as environment variables in the Render dashboard.
