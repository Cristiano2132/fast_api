from uuid import UUID, uuid4
from typing import List
from fastapi import FastAPI
from models import Gender, Role, User

app = FastAPI()

db: List[User] =[
    User(id=uuid4(), 
    first_name='Joana', 
    last_name='python',
    gender=Gender.female,
    roles=[Role.student]
    ),
    User(id=uuid4(), 
    first_name='Joao', 
    last_name='Peter',
    gender=Gender.male,
    roles=[Role.admin, Role.user]
    )
]

@app.get("/")
def root():
    '''Docstrings'''
    return {'Hello': 'World'}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_users(user: User):
    db.append(user)
    return {'id': user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_users(user_id: UUID):
    for user in db:
        if user.id==user_id:
            db.remove(user)
            return 