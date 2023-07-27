import streamlit as st
import json
from backend import get_bible_text
from nlp import get_wordcloud_data_and_plot
import plotly.express as px


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
st.title("Nube de palabras Biblicas".upper())
st.subheader("Visualiza la Palabra de Dios por Libro y Capítulo")

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

# Add columns for graphs
col1, col2 = st.columns([2, 1])

with col1:
    # Add wordcloud data and graph
    data, graph = get_wordcloud_data_and_plot(
        version=bible, book=book_en, chapter=chapter)
    st.image("wordcloud_fig.png",
             caption=f"Nube de palabras de {book_es} capítulo {chapter}")

with col2:
    # Add Plotly Top 20 words (color_discrete_sequence=["#00172B"])
    top = 5
    st.subheader(f"Primeras {top} palabras mas repetidas")
    keys = list(data.keys())[:top][::-1]
    values = list(data.values())[:top][::-1]
    fig = px.bar(x=values, y=keys, text=values, orientation="h")
    fig.update_traces(textposition='outside')
    fig.update_layout(title='', xaxis_title='Frecuencia',
                      yaxis_title='Palabra')
    st.plotly_chart(fig, use_container_width=True)

# Call bible chapter text
st.subheader(f"{book_es} capítulo {chapter}:")
text = get_bible_text(version=bible, book=book_en, chapter=chapter)
st.write(text)
