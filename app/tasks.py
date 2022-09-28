from pydantic import BaseModel, validator
from datetime import date


class Task(BaseModel):
    """task description should be longer than 5 symbols or None"""
    user: int
    name: str
    description: str | None
    deadline: date
    is_completed: bool
