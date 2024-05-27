from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/healthcheck")
async def healthcheck()->dict:
    return {"status": "yes"}