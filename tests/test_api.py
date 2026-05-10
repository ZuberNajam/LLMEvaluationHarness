from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_answer():

    response = client.post(
        "/answer",
        json={"question": "What is RAG?"}
    )

    assert response.status_code == 200

    data = response.json()

    assert "answer" in data
    assert "sources" in data
    assert "latency" in data