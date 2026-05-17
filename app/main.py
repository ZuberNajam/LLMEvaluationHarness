import time

from fastapi import FastAPI
from evaluator import evaluate_hallucination, hallucination_check

from models import (
    QuestionRequest,
    AnswerResponse
)

from rag_pipeline import build_context
# from app.ollama_client import OllamaClient
from retrieval_metrics import (
    evaluate_context_recall, evaluate_context_precision
)

from embedding_metrics import (
    semantic_similarity
)


app = FastAPI()

# # client = OllamaClient()

from openai import OpenAI
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# response = client.responses.create(
#     model="gpt-oss:20b",
#     input="Write a short bedtime story about a unicorn."
# )

# print(response.output_text)

@app.get("/models")
async def get_models():
    models = client.models.list()
    return models

@app.post("/answer", response_model= AnswerResponse)
async def answer(req: QuestionRequest):
    start_time = time.time()

    rag = build_context(req.question)

    llm_output = client.responses.create(
        model="gpt-oss:20b",
        input=rag["prompt"]
    )

    precision = evaluate_context_precision(
        req.question,
        rag["context"]
    )

    recall = evaluate_context_recall(
        req.question,
        rag["context"],
        llm_output.output_text
    )

    hallucination_result = evaluate_hallucination(
        rag["prompt"],
        llm_output.output_text
    )

    print("Precision:", precision)
    print("Recall:", recall)

    similarity_score = semantic_similarity(
        llm_output.output_text,
        rag["context"]
    )

    print("Similarity Score:", similarity_score)

    evaluation_data = {

        "question": req.question,

        "answer": llm_output.output_text,

        "hallucination_check":
            hallucination_check,

        "context_precision":
            precision,

        "context_recall":
            recall,

        "answer_similarity":
            similarity_score,

        "latency":
            time.time() - start_time
    }

    return AnswerResponse(
        answer=llm_output.output_text,
        sources=rag["sources"],
        #added context for LLM-as-a-judge
        context=rag["prompt"],
        hallucination_check=hallucination_result,
        context_precision=precision,
        context_recall=recall,
        latency=time.time() - start_time,
        answer_similarity = similarity_score
    )
