from pydantic import BaseModel


class Response(BaseModel):
    status_code: int
    content: str
    headers: dict
    model: object | None = None
