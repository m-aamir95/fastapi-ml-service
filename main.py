from fastapi import FastAPI, HTTPException, Depends, status
from routers import sentiment_router

from database.database_connection import engine, SessionLocal
from database import db_schema_models

from sqlalchemy.orm import session

from pydantic_models import data_models 




# Instantiate the tables via sqlalchemy models 
db_schema_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routes defined in other files
app.include_router(sentiment_router.router)



# General API routes
@app.get("/", tags=["General"])
async def root() -> data_models.UserBase:

    new_user = data_models.UserBase(id = "12345", username="aamir", hashed_password="aamir321")

    return new_user

@app.post("/add_user", tags=["General"])
async def add_user(user : data_models.UserLogin) -> dict:    
    
    print("Received the following user")
    print(user)

    return { "Status" : "All good"}


@app.get("/health", tags=["General"])
async def health_check() -> dict:
    
    return {"Status" : "API is up and running", 
            "Status_Boolean" : True,
            "Model_Status" : "Configured and Loaded",
            "Model_Status_Boolean" : True}