from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import crud, schemas, database, auth

router = APIRouter()

@router.get("/movies", response_model=list[schemas.Movie])
def get_movies(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_movies(db=db, skip=skip, limit=limit)

@router.get("/movies/{movie_id}", response_model=schemas.Movie)
def get_movie(movie_id: int, db: Session = Depends(database.get_db)):
    db_movie = crud.get_movie(db=db, movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@router.post("/movies", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    return crud.create_movie(db=db, movie=movie, user_id=current_user.id)

@router.put("/movies/{movie_id}", response_model=schemas.Movie)
def update_movie(movie_id: int, movie: schemas.MovieCreate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    db_movie = crud.update_movie(db=db, movie_id=movie_id, movie=movie, user_id=current_user.id)
    if db_movie is None:
        raise HTTPException(status_code=403, detail="Not authorized to update this movie")
    return db_movie

@router.delete("/movies/{movie_id}", response_model=schemas.Movie)
def delete_movie(movie_id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    db_movie = crud.delete_movie(db=db, movie_id=movie_id, user_id=current_user.id)
    if db_movie is None:
        raise HTTPException(status_code=403, detail="Not authorized to delete this movie")
    return db_movie
