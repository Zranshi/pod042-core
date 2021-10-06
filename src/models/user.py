import orm
from fastapi import APIRouter
from src.models.base import BaseModel, BaseSchema, all_models


class User(BaseModel):
    tablename = "users"
    registry = all_models
    fields = {
        "name": orm.String(max_length=100, default=""),
        "password": orm.String(max_length=100, default="123456"),
        "email": orm.String(max_length=100, default="", unique=True),
        **BaseModel.basic,
    }


class UserSchema(BaseSchema):
    name: str = ""
    password: str = "123456"
    email: str = ""


router = User.bind_CRUD(APIRouter(), UserSchema)
