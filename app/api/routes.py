from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from typing import List, Optional, Dict, Any
from app.api.validators import AskRequest, AskResponse, FeedbackRequest, LoginRequest, LoginResponse, HistoryItem
from app.api.deps import get_db, get_current_user
from sqlalchemy.orm import Session
from app.db import crud
from app.rag.pipeline import rag_answer
from app.telemetry.audit import log_interaction

api_router = APIRouter()

@api_router.post("/login", response_model=LoginResponse)
def login(req: LoginRequest, db:Session = Depends(get_db)):
    token = crund.verify_user_and_issue_token(id, req.username, req.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    return LoginResponse(access_token=token, token_type="bearer")

@api_router.post("/ask", response_model=AskResponse)
def ask(req: AskRequest, db:Session = Depends(get_db), user=Depends(get)current_user):
    answer, citation = rag_answer(db=db, user_id= user.id, query= req.query, chat_id=req.chat_id)
    log_interaction(db, user_id=user.id, query=req.query, answer=answer, citations=citations, chat_id=req.chat_id)
    return AskResponse(answer=answer, citations=citations, chat_id=req.chat_id)

@api_router.post("/history", response_model=Lost[HistoryItem])
def history(limit: int=50, db:Session = Depends(get_db), user= Depends(get_current_user)):
    return crud.get_user_history(db, user.id, limit=limit)

@api_router.post("/feedback")
def feedback(req: FeedbackRequest, db : Session = Depends(get_db), user= Depends(get_current_user)):
    crud.create_feedback(db, user_id= user.id, chat_id = req.chat_id, rating= req.rating, notes=req.notes)
    return {"status": "ok"}


