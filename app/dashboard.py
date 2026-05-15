import streamlit as st
import requests
import pandas as pd
from pandas import DataFrame

if "history" not in st.session_state:
    st.session_state["history"] = []

st.title("LLM Evaluation Dashboard")


question = st.text_input(
    "Enter a question"
)


if st.button("Evaluate"):

    response = requests.post(
        "http://127.0.0.1:8000/answer",
        json={"question": question}
    )

    st.write("Status Code:", response.status_code)

    st.write("Raw Response:")

    st.write(response.text)

    data = response.json()

    st.subheader("Generated Answer")

    st.write(data["answer"])

    st.subheader("Evaluation Metrics")

    st.metric(
        "Hallucination Check",
        data["hallucination_check"]
    )

    st.metric(
        "Context Precision",
        round(data["context_precision"], 2)
    )

    st.metric(
        "Context Recall",
        round(data["context_recall"], 2)
    )

    st.metric(
        "Answer Similarity",
        round(data["answer_similarity"], 2)
    )

    st.metric(
        "Latency",
        round(data["latency"], 2)
    )

    st.session_state.history.append(data)

    df: DataFrame = pd.DataFrame(st.session_state.history)


    st.subheader("Evaluation Trends")

    st.line_chart(
        df [
            [
                "hallucination_check",
                "context_precision",
                "context_recall",
                "answer_similarity",
                "latency",
            ]
        ]
)