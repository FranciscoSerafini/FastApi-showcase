from fastapi import FastAPI, HTTPException, Query, Path
from pydantic import BaseModel, constr, EmailStr, Field
from typing import List

app = FastAPI(
    title='CRUD API',
    description='API de prueba',
    version='0.0.0'
)

class User(BaseModel):
    id: int = Field(description='Id del usuario', example=1)
    name: constr(min_length=1, max_length=50) = Field(description='Nombre del usuario', example='Fran Serafini')
    email: EmailStr = Field(description='Email del usuario', example='francisco@gmail.com')
    age: int = Field(description='Edad del usuario', example=25)

class createUserResponse(BaseModel):
    message: str = Field(
        description="Éxito",
        example='Usuario creado correctamente'
    )

class UpdateUserSuccessfulResponse(BaseModel):
    message: str = Field(
        description="Mensaje de éxito en la operación",
        example="Usuario actualizado correctamente"
    )

class DeleteUserSuccessfulResponse(BaseModel):
    message: str = Field(
        description="Mensaje de éxito en la operación",
        example="Usuario eliminado correctamente"
    )

database = {
    0: User(id=0, name="John", email="john@gmail.com", age=20),
    1: User(id=1, name="Mike", email="mike@gmail.com", age=20),
    2: User(id=2, name="Sarah", email="sarah@gmail.com", age=25),
    3: User(id=3, name="Emma", email="emma@gmail.com", age=22),
    4: User(id=4, name="David", email="david@gmail.com", age=28),
    5: User(id=5, name="Sophia", email="sophia@gmail.com", age=27),
    6: User(id=6, name="James", email="james@gmail.com", age=35),
    7: User(id=7, name="Olivia", email="olivia@gmail.com", age=24),
    8: User(id=8, name="Lucas", email="lucas@gmail.com", age=31),
    9: User(id=9, name="Mia", email="mia@gmail.com", age=29)
}

@app.get('/', tags=['Health Check'], description='Ruta raíz para comprobar que la API está activa')
def root():
    return {"message": "La API está funcionando"}

@app.post('/users', tags=['Users'], description='Ruta para crear un nuevo usuario', response_model=createUserResponse, status_code=201)
def create_user(user: User):
    if user.id in database:
        raise HTTPException(status_code=400, detail='El usuario ya existe')
    
    for existing_user in database.values():
        if existing_user.email == user.email:
            raise HTTPException(status_code=400, detail="El usuario con este email ya existe")
    
    database[user.id] = user
    return {"message": "Usuario registrado"}

@app.get('/users', tags=['Users'], response_model=List[User])
def get_all_users(
    name: str = Query(description="Nombre del usuario", example='Fran', default=None),
    email: str = Query(description='Email del usuario', example='francisco@gmail.com', default=None),
    age: int = Query(description='Edad del usuario', example=24, default=None)
) -> List[User]:
    filter_users = []
    for user in database.values():
        if (name is None or user.name == name) and \
           (email is None or user.email == email) and \
           (age is None or user.age == age):
            filter_users.append(user)
    return filter_users

@app.get('/users/{user_id}', tags=['Users'], response_model=User)
def get_id_user(user_id: int = Path(..., description='El id de usuario que quiere obtener', example=1)) -> User:
    user = database.get(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail='Usuario no encontrado')

@app.put('/users/{user_id}', tags=['Users'], response_model=UpdateUserSuccessfulResponse)
def update_user(user: User, user_id: int = Path(..., description='El usuario que quiere actualizar', example=1)) -> UpdateUserSuccessfulResponse:
    if user_id in database:
        database[user_id] = user
        return {'message': 'Usuario actualizado correctamente'}
    raise HTTPException(status_code=404, detail='Usuario no encontrado')

@app.delete("/users/{user_id}", tags=["Users"], response_model=DeleteUserSuccessfulResponse)
def delete_user(user_id: int = Path(..., description="El id del usuario que queremos eliminar", example=1)) -> DeleteUserSuccessfulResponse:
    if user_id in database:
        del database[user_id]
        return {"message": "Usuario eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
