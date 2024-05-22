from fastapi import FastAPI, HTTPException
from fastapi.responses import  JSONResponse
from pydantic import BaseModel
from jwt_manager import create_token
from fastapi import APIRouter
from schemas.login import User


movie_login = APIRouter()

# Ruta para loguearse
@movie_login.post('/login', tags=['autenticación'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=200, content={"token": token})
    raise HTTPException(status_code=401, detail="Credenciales inválidas")