from fastapi import APIRouter, Depends

from pydantic_models import data_models


from services.sentiment_service import SentimentService, SentimentServiceHuggingFace
from services.user_service import UserService, SqlAlchemyUserService

from database.database_connection import CustomizedDBSession



#region Dependency Injection for services
# TODO, maybe the GetSentimentService and GetUserService class can be used as one
# TODO, inject the actual service via the constructor, this way we can use the same
# TODO, class for both the services
class GetSentimentService():

    def __init__(self):

        self.text_analysis_service : SentimentService = SentimentServiceHuggingFace()

    def __call__(self) -> SentimentService:
        
        return self.text_analysis_service

sentimentService_dependency : SentimentService = GetSentimentService()

class GetUserService():

    def __init__(self):
        self.user_service : UserService = SqlAlchemyUserService(CustomizedDBSession)
    
    def __call__(self) -> UserService:
        return self.user_service

userService_dependency = GetUserService()
#endregion

router = APIRouter(
    prefix="/api/ai_model",
    tags=["AI_Model"]
)


@router.post("/get_sentiment_score")
async def get_sentiment_score(req : data_models.SentimentTextAnalysisWebRequest,
                              text_analysis_service = Depends(sentimentService_dependency),
                              user_service = Depends(userService_dependency)) -> dict:
    

    return text_analysis_service.get_text_analysis(req, user_service)
    
