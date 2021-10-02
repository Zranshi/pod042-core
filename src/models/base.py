from datetime import datetime
from typing import Dict

import orm
from fastapi import APIRouter
from src.utils.db_conn import database_connection

all_models = orm.ModelRegistry(database=database_connection())


class BaseModel(orm.Model):
    basic = {
        "id": orm.Integer(primary_key=True),
        "update_time": orm.DateTime(default=datetime.now()),
        "create_time": orm.DateTime(default=datetime.now()),
        "delete_time": orm.DateTime(allow_null=True),
    }

    @classmethod
    def bind_CRUD(cls, r: APIRouter, SchemaClass):
        cls.bind_lst(r)
        cls.bind_search(r)
        cls.bind_create(r, SchemaClass)
        cls.bind_update(r, SchemaClass)
        cls.bind_delete(r)

    @classmethod
    def bind_lst(cls, r: APIRouter):
        @r.get("/list")
        async def lst() -> Dict:
            return {
                "msg": f"{cls.__name__} list search successful.",
                "data": await cls.objects.filter(delete_time=None).all(),
            }

    @classmethod
    def bind_search(cls, r: APIRouter):
        @r.get("")
        async def search(id: int) -> Dict:
            obj = await cls.objects.filter(id=id, delete_time=None).all()
            return {
                "msg": f"{cls.__name__} object search successful."
                if obj
                else f"{cls.__name__} object no found.",
                "data": obj,
            }

    @classmethod
    def bind_create(cls, r: APIRouter, SchemaClass):
        @r.post("")
        async def create(schema: SchemaClass) -> Dict:
            await cls.objects.create(**schema.dict())
            return {"msg": f"{cls.__name__} object has created successful."}

    @classmethod
    def bind_update(cls, r: APIRouter, SchemaClass):
        @r.put("")
        async def update(id: int, schema: SchemaClass) -> Dict:
            obj = await cls.objects.filter(id=id, delete_time=None).first()
            if obj:
                await obj.update(**schema.dict(), update_time=datetime.now())
                return {
                    "msg": f"{cls.__name__} object has updated successfully"
                }
            return {"msg": f"{cls.__name__} object no found."}

    @classmethod
    def bind_delete(cls, r: APIRouter):
        @r.delete("")
        async def delete(id: int) -> Dict:
            obj = await cls.objects.filter(id=id, delete_time=None).first()
            if obj:
                await obj.update(delete_time=datetime.now())
                return {
                    "msg": f"{cls.__name__} object has deleted successfully"
                }
            return {"msg": f"{cls.__name__} object no found."}
