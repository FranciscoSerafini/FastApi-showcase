from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id:int
    name:str
    email:str
    age:int
    
database = {
    0: User(id=0, name="John", email="john@gmail.com", age=20),
    1: User(id=1, name="Mike", email="mike@gmail.com", age=30),
    2: User(id=2, name="Sarah", email="sarah@gmail.com", age=25),
    3: User(id=3, name="Emma", email="emma@gmail.com", age=22),
    4: User(id=4, name="David", email="david@gmail.com", age=28),
    5: User(id=5, name="Sophia", email="sophia@gmail.com", age=27),
    6: User(id=6, name="James", email="james@gmail.com", age=35),
    7: User(id=7, name="Olivia", email="olivia@gmail.com", age=24),
    8: User(id=8, name="Lucas", email="lucas@gmail.com", age=31),
    9: User(id=9, name="Mia", email="mia@gmail.com", age=29)
}

#crecion de usuario
@app.post('/users')
def create_users(user:User):
    if user.id in  database:
        return {'error':'el usuario ya existe'}
    database[user.id] = user
    return {'message':'el usuario se creo correctamente'}

#obtencion de los usarios
@app.get('/users')
def getAll_users():
    return list(database.values())

#obtencion de usarios por id
@app.get('/users/{user_id}')
def get_users_id(user_id:int):
    user = database.get(user_id)
    if user:
        return user
    return {'error':'usuario no encontrado'}

#actualizacion de un usuario
@app.put('/user/{user_id}')
def update_user(user_id:int, user:User):
    if user_id in database:
        database[user_id] = user
        return {'message':'usuario actualizado correctamente'}
    return {'error':'usuario no encontrado'}

#eliminacion de un usuario
@app.delete('/user/{user_id}')
def delete_user(user_id:int):
    if user_id in database:
        del database[user_id]
        return {'message':'usuario eleminado correctamente'}
    return {'error':'el usuario no fue encontrado'}