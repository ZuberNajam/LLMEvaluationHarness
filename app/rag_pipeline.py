from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
KB_PATH = BASE_DIR / "data" / "knowledge_base.txt"
#KB_PATH = Path("app/data/knowledge_base.txt")

def load_knowledge_base():
    with open(KB_PATH, "r", encoding="utf-8") as f:
        return f.read()

import re


def build_context(question):

    kb = load_knowledge_base()

    chunks = [
        chunk.strip()
        for chunk in kb.split("\n")
        if chunk.strip()
    ]

    # normalize question
    question_words = re.findall(
        r"\w+",
        question.lower()
    )

    relevant_chunks = []

    for chunk in chunks:

        chunk_lower = chunk.lower()

        if any(
            word in chunk_lower
            for word in question_words
        ):
            relevant_chunks.append(chunk)

    # fallback
    if not relevant_chunks:

        context = "NO_RELEVANT_CONTEXT_FOUND"

    else:

        context = "\n".join(relevant_chunks)

    print("Retrieved Context:", context)

    prompt = f"""
You are a helpful assistant.

Knowledge Base:
{context}

Question:
{question}

IMPORTANT:
Only answer using the provided context.
If the answer is not explicitly present in the context,
do not guess or use outside knowledge. Say:
"I could not find the answer in the provided context."
"""

    return {
        "prompt": prompt,
        "context": context,
        "sources": ["knowledge_base.txt"]
    }

# def build_context(question):
#     kb = load_knowledge_base()
#     chunks = kb.split("\n")
#     relevant_chunks = []
#     for chunk in chunks:
#         if question.lower() in chunk.lower() or any(word.lower() in chunk.lower()
#             for word in question.split()):
#             relevant_chunks.append(chunk)
#
#     if not relevant_chunks:
#         relevant_chunks = chunks[:2]
#
#     context = "\n".join(relevant_chunks)
#     print("Retrieved context:", context)
#
#     prompt = f"""
# You are a helpful project assistant.
#
# Knowledge Base:
# {context}
#
# Question:
# {question}
#
# Answer only using the provided context.
# """
#     return {
#         "prompt": prompt,
#         "context": context,
#         "sources": ["knowledge_base.txt"],
#     }
