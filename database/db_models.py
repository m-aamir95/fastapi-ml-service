from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database_connection import Base


class User(Base):

    __tablename__ = "User"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(32), unique=True, index=True)
    hashed_password = Column(String(256))

    # Establish a bi-directional relationship with SentimentText
    sentiment_texts = relationship("SentimentText", back_populates="writter_by")


class SentimentText(Base):

    __tablename__ = "SentimentText"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("User.id"))
    text_id = Column(String(32))
    text = Column(String(1000))
    sentiment_bag = Column(String(50))
    reviewed = Column(Boolean, default=False)

    # Establish a bi-directional relationship with User
    written_by = relationship("User", back_populates="sentiment_texts")
