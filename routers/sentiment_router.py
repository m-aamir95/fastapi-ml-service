from fastapi import APIRouter

from pydantic_models import data_models

from transformers import pipeline

router = APIRouter(
    prefix="/api/ai_model",
    tags=["AI_Model"]
)


@router.post("/get_sentiment_score")
async def get_sentiment_score(req : data_models.SentimentTextAnalysisRequest) -> dict:
   
    
    sentiment_analysis_pipeline = pipeline("sentiment-analysis")

    tr = {"model_resp" : sentiment_analysis_pipeline(req.text)}
    return tr
