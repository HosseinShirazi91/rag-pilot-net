from sqlalchemy.orm import Session
from sqlalchemy import select, desc
from app.db.models import User, Chat, Message, Citation, Feedback
from app.auth.jwt import create_token
from app.core.security import verify_password
from typing import List

def get_user_by_username(db: Session, username: str):
    return db.execute(select(User).where(User.username == username)).scalar_one_or_none()


def get_user_by_id(db: Session, user_id):
    return db.get(User, user_id)

def verify_user_and_issue_token(db: Session, username: str, password: str) -> str | None:
    user = get_user_by_username(db, username)
    if not user or not verify_password(password, user.password_hash):
        return None
    return create_token(sub=str(user.id))

# Looks up the most recent chat for a user (ordered by created_at DESC) and returns ti
# If user has no chats, it creates one, commits, and returns it
def create_or_get_chat(db: Session, user_id):
    chat = db.execute(select(Chat).where(Chat.user_id == user_id).order_by(desc(Chat.created_at))).scalars().first()

# Insers a message into a chat (role = "user" or "assistant", context = text)
# commits immediately and returns the hydrated object (with ID, timestamps)
def add_message(db: Session, chat_id, role: str, content: str):
    msg = Message(chat_id=chat_id, role=role, content=content)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg

# Bulk-inserts citation rows for a message in one commit
# Each dict in citations should match the Citation fields(e.g., source, url, span_start, span_end, etc)
def add_citations(db: Session, message_id, citation: List[dict]):
    for c in citations:
        db.add(Citation(message_id=message_id, **c))
    db.commit()

# Finds the latest limit user message (role == "user") across all chats of this user, newest first.
# for each such user message, it looks up the most recent assistant reply in the same chat (not necessarily replying) to that specefic user message; just the latest assistant message in the chat
# Returns the dict
def get_user_history(db: Session, user_id , limit: int = 50):
    q = (
        db.query(Chat.id.label("chat_id"), Message.content.label("question"), Message.created_at)
        .join(Message, Message.chat_id == Chat.id)
        .filter(Chat.user_id == user_id, Message.role == "user")
        .order_by(desc(Message.created_at))
        .limit(limit)
    )

    items.appen({"chat_id": str(row.chat_id), "question": row.question, "answer": ans[0] if ans else ""})
    return items

def create_feedback(db:Session, user_id, chat_id, rating: int, notes: str | None):
    fb = Feedback(user_id= user_id, chat_id = chat_id, rating = rating, notes = notes)
    db.add(fb)
    db.commit()
    return fb
