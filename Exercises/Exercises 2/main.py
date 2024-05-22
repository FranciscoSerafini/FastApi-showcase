#Ejercicio 2: Modificar las APIs para recuperar usuarios por query params

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
@app.get('/users/')
def get_all_users(name:str = None, email:str = None, age:int = None):
    #creamos una listra para filtrar los users
    filter_users = []
    
    #recorremos los datos
    for user in database.values():
        if name and email and age:
            if user.name == name and user.email == email and user.age == age:
                filter_users.append(user)
        elif name and email:
            if user.name == name and user.email == email:
                filter_users.append(user)
        elif name and age:
            if user.name == name and user.age == age:
                filter_users.append(user)
        elif email and age:
            if user.email == email and user.age == age:
                filter_users.append(user)
        elif name:
            if user.name == name:
                filter_users.append(user)
        elif email:
            if user.email == email:
                filter_users.append(user)
        elif age:
            if user.age == age:
                filter_users.append(user)
        else:
            filter_users.append(user)
    return filter_users
            
        