from models import *

response = AnswerResponse(
    answer = "Test Answer",
    sources = ["file1", "file2"],
    latency = 0.3
)

print(response)