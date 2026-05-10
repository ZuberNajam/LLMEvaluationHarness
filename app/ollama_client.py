import requests

class OllamaClient:
    def __init__(self,
                 model = "llama3",
                 url="http://localhost:11434/api/generate"):
        self.url = url
        self.model = model

    def generate(self, prompt):

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(self.url, json=payload)
        response.raise_for_status()
        data = response.json()

        return {
            "response": data["response"]
        }