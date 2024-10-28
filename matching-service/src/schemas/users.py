from uuid import UUID

from pydantic import BaseModel
from typing_extensions import Optional


class UserCreate(BaseModel):
    avatar: Optional[str] = None
    gender: str
    email: str
    first_name: str
    last_name: str

class UserInDB(BaseModel):
    id: UUID
    first_name: Optional[str] = None
    last_name: Optional[str] = None