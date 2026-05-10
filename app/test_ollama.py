from http.client import responses
from ollama_client import OllamaClient

client =OllamaClient()

response = client.generate("What is Python?")
print(response)