from datetime import datetime
from pydantic import BaseModel, ConfigDict

from src.models import Users, Roles


class UsersDTO(BaseModel):
    id: int
    username: str
    role: Roles


