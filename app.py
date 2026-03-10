import streamlit as st
from data_fetcher import fetch_data
from agent import ask_agent

st.title("Skylark Monday Business Intelligence Agent")

st.write("Ask questions about deals, revenue, and pipeline.")

df = fetch_data()

st.write("Connected Data Preview")

st.dataframe(df.head())

question = st.text_input("Ask a business question")

if question:

    answer = ask_agent(question, df)

    st.subheader("Insight")

    st.write(answer)


if st.button("Generate Leadership Update"):

    summary = ask_agent(
        "Give leadership summary about revenue, pipeline, sector performance",
        df
    )

    st.write(summary)