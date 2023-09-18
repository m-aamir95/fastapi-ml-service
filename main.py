from fastapi import FastAPI

from services import sentiment_router

app = FastAPI()

app.include_router(sentiment_router.router)

@app.get("/", tags=["General"])
async def root() -> dict:
    return {"message" : "Hello World, Hello FastAPI"}

@app.get("/health", tags=["General"])
async def health_check() -> dict:
    return {"Status" : "API is up and running", 
            "Model_Status" : "Configured and Loaded"}