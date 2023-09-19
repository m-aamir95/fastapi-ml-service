from fastapi import APIRouter

router = APIRouter(
    prefix="/api/ai_model",
    tags=["AI_Model"]
)


@router.get("/get_sentiment_score")
async def get_sentiment_score():
    return {
        "Positive_Sentiment_Score" : 0.55,
        "Negative_Sentiment_Score" : 0.44
    }
