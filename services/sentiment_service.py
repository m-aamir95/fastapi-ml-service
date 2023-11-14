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

    def __init__(self, custom_db_session : Session):

        #TODO, By default, the pipeline object will choose a sentiment analysis model itself
        #We can configure it in the arguments
        self.sentiment_analysis_pipeline = pipeline("text-classification", model="m-aamir95/finetuning-sentiment-classification-model-with-amazon-appliances-data")
        self.custom_db_session : Session = custom_db_session

    
    def get_text_analysis(self, req : data_models.SentimentTextAnalysisWebRequest, user_service : UserService) -> dict:

        # Authenticate the user
        authenticated_user = user_service.verify_user_login(req.username, req.hashed_password)
        if authenticated_user is None:
            raise HTTPException(status_code=400, detail="Invalid username or password")
        

        text_analysis_model_resp = self.sentiment_analysis_pipeline(req.text)

        # The model outputs LABEL_1 and LABEL_0 for LABEL_1 as a Good Positive review and LABEL_0 as a negative one
        # We are going to chage LABEL_1 -> Positive and LABEL_0 to Negative before pushing things to the DB
        # And returning the Resp to user
        if text_analysis_model_resp[0]["label"] == "LABEL_1":
            text_analysis_model_resp[0]["label"] = "Positive"
        else:
            text_analysis_model_resp[0]["label"] = "Negative"

        # Insert the record into the database
        sentiment_record = db_schema_models.SentimentText(user_id=authenticated_user.id,
                                                          text=req.text,
                                                          sentiment_bag= json.dumps(text_analysis_model_resp[0]),
                                                          )

        with self.custom_db_session as db_session:

             try:
                db_session.add(sentiment_record)
                db_session.commit()
                db_session.refresh(sentiment_record)

            except PendingRollbackError as rollback_error:
                # Roll back the transaction and handle the error
                db_session.rollback()
                print(f"PendingRollbackError: {rollback_error}")
                # Additional error handling if needed
            except Exception as e:
                # Roll back the transaction and handle other exceptions
                db_session.rollback()
                print(f"Error: {e}")
                # Additional error handling if needed
            finally:
                # The session is automatically closed when the block exits
                pass
    

        return {"model_resp" : text_analysis_model_resp}
