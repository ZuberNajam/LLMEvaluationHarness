from app.evaluator import evaluate_hallucination


def test_grounded_answer():

    context = """
    RAG means Retrieval Augmented Generation.
    """

    answer = "RAG means Retrieval Augmented Generation."

    result = evaluate_hallucination(
        context,
        answer
    )

    assert result == "PASS"


def test_hallucinated_answer():

    context = """
    RAG means Retrieval Augmented Generation.
    """

    answer = "RAG was invented by Google."

    result = evaluate_hallucination(
        context,
        answer
    )

    assert result == "FAIL"

def test_partial_hallucination():

    context = """
    AWS stands for Amazon Web Services.
    """

    answer = """
    AWS stands for Amazon Web Services
    and was founded in 2012.
    """

    result = evaluate_hallucination(
        context,
        answer
    )

    assert result == "FAIL"