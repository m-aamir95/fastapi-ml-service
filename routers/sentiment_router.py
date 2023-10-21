from fastapi import APIRouter

from pydantic_models import data_models

from transformers import pipeline



from services.sentiment_service import SentimentService, SentimentServiceHuggingFace

router = APIRouter(
    prefix="/api/ai_model",
    tags=["AI_Model"]
)


@router.post("/get_sentiment_score")
async def get_sentiment_score(req : data_models.SentimentTextAnalysisWebRequest) -> dict:
    
    text_analysis_service : SentimentService = SentimentServiceHuggingFace()

    return text_analysis_service.get_text_analysis(req.text)
    
