import streamlit as st
import requests
import pandas as pd
from pandas import DataFrame

from openai import OpenAI
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

if "history" not in st.session_state:
    st.session_state["history"] = []

st.title("LLM Evaluation Dashboard")

# TODO: on startup fetch models from backend server and populate this dropdown
# TODO: when a model is selected, pass it to the backend server for model selection

models = requests.get("http://127.0.0.1:8000/models").json()
print(models)

models = [m['id'] for m in models['data']]

selected_model = st.selectbox(
    "Select a model",
    models
)

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