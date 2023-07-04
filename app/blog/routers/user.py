from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import database, schemas
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db : Session = Depends(database.get_db)):
    return user.create(request, db)

@router.get('/', response_model=List[schemas.ShowUser])
def all_user(db : Session = Depends(database.get_db)):
    return user.get_all(db)