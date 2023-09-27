from pydantic import BaseModel
from typing import Optional



class UserLogin(BaseModel):

    username :  str
    hashed_password : str

class UserBase(UserLogin):

    id : str

class SentimentTextBase(BaseModel):

    id : str
    user_id : str
    text_id : Optional[str]
    text : str
    sentiment_bag : str
    reviewed : bool