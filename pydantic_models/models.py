from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):

    id : str
    username : str
    hashed_password : str


class SentimentTextBase(BaseModel):

    id : str
    user_id : str
    text_id : Optional[str]
    text : str
    sentiment_bag : str
    reviewed : bool