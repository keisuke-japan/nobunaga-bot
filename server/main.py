import os
import sys

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# /src をパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from server.nobunaga_agent import ask_question

app = FastAPI()

API_KEY = "your_secret_api_key"

origins = ["http://localhost:5173"]  # Frontendのオリジンをここに書く
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message(BaseModel):
    text: str = Field(title="Request message to LLM.", max_length=1000)


class LLMResponse(BaseModel):
    answer: str


@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}


@app.post("/llm")
async def run_llm(message: Message, api_key: str) -> LLMResponse:
    answer = ask_question(message.text)
    with open("server/apikey.txt") as file:
        id_set = {line.strip() for line in file}

    if api_key not in id_set:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    llm_response = LLMResponse(answer=answer)
    return llm_response
