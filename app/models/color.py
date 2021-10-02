from pydantic import BaseModel


class Color(BaseModel):
    name: str
    red: int
    green: int
    blue: int
