from fastapi import APIRouter
from src.models.todo import Todo
from src.schema.todo import TodoSchema

router = APIRouter()
Todo.bind_CRUD(router, TodoSchema)
