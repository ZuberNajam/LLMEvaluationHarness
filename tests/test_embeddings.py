from app.embedding_metrics import semantic_similarity


def test_similarity():

    text1 = "RAG means Retrieval Augmented Generation."

    text2 = "Retrieval Augmented Generation is called RAG."

    score = semantic_similarity(
        text1,
        text2
    )

    print(score)

    assert score > 0.7

def test_low_similarity():

    text1 = "RAG means Retrieval Augmented Generation."

    text2 = "Pizza is popular in Italy."

    score = semantic_similarity(
        text1,
        text2
    )

    print(score)

    assert score < 0.5