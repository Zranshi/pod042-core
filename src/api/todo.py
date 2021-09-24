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
    todo = Todo()
    todo.__dict__.update(schema.__dict__)
    db.sess.add(todo)
    db.sess.flush()
    return {"msg": f"Todo object: id={todo.id} create success."}


@router.put("")
async def update_todo(id: int, schema: TodoSchema) -> dict:
    q = db.sess.query(Todo).filter_by(id=id)
    ok = q.first()
    if ok:
        q.update(schema.__dict__)
        db.sess.flush()
        return {"msg": f"Todo object: id={id} has been updated."}
    return {"msg": f"Todo object: id={id} no found."}


@router.delete("")
async def delete_todo(id: int) -> dict:
    q = db.sess.query(Todo).filter_by(id=id)
    ok = q.first()
    if ok:
        q.delete()
        db.sess.flush()
        return {"data": f"Todo with id={id} has been removed."}

    return {"data": f"Todo with id={id} not found."}
