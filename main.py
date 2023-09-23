from fastapi import FastAPI, HTTPException, Depends, status
from routers import sentiment_router

from database.database_connection import engine, SessionLocal
from database.database_connection import db_models

from sqlalchemy.orm import session

# Instantiate the tables via sqlalchemy models 
db_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routes defined in other files
app.include_router(sentiment_router.router)



# General API routes
@app.get("/", tags=["General"])
async def root() -> dict:
    return {"message" : "Hello World, Hello FastAPI"}

@app.get("/health", tags=["General"])
async def health_check() -> dict:
    return {"Status" : "API is up and running", 
            "Model_Status" : "Configured and Loaded"}