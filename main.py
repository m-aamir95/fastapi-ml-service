from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.responses import RedirectResponse

from routers import sentiment_router, user_router

from database.database_connection import engine
from database import db_schema_models

from pydantic_models import data_models 




# Instantiate the tables via sqlalchemy models 
db_schema_models.Base.metadata.create_all(bind=engine)



app = FastAPI()

# Include routes defined in other files
app.include_router(sentiment_router.router)
app.include_router(user_router.router)



# General API routes
@app.get("/", tags=["General"])
async def root() -> data_models.UserBase:
    
    # Redirect to docs
    return RedirectResponse(f"http://localhost:{app.port}/docs", status_code=400)


@app.get("/health", tags=["General"])
async def health_check() -> dict:
    
    return {"Status" : "API is up and running", 
            "Status_Boolean" : True,
            "Model_Status" : "Configured and Loaded",
            "Model_Status_Boolean" : True}