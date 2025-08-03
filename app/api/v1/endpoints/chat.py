from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/chat")
async def chat(user_message: str, db: Session = Depends(get_db)):
    # Process user message and interact with the database
    # For now, simulate a response
    bot_response = "This is a simulated response."
    
    # Store chat history in the database
    # db.add(ChatHistory(user_message=user_message, bot_response=bot_response))
    # db.commit()
    
    return {"response": bot_response}