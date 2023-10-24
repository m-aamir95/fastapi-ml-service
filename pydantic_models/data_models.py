from pydantic import BaseModel
from typing import Optional

# Models for interacting with user objects

class UserBase(BaseModel):

    username :  str
    hashed_password : str



# Models For Sentiment Analysis interaction

class SentimentTextBase(BaseModel):

    id : str
    user_id : str
    text_id : Optional[str]
    text : str
    sentiment_bag : str
    reviewed : bool


class SentimentTextAnalysisWebRequest(BaseModel):

    user_id : str
    text : str