from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"message" : "Hello World, Hello FastAPI"}

@app.get("/health")
async def health_check() -> dict:
    return {"Status" : "API is up and running", 
            "Model_Status" : "Configured and Loaded"}