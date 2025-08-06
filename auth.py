# backend/auth.py
import os
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import firebase_admin
from firebase_admin import credentials, auth

# --- Firebase Admin SDK Initialization ---
# This looks for the service account key file you downloaded.
# Ensure 'firebase-service-account.json' is in your 'backend' directory.
try:
    cred = credentials.Certificate('firebase-service-account.json')
    firebase_admin.initialize_app(cred)
except Exception as e:
    print(f"Error initializing Firebase Admin SDK: {e}")
    # This will prevent the app from starting if the key is missing or invalid,
    # which is good for security.
    raise e

# This tells FastAPI how to find the token in the request's "Authorization" header.
# The tokenUrl is not used for verification here, but it's a required parameter.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    This is a FastAPI "dependency". It will be run for every request
    to a protected endpoint. It verifies the Firebase ID token and returns
    the user's data if the token is valid.
    """
    try:
        # Firebase Admin SDK verifies the token. It checks the signature,
        # expiration time, and other claims.
        decoded_token = auth.verify_id_token(token)
        # You can optionally return the user's UID or the whole decoded token
        return decoded_token
    except Exception as e:
        # If verify_id_token fails, it raises an exception. We catch it
        # and return a standard 401 Unauthorized error.
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
