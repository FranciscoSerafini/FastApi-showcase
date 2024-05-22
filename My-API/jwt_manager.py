from jwt import encode
from jwt import decode

#creamos la funcion para el token de seguridad

def create_token(data:dict):
    token:str=encode(payload=data,key="mykey",algorithm="HS256") #contenido que le vamos a pasar al token
    return token

def validar_token(token:str) -> dict:
    data:dict=decode(token,key="mykey", algorithms=['HS256'])
    return data