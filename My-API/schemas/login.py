from pydantic import BaseModel

# Clase información del usuario
class User(BaseModel):
    email: str
    password: str

user_data = {"email": "admin@gmail.com", "password": "admin"}
user_instance = User(**user_data)