Reely AI - Smart Content Studio
Reely AI is a modern web application that leverages artificial intelligence to assist users with various content creation tasks. It features a responsive frontend built with React and Tailwind CSS, user authentication handled by Firebase, and a Python FastAPI backend that connects to the Gemini Large Language Model for content generation.

🚀 Getting Started
Prerequisites
Backend: Python 3.9+

Frontend: Node.js v20+

Firebase: A Firebase project with Authentication and a service account key.

Gemini API Key: A valid API key for the Google Gemini LLM.

🐍 Backend Setup (FastAPI)
The backend is a Python server built with the FastAPI framework. It provides the API endpoints that the frontend consumes for AI-powered tasks.

1. Navigate to the Backend Directory
cd backend

2. Configure Environment Variables
You need to set up two crucial configuration files in the backend directory.

Create a .env file for your Gemini API Key:

# backend/.env
GOOGLE_API_KEY="YOUR_GEMINI_API_KEY_HERE"

Add your Firebase Service Account Key:

Go to your Firebase project settings and generate a new private key in the "Service Accounts" tab.

This will download a JSON file. Move this file into the backend directory and rename it to firebase-service-account.json.

Important: These files contain sensitive information. Ensure they are listed in your .gitignore file to prevent them from being committed to your repository.

3. Run the Server
A shell script is provided to automate the setup and execution process.

Make the script executable (you only need to do this once):

chmod +x run_backend.sh

Start the backend server:

./run_backend.sh

This script will automatically:

Create a Python virtual environment (venv) if it doesn't exist.

Install all required dependencies from requirements.txt.

Start the FastAPI server with auto-reload.

The backend API will be running at http://localhost:8000.

⚛️ Frontend Setup (React + Vite)
The frontend is a single-page application built with React and Vite, styled with Tailwind CSS.

1. Navigate to the Frontend Directory
cd frontend

2. Configure Firebase
You need to connect the frontend to your Firebase project.

In the frontend/src/ directory, locate the firebase.js file.

Replace the placeholder firebaseConfig object with your actual project credentials from the Firebase console (Project Settings > General > Your apps > SDK setup and configuration).

// frontend/src/firebase.js
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_STORAGE_BUCKET",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID"
};

3. Install Dependencies
npm install

4. Run the Development Server
npm run dev

The frontend application will be available at http://localhost:5173.

☁️ Deployment
This application is configured for deployment with the following services:

Backend: Deployed on Render.

Frontend: Deployed on Vercel or Firebase Hosting.

Refer to the deployment guides for each service for specific instructions on connecting your GitHub repository and setting up environment variables.
