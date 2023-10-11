from datetime import datetime

from pydantic import BaseModel


class Category(BaseModel):
    id: int
    title: str
    created_at: datetime
    updated_at: datetime | None


class Question(BaseModel):
    id: int
    answer: str
    question: str
    created_at: datetime
    updated_at: datetime | None
    category: Category


