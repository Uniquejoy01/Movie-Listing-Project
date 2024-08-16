from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database, auth

router = APIRouter()

@router.post("/movies/{movie_id}/ratings", response_model=schemas.Rating)
def create_rating(movie_id: int, rating: schemas.RatingCreate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    rating.movie_id = movie_id
    return crud.create_rating(db=db, rating=rating, user_id=current_user.id)

@router.get("/movies/{movie_id}/ratings", response_model=list[schemas.Rating])
def get_ratings(movie_id: int, db: Session = Depends(database.get_db)):
    return crud.get_ratings(db=db, movie_id=movie_id)
