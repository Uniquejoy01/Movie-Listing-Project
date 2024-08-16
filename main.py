from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from auth import authenticate_user, create_access_token, get_current_user
import crud as crud, schema as schema
from database import engine, Base, get_db
from auth import pwd_context
from typing import Optional
# import sentry_sdk
from logger import get_logger
from fastapi.middleware.cors import CORSMiddleware
from .routes import user, movie, rating, comment

logger = get_logger(__name__)

Base.metadata.create_all(bind=engine)

# Initialize the database

# Create the FastAPI app
app = FastAPI()

@app.get('/')
def view_movie():
    return {"movie": "This is your movie"}

# CORS middleware (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as needed for your environment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routers
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(movie.router, prefix="/movies", tags=["Movies"])
app.include_router(rating.router, prefix="/ratings", tags=["Ratings"])
app.include_router(comment.router, prefix="/comments", tags=["Comments"])

# Root endpoint (optional)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Listing API"}
