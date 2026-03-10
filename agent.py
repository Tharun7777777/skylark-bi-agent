import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_agent(question, df):

    data = df.head(100).to_string()

    prompt = f"""
You are a Business Intelligence AI.

Dataset preview:
{data}

Answer the founder question with insights.

Question:
{question}

Mention if data is incomplete.
"""

    response = model.generate_content(prompt)


    return response.text
