from fastapi import APIRouter, Depends

from pydantic_models import data_models

from transformers import pipeline



from services.sentiment_service import SentimentService, SentimentServiceHuggingFace

router = APIRouter(
    prefix="/api/ai_model",
    tags=["AI_Model"]
)



#region Dependency Injection for the Sentiment Analysis Service
class GetSentimentService():

    def __init__(self):

        self.text_analysis_service : SentimentService = SentimentServiceHuggingFace()

    def __call__(self):
        
        return self.text_analysis_service

sentimentService_dependency = GetSentimentService()
#endregion

@router.post("/get_sentiment_score")
async def get_sentiment_score(req : data_models.SentimentTextAnalysisWebRequest,
                              text_analysis_service = Depends(sentimentService_dependency)) -> dict:
    

    return text_analysis_service.get_text_analysis(req.text)
    
