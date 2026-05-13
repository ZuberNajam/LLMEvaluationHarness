from pydantic import BaseModel
from typing import List

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str
    sources: List[str]
    #Added for LLM-as-a-Judge
    context:str
    hallucination_check: str
    context_precision: float
    context_recall: float
    latency: float