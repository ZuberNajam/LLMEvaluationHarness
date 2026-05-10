from rag_pipeline import build_context

result = build_context("What is AWS?")

assert "Amazon Web Services" in result["prompt"]

#print(result["prompt"])
#print(result["sources"])
print("RAG has passed.")