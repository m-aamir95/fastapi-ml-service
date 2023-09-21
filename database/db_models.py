from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database_connection import Base


class User(Base):

    __tablename__ = "User"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # Establish a bi-directional relationship with SentimentText
    sentiment_texts = relationship("SentimentText", back_populates="writter_by")


class SentimentText(Base):

    __tablename__ = "SentimentText"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("User.id"))
    text_id = Column(String)
    text = Column(String)
    sentiment_bag = Column(String)
    reviewed = Column(Boolean, default=False)

    # Establish a bi-directional relationship with User
    written_by = relationship("User", back_populates="sentiment_texts")
