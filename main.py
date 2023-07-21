import streamlit as st
import json
from backend import get_bible_text


# Add page config and titles
st.set_page_config(page_title="Home",
                   page_icon="📖",
                   layout="wide")

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
version = st.selectbox("Seleccione la versión de la biblia",
                      ("Reina Valera Revisada 1960", "Reina Valera Actualizada"))

if version == "Reina Valera Revisada 1960":
    bible = detail_versions[0].get("bible")
    description = detail_versions[0].get("description")
if version == "Reina Valera Actualizada":
    bible = detail_versions[1].get("bible")
    description = detail_versions[1].get("description")

# Add bible version description
st.write(description)

# Add book Box
help = """
Los libros: Abdías, Filemón, 2 Juan, 3 Juan y Judas, solo tienen 1 capítulo. 
"""
book_es = st.selectbox("Seleccione el libro",
                       ([key for key in detail_chapters.keys()]),
                       help=help)
book_en = detail_chapters.get(book_es).get("Inglés")

# Add chapter Box
numbers = detail_chapters.get(book_es).get("Capítulos")

if numbers == 1:
    chapter = ""
else:
    chapter = st.selectbox("Seleccione el capítulo",
                           ([number for number in range(1, numbers + 1)]))

# Call bible chapter text
text = get_bible_text(version=bible, book=book_en, chapter=chapter)
st.write(text)
