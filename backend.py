import requests
import streamlit as st


def get_bible_text(version, book, chapter):
    # Request
    api_key = st.secrets["BIBLEPASS"]
    url = f"https://api.biblia.com/v1/bible/content/{version}.txt?passage={book}{chapter}&key={api_key}"

    # Get data
    response = requests.get(url)
    data = response.text

    return data


if __name__ == "__main__":
    print(get_bible_text(version="rvr60", book="Acts", chapter="3"))