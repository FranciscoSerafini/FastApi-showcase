from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr, EmailStr

app = FastAPI()

class User(BaseModel):
    id: int
    name: constr(min_length=1, max_length=50) # type: ignore
    email: EmailStr
    age: int
    
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

#implementamos validaciones en las rutas de API
#implementamos HTTPException -> lo utilizamos para manejar casos en que los datos no cumplen con las validaciones
@app.post('/users')
def create_users(user:User):
    #comprobacion de id
    if user.id in database:
        raise HTTPException(status_code=404, detail="El usuario que quiere añadir ya existe")
    if user.email in database:
        raise HTTPException(status_code=404, detail="El email que quiere ingresar ya existe")
    #simulamos la creacion de un usuario
    database[user.id] = user
    return {'message':'se creo el usuario correctamente'}

@app.get('/users/{user_id}')
def get_id_users(user_id:int = None):
    user = database.get(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="El id del usuario no existe")

@app.put('/users/{user_id}')
def update_user(user_id:int, user:User):
    if user_id in database:
        database[user_id] = user
        return{'message':'el usuario fue actualizado correctamente'}
    raise HTTPException(status_code=404, detail="El usuario no fue encontrado")

@app.delete('/users/{user_id}')
def delete_user(user_id:int, user:User):
    if user_id in database:
        del database[user_id]
        return{'message':'el usuario se elimino correctamente'}
    raise HTTPException(status_code=404, detail='El usuario no fue encontrado')