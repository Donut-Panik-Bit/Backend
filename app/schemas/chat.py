from pydantic import BaseModel


class Chat(BaseModel):
    name: str
    status: str
