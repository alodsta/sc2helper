from pydantic import BaseModel


class SCObject(BaseModel):
    id: int | None
