import requests as rq
import streamlit as st
import json


# Add page config and titles
st.set_page_config(page_title="Home",
                   page_icon="📖",
                   layout="centered")

# Load bible versions
with open("bible_versions.json", "r", encoding="utf-8") as file:
    versions = file.read()
detail_versions = json.loads(versions)

# Load bible chapters name and numbers
with open("bible.json", "r", encoding="utf-8") as file:
    versions = file.read()
detail_chapters = json.loads(versions)


# Add title widget
st.title("Buscador de palabras".upper())

# Add bible version box
option = st.selectbox("Seleccione la versión de la biblia",
                      ("Reina Valera Revisada 1960", "Reina Valera Actualizada"))

if option == "Reina Valera Revisada 1960":
    bible = detail_versions[0].get("bible")
    description = detail_versions[0].get("description")
if option == "Reina Valera Actualizada":
    bible = detail_versions[1].get("bible")
    description = detail_versions[1].get("description")

# Add bible version description
st.write(description)

# Add book Box
book = st.selectbox("Seleccione el libro",
                    ([key for key in detail_chapters.keys()]))

# Add chapter Box
numbers = detail_chapters.get(book)
chapter = st.selectbox("Seleccione el capítulo",
                       ([number for number in range(1, numbers + 1)]))
