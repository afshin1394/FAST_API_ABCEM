from pydantic import BaseModel, Field, field_validator


class CreateUserRequest(BaseModel):
    name: str = Field(..., description="The user's name")
    age: str = Field(..., description="The user's age")
    gender: str = Field(..., description="The user's gender")

    class Config:
        json_schema_extra = {
            "name": {
                "name": "ali"
            },
            "age": {
                "age": "21"
            },
            "gender": {
                "age": "male"
            }
        }
