import time

from fastapi import FastAPI
from app.evaluator import evaluate_hallucination, hallucination_check

from app.models import (
    QuestionRequest,
    AnswerResponse
)

from app.rag_pipeline import build_context
from app.ollama_client import OllamaClient
from app.retrieval_metrics import (
    evaluate_context_recall, evaluate_context_precision
)

from app.embedding_metrics import (
    semantic_similarity
)


app = FastAPI()

client = OllamaClient()

@app.post("/answer", response_model= AnswerResponse)
async def answer(req: QuestionRequest):
    start_time = time.time()

    rag = build_context(req.question)

    llm_output = client.generate(rag["prompt"])

    precision = evaluate_context_precision(
        req.question,
        rag["context"]
    )

    recall = evaluate_context_recall(
        req.question,
        rag["context"],
        llm_output["response"]
    )

    hallucination_result = evaluate_hallucination(
        rag["prompt"],
        llm_output["response"]
    )

    print("Precision:", precision)
    print("Recall:", recall)

    similarity_score = semantic_similarity(
        llm_output["response"],
        rag["context"]
    )

    print("Similarity Score:", similarity_score)

    evaluation_data = {

        "question": req.question,

        "answer": llm_output["response"],

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
        answer=llm_output["response"],
        sources=rag["sources"],
        #added context for LLM-as-a-judge
        context=rag["prompt"],
        hallucination_check=hallucination_result,
        context_precision=precision,
        context_recall=recall,
        latency=time.time() - start_time,
        answer_similarity = similarity_score
    )



