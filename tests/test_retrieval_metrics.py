from app.retrieval_metrics import (
    evaluate_context_precision,
    evaluate_context_recall
)


def test_context_precision():

    question = "What is RAG?"

    context = """
    RAG means Retrieval Augmented Generation.
    AWS is a cloud provider.
    """

    score = evaluate_context_precision(
        question,
        context
    )

    assert isinstance(score, float)

    assert 0.0 <= score <= 1.0

def test_context_recall():

    question = "What is RAG?"

    context = """
    RAG means Retrieval Augmented Generation.
    """

    answer = "RAG means Retrieval Augmented Generation."

    score = evaluate_context_recall(
        question,
        context,
        answer
    )

    assert isinstance(score, float)

    assert 0.0 <= score <= 1.0