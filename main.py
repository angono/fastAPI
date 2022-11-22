from fastapi import FastAPI 
from pydantic import BaseModel
from typing import Optional, Union

app = FastAPI()

fakedb = []

class Course(BaseModel):
    id: int
    name: str
    price: float
    available: Optional[bool] = None

@app.get('/')
async def get_course():
    return fakedb

@app.get('/courses/{course_id}')
async def get_a_course(course_id:int):
    course = course_id - 1
    return fakedb[course]

@app.post('/courses')
async def add_course(course:Course):
    fakedb.append(course.dict())
    return fakedb[-1]

@app.put('/courses/{course_id}')
async def update_course(course_id:int, course:Course):
    obj = course_id - 1
    fakedb[obj].update(course.dict())
    return fakedb

@app.delete('/courses/{course_id}')
async def delete_course(course_id:int):
    fakedb.pop(course_id-1)
    return {'Task': 'Deletion successful'}

