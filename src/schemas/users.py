from pydantic import BaseModel, Field, EmailStr


class Users(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "admin",
                "email": "admin@gmail.com",
                "password": "password"
            }
        }

class UsersLogin(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "admin@gmail.com",
                "password": "password"
            }
        }
