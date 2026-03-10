import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("MONDAY_API_KEY")
url = "https://api.monday.com/v2"
headers = {"Authorization": API_KEY}
query = """
{
 boards {
  name
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
"""
response = requests.post(url, json={"query": query}, headers=headers)
with open("monday_resp.txt", "w", encoding="utf-8") as f:
    f.write(json.dumps(response.json(), indent=2))
