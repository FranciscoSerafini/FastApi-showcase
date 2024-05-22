from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from jwt_manager import create_token, validar_token


# Devuelve las credenciales de usuario
class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validar_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales no válidas")