from typing import List
from fastapi import APIRouter, Depends, status, Response
from .. import database, schemas, oauth2
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
def create(request: schemas.Blog, db : Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db : Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db : Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db : Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id, db : Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)
