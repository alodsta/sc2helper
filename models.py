from pydantic import BaseModel
from typing import Optional


class SCObject(BaseModel):
    _id: Optional[int]
