from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str
    description: str

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

    class RatingBase(BaseModel):
      score: float

    class RatingCreate(RatingBase):
      movie_id: int

    class Rating(RatingBase):
      id: int
    movie_id: int
    user_id: int

    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    text: str
    parent_id: int | None = None

class CommentCreate(CommentBase):
    movie_id: int

class Comment(CommentBase):
    id: int
    movie_id: int
    user_id: int

    class Config:
        orm_mode = True
   
