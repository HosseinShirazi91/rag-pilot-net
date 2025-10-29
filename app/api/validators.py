from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class LoginRequest(BaseModel):
    username    : str
    password    : str

class LoginResponse(BaseModel):
    access_toke : str
    token_type  : str = "bearer"

class Citation(BaseModel):
    doc_id  : str
    path    : str
    page    : int | None = None
    score   : float | None = None
    snippet : str | None = None

class AskRequest(BaseModel):
    query   : str = Field(min_length=2)
    chat_id : str | None = None

class AskResponse(BaseModel):
    answer  : str
    citation: List[Citation]
    chat_id : str | None = None

class FeedbackRequest(BaseModel):
    chat_id : str
    rating  : int = Field(ge=1, le=5)
    notes   : str | None = None

class HistoryItem(BaseModel):
    chat_id : str
    question: str
    answer  : str
