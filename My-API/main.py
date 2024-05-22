from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from jwt_manager import create_token
from config.database import Engine,Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.login import movie_login

app = FastAPI()  # Utilización del módulo

app.title = "My Application FastAPI"  # Cambiamos el título de nuestra app
app.version = "0.0.1"  # La versión

app.add_middleware(ErrorHandler) #añadiomos el middleware a la app, se aplica en toda la app
app.include_router(movie_router)
app.include_router(movie_login)

Base.metadata.create_all(bind=Engine)



movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": 2009,
        "rating": 7.8,
        "category": "anime"
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": 2009,
        "rating": 7.8,
        "category": "Acción"
    }
]

@app.get('/', tags=["Home"])  # Creación de nuestra aplicación y además cambio de los tags
def message():
    return HTMLResponse('<h1>Hello World</h1>')



        
            
    
    