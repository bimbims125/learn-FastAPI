from pydantic import BaseModel
from datetime import datetime

class PostinganModel(BaseModel):
    id: int
    author: str
    post: str
    created_at: datetime