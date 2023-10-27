from transformers import pipeline

from abc import ABC, abstractmethod

#Sentiment Service interface
class SentimentService(ABC):

    @abstractmethod
    def get_text_analysis(self) -> dict:
        pass





# HuggingFace implementation
class SentimentServiceHuggingFace(SentimentService):

    def __init__(self):

        #TODO, By default, the pipeline object will choose a sentiment analysis model itself
        #We can configure it in the arguments
        self.sentiment_analysis_pipeline = pipeline("sentiment-analysis")

    
    def get_text_analysis(self, text : str) -> dict:

        # Authenticate the user
        return {"model_resp" : self.sentiment_analysis_pipeline(text)}
