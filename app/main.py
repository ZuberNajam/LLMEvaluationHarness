import time

from fastapi import FastAPI

from app.models import (
    QuestionRequest,
    AnswerResponse
)

from rag_pipeline import build_context
from ollama_client import OllamaClient

app = FastAPI()

client = OllamaClient()

@app.post("/answer", response_model= AnswerResponse)
async def answer(req: QuestionRequest):
    start_time = time.time()

    rag = build_context(req.question)

    llm_output = client.generate(rag["prompt"])

    return AnswerResponse(
        answer=llm_output["response"],
        sources=rag["sources"],
        latency=time.time() - start_time
    )
