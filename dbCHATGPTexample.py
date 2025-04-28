# models.py
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class ChatRoom(Base):
    __tablename__ = "chat_rooms"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    messages = relationship("ChatMessage", back_populates="room")

class ChatMessage(Base):
    __tablename__ = "chat_messages"
    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(String, ForeignKey("chat_rooms.id"))
    sender = Column(String)
    text = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

    room = relationship("ChatRoom", back_populates="messages")

