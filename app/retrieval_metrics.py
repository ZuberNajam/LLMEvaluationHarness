# from app.ollama_client import OllamaClient

# client = OllamaClient()

from openai import OpenAI
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")


def evaluate_context_precision(question, context):

    prompt = f"""
You are evaluating retrieval quality.

Question:
{question}

Retrieved Context:
{context}

Evaluate how much of the retrieved context
is relevant to answering the question.

Scoring:
1.0 = all retrieved context is useful
0.5 = some useful, some irrelevant
0.0 = mostly irrelevant

Return ONLY a number between 0.0 and 1.0.
"""

    # result = client.generate(prompt)["response"].strip()
    result = client.responses.create(
        model="gpt-oss:20b",
        input=prompt
    ).output_text.strip()

    import re

    match = re.search(r"0(\.\d+)?|1(\.0+)?", result)

    if not match:
        return 0.0

    return float(match.group())

def evaluate_context_recall(question, context, answer):

    prompt = f"""
You are evaluating retrieval completeness.

Question:
{question}

Retrieved Context:
{context}

Generated Answer:
{answer}

Evaluate whether the retrieved context
contained enough information to answer the question fully.

Scoring:
1.0 = all needed information retrieved
0.5 = partially sufficient
0.0 = critical information missing

Return ONLY a number between 0.0 and 1.0.
"""

    # result = client.generate(prompt)["response"].strip()
    result = client.responses.create(
        model="gpt-oss:20b",
        input=prompt
    ).output_text.strip()

    import re

    match = re.search(r"0(\.\d+)?|1(\.0+)?", result)

    if not match:
        return 0.0

    return float(match.group())