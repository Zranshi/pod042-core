from fastapi import APIRouter
from pydantic import BaseModel
from src.models.user import User

router = APIRouter()


class LoginSchema(BaseModel):
    email: str = ""
    password: str = ""


class RegisterSchema(BaseModel):
    email: str = ""
    name: str = ""
    password: str = "123456"


@router.post("/login")
async def login(schema: LoginSchema):
    user = await User.objects.filter(
        delete_time=None,
        email=schema.email,
        password=schema.password,
    ).first()
    return {
        "msg": "login successful!" if user else "login failed!",
        "data": user,
    }


@router.post("/registry")
async def register(schema: RegisterSchema):
    is_exists = await User.objects.filter(
        delete_time=None,
        email=schema.email,
    ).exists()
    if is_exists:
        return {
            "msg": "email has already been registered!",
            "data": None,
        }

    user = await User.objects.create(
        name=schema.name,
        email=schema.email,
        password=schema.password,
    )
    return {
        "msg": "register successful!",
        "data": user,
    }


@router.put("/find_back")
async def find_back(schema: LoginSchema):
    is_exists = await User.objects.filter(
        delete_time=None,
        email=schema.email,
    ).exists()
    if is_exists:
        await User.objects.update(password=schema.password)
        return {"msg": "password has been changed."}
    return {"msg": "Could not find the email."}
