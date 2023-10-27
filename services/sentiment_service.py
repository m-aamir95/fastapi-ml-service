from transformers import pipeline

from fastapi import HTTPException

from abc import ABC, abstractmethod

from pydantic_models import data_models

from services.user_service import UserService

#Sentiment Service interface
class SentimentService(ABC):

    @abstractmethod
    def get_text_analysis(self, user_service : UserService) -> dict:
        pass





# HuggingFace implementation
class SentimentServiceHuggingFace(SentimentService):

    def __init__(self):

        #TODO, By default, the pipeline object will choose a sentiment analysis model itself
        #We can configure it in the arguments
        self.sentiment_analysis_pipeline = pipeline("sentiment-analysis")

    
    def get_text_analysis(self, req : data_models.SentimentTextAnalysisWebRequest, user_service : UserService) -> dict:

        # Authenticate the user
        authenticated_user = user_service.verify_user_login(req.username, req.hashed_password)
        if authenticated_user is None:
            raise HTTPException(status_code=400, detail="Invalid username or password")
        
        print("------ Printing the authenticated user ---------")
        print(authenticated_user)
        for u in authenticated_user:
            print(u)
        print("------------------------------------------------")


        return {"model_resp" : self.sentiment_analysis_pipeline(req.text)}
