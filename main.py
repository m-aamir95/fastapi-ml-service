from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware

from routers import sentiment_router, user_router

from database.database_connection import engine
from database import db_schema_models

from pydantic_models import data_models 




# Instantiate the tables via sqlalchemy models 
db_schema_models.Base.metadata.create_all(bind=engine)


app = FastAPI()

#Enable CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routes defined in other files
app.include_router(sentiment_router.router)
app.include_router(user_router.router)



# General API routes
@app.get("/", tags=["General"])
async def root() -> dict:
    
    # Redirect to docs message
    return {"msg" : "Please visit /docs"}


@app.get("/health", tags=["General"])
async def health_check() -> dict:
    
    return {"Status" : "API is up and running", 
            "Status_Boolean" : True,
            "Model_Status" : "Configured and Loaded",
            "Model_Status_Boolean" : True}




            