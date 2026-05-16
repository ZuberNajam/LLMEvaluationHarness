# from app.ollama_client import OllamaClient

# client = OllamaClient()

from openai import OpenAI
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")


def hallucination_check(context, answer):

#     prompt = f"""
# You are an AI evaluator.
#
# Determine whether the answer is fully supported by the provided context.
#
# Context:
# {context}
#
# Answer:
# {answer}
#
# Rules:
# - If answer contains unsupported claims -> hallucination
# - If answer adds external information -> hallucination
# - If fully grounded -> faithful
#
# Respond ONLY with:
# PASS
# or Fail
# """
#     return prompt

    return f"""
    You are a strict hallucination detection system.

    Your job is to classify the answer.

    Context:
    {context}

    Answer:
    {answer}

    Evaluation Rules:
    - If answer is fully supported → PASS
    - If answer includes ANY unsupported claim → FAIL
    - If answer says "not found", "uncertain", or asks for clarification → PASS

    Respond ONLY with:
    PASS
    or
    FAIL
    """

def evaluate_hallucination(context, answer):
    prompt = hallucination_check(context, answer)
    # evaluation = client.generate(prompt)
    evaluation = client.responses.create(
        model="gpt-oss:20b",
        input=prompt
    ).output_text.strip().upper()

    if "PASS" in evaluation:
        return "PASS"
    else:
        return "FAIL"