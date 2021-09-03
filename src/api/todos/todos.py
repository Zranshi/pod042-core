from fastapi import APIRouter
from src.orm.todo import Todo
from src.schema.todo import TodoSchema
from src.utils.db import db

router = APIRouter()


@router.get("")
async def get_todos() -> dict:
    return {
        "msg": "Todo object search successful.",
        "data": db.sess.query(Todo).all(),
    }


@router.post("")
async def add_todo(schema: TodoSchema) -> dict:
    new_todo = schema.new_obj(Todo())
    db.sess.add(new_todo)
    db.sess.flush()
    return {"msg": f"Todo object: id={new_todo.id} create success."}


@router.put("")
async def update_todo(schema: TodoSchema) -> dict:
    todo = db.sess.query(Todo).filter_by(id=schema.id).first()
    if todo:
        todo = schema.new_obj(todo, {"id"})
        db.sess.flush()
        return {"msg": f"Todo object: id={schema.id} has been updated."}
    return {"msg": f"Todo object: id={schema.id} no found."}


@router.delete("")
async def delete_todo(id: int) -> dict:
    todo = db.sess.query(Todo).filter_by(id=id).first()
    if todo:
        db.sess.delete(todo)
        db.sess.commit()
        return {"data": f"Todo with id={id} has been removed."}

    return {"data": f"Todo with id={id} not found."}
