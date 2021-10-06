from datetime import datetime
from typing import Dict

import orm
from fastapi import APIRouter
from pydantic import BaseModel as AbstractSchemaModel
from src.utils.db_conn import database_connection

all_models = orm.ModelRegistry(database=database_connection())


class BaseSchema(AbstractSchemaModel):
    def dict(self) -> Dict:
        return self.__dict__


class BaseModel(orm.Model):
    basic = {
        "id": orm.Integer(primary_key=True),
        "update_time": orm.DateTime(default=datetime.now()),
        "create_time": orm.DateTime(default=datetime.now()),
        "delete_time": orm.DateTime(allow_null=True),
    }

    @classmethod
    def bind_CRUD(cls, r: APIRouter, SchemaClass) -> APIRouter:
        cls.bind_lst(r)
        cls.bind_search(r)
        cls.bind_create(r, SchemaClass)
        cls.bind_update(r, SchemaClass)
        cls.bind_delete(r)
        return r

    @classmethod
    def bind_lst(cls, r: APIRouter) -> APIRouter:
        @r.get("/list")
        async def lst() -> Dict:
            return {
                "msg": f"{cls.__name__} list search successful.",
                "data": await cls.objects.filter(delete_time=None).all(),
            }

        return r

    @classmethod
    def bind_search(cls, r: APIRouter) -> APIRouter:
        @r.get("")
        async def search(id: int) -> Dict:
            obj = await cls.objects.filter(id=id, delete_time=None).all()
            return {
                "msg": f"{cls.__name__} object search successful."
                if obj
                else f"{cls.__name__} object no found.",
                "data": obj,
            }

        return r

    @classmethod
    def bind_create(cls, r: APIRouter, SchemaClass) -> APIRouter:
        @r.post("")
        async def create(schema: SchemaClass) -> Dict:
            await cls.objects.create(**schema.dict())
            return {"msg": f"{cls.__name__} object has created successful."}

        return r

    @classmethod
    def bind_update(cls, r: APIRouter, SchemaClass) -> APIRouter:
        @r.put("")
        async def update(id: int, schema: SchemaClass) -> Dict:
            obj = await cls.objects.filter(id=id, delete_time=None).first()
            if obj:
                await obj.update(**schema.dict(), update_time=datetime.now())
                return {
                    "msg": f"{cls.__name__} object has updated successfully"
                }
            return {"msg": f"{cls.__name__} object no found."}

        return r

    @classmethod
    def bind_delete(cls, r: APIRouter) -> APIRouter:
        @r.delete("")
        async def delete(id: int) -> Dict:
            obj = await cls.objects.filter(id=id, delete_time=None).first()
            if obj:
                await obj.update(delete_time=datetime.now())
                return {
                    "msg": f"{cls.__name__} object has deleted successfully"
                }
            return {"msg": f"{cls.__name__} object no found."}

        return r
