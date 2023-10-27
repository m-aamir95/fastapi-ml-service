from transformers import pipeline

from fastapi import HTTPException

from sqlalchemy.orm import Session

from abc import ABC, abstractmethod

from pydantic_models import data_models

from services.user_service import UserService

from database import db_schema_models

import json

#Sentiment Service interface
class SentimentService(ABC):

    @abstractmethod
    def get_text_analysis(self, user_service : UserService) -> dict:
        pass





# HuggingFace implementation
class SentimentServiceHuggingFace(SentimentService):

    def __init__(self, db_session : Session):

        #TODO, By default, the pipeline object will choose a sentiment analysis model itself
        #We can configure it in the arguments
        self.sentiment_analysis_pipeline = pipeline("sentiment-analysis")
        self.db_session : Session = db_session

    
    def get_text_analysis(self, req : data_models.SentimentTextAnalysisWebRequest, user_service : UserService) -> dict:

        # Authenticate the user
        authenticated_user = user_service.verify_user_login(req.username, req.hashed_password)
        if authenticated_user is None:
            raise HTTPException(status_code=400, detail="Invalid username or password")
        

        text_analysis_model_resp = self.sentiment_analysis_pipeline(req.text)

        # Insert the record into the database
        sentiment_record = db_schema_models.SentimentText(user_id=authenticated_user.id,
                                                          text=req.text,
                                                          sentiment_bag= json.dumps(text_analysis_model_resp[0]),
                                                          )
        
        self.db_session.add(sentiment_record)
        self.db_session.commit()
        self.db_session.refresh(sentiment_record)
        

        return {"model_resp" : text_analysis_model_resp}
