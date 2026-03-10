import requests
import os
import pandas as pd
from dotenv import load_dotenv

import streamlit as st



load_dotenv()


API_KEY = st.secrets["MONDAY_API_KEY"]
url = "https://api.monday.com/v2"

headers = {
    "Authorization": API_KEY,
    "API-Version": "2024-01"
}

query = """
{
 boards {
  name
  items_page {
   items {
    name
    column_values {
     text
     column {
      title
     }
    }
   }
  }
 }
}
"""

def fetch_data():

    response = requests.post(url, json={"query": query}, headers=headers)

    result = response.json()

    print(result)   # debug

    if "data" not in result:
        raise Exception(f"Monday API Error: {result}")

    boards = result["data"]["boards"]

    rows = []

    for board in boards:

        # Handle structural difference with items_page
        items = board.get("items_page", {}).get("items", []) if "items_page" in board else board.get("items", [])
        
        for item in items:

            row = {
                "board": board["name"],
                "item": item["name"]
            }

            for col in item["column_values"]:
                value = col["text"] if col["text"] else col.get("value", "Unknown")
                row[col["column"]["title"]] = value

            rows.append(row)

    df = pd.DataFrame(rows)

    df.fillna("Unknown", inplace=True)


    return df


