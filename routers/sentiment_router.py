from fastapi import APIRouter

router = APIRouter()


@router.get("/get_sentiment_score", tags=["AI_Model"])
async def get_sentiment_score():
    return {
        "Positive_Sentiment_Score" : 0.55,
        "Negative_Sentiment_Score" : 0.44
    }
