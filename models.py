from pydantic import BaseModel
from typing import Optional


class SCObject(BaseModel):
    some_id: Optional[int]
