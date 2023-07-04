from fastapi import FastAPI
from app.blog import models
from app.blog.database import engine
from app.blog.routers import user, blog, authentication

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog.router)