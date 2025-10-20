from sqlalchemy import Column, String, Integer, JSON, DateTime
from datetime import datetime
from .database import Base

class StringRecord(Base):
    __tablename__ = "strings"

    id = Column(String, primary_key=True, index=True)
    value = Column(String, unique=True, nullable=False)
    length = Column(Integer)
    is_palindrome = Column(Integer)  # store 0/1
    unique_characters = Column(Integer)
    word_count = Column(Integer)
    character_frequency_map = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)