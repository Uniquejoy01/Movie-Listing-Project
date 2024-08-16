from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database, auth

router = APIRouter()

@router.post("/movies/{movie_id}/comments", response_model=schemas.Comment)
def create_comment(movie_id: int, comment: schemas.CommentCreate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    comment.movie_id = movie_id
    return crud.create_comment(db=db, comment=comment, user_id=current_user.id)

@router.get("/movies/{movie_id}/comments", response_model=list[schemas.Comment])
def get_comments(movie_id: int, db: Session = Depends(database.get_db)):
    return crud.get_comments(db=db, movie_id=movie_id)
