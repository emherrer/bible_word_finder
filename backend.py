import requests
import streamlit as st


# Bible Table Contents
api_key = st.secrets["BIBLEPASS"]
url = f"https://api.biblia.com/v1/bible/content/rva.txt.txt?passage=Genesis1.1&callback=myCallbackFunction&key={api_key}"

# Get requests
table_content = requests.get(url).json()

print(table_content)