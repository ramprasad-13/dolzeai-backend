# backend/main.py

import os
import google.generativeai as genai
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends # <-- Add Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from auth import get_current_user # <-- Import our new function

# --- Application Setup ---
load_dotenv()
app = FastAPI()

# --- CORS Configuration ---
origins = [
    "https://dolzeai-frontend.vercel.app/login",
    "https://dolzeai-backend.onrender.com",
    "http://localhost:3000", # The default port for React's development server
    "http://localhost:5173", # The default port for Vite + React
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Gemini API Configuration ---
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables.")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    print(f"Error configuring Gemini API: {e}")
    model = None

# --- Pydantic Models for Request Bodies ---
class TextRequest(BaseModel):
    text: str

class IdeaRequest(BaseModel):
    topic: str

class RefineRequest(BaseModel):
    text: str
    instruction: str # e.g., "make it more formal", "add more humor"

class ChatRequest(BaseModel):
    query: str

# --- API Endpoints ---

@app.get("/api")
def read_root():
    """A simple public endpoint to confirm the server is running."""
    return {"message": "Welcome to the Reely AI Backend!"}

# This is how you protect an endpoint. FastAPI will run get_current_user
# before running the endpoint's logic. If authentication fails,
# it will automatically send a 401 Unauthorized response.

@app.post("/api/summarize")
async def summarize_text(request: TextRequest, user: dict = Depends(get_current_user)):
    """Endpoint to summarize a given block of text."""
    if not model:
        raise HTTPException(status_code=500, detail="Gemini API not configured.")
    try:
        # The 'user' variable now contains the decoded token, e.g., user['uid']
        print(f"Request received from user: {user['uid']}")
        prompt = f"Please provide a concise summary of the following text:\n\n{request.text}"
        response = model.generate_content(prompt)
        return {"summary": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating summary: {str(e)}")

@app.post("/api/generate-ideas")
async def generate_ideas(request: IdeaRequest, user: dict = Depends(get_current_user)):
    """Endpoint to generate creative ideas based on a topic."""
    if not model:
        raise HTTPException(status_code=500, detail="Gemini API not configured.")
    try:
        prompt = f"Generate a list of creative ideas for the following topic: {request.topic}. Please format them as a bulleted or numbered list."
        response = model.generate_content(prompt)
        return {"ideas": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating ideas: {str(e)}")

@app.post("/api/refine-content")
async def refine_content(request: RefineRequest, user: dict = Depends(get_current_user)):
    """Endpoint to refine text based on an instruction."""
    if not model:
        raise HTTPException(status_code=500, detail="Gemini API not configured.")
    try:
        # If the instruction is empty, use a default one.
        instruction = request.instruction if request.instruction else "improve the grammar and clarity"
        prompt = f"Please refine the following text based on this instruction: '{instruction}'.\n\nOriginal Text:\n{request.text}\n\nRefined Text:"
        response = model.generate_content(prompt)
        return {"refined_text": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error refining content: {str(e)}")

@app.post("/api/chat")
async def chat_with_bot(request: ChatRequest, user: dict = Depends(get_current_user)):
    """Endpoint for a simple chatbot."""
    if not model:
        raise HTTPException(status_code=500, detail="Gemini API not configured.")
    try:
        # You can build a more complex personality here if you want
        prompt = f"You are a helpful assistant. Respond to the following user query in a conversational tone: {request.query}"
        response = model.generate_content(prompt)
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in chat: {str(e)}")
