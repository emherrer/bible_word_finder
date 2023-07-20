# -*- coding: utf-8 -*-

import requests as rq
import streamlit as st
import json


# Add page config and titles
st.set_page_config(page_title="Home",
                   page_icon="📖",
                   layout="centered")


# Add bible versions
with open("bible_versions.json", "r", encoding="utf-8") as file:
    versions = file.read()
detail_versions = json.loads(versions)

# Add title
st.title("Buscador de palabras".upper())

# Add Box
option = st.selectbox("Seleccione la versión de la biblia", 
            ("Reina Valera Revisada 1960", "Reina Valera Actualizada"))

if option == "Reina Valera Revisada 1960":
    bible = detail_versions[0].get("bible")
    description = detail_versions[0].get("description")
if option == "Reina Valera Actualizada":
    bible = detail_versions[1].get("bible")
    description = detail_versions[1].get("description")

# Add bible description
st.write(description)


api_key = st.secrets["BIBLEPASS"]
url = f"https://api.biblia.com/v1/bible/content/rva.txt.txt?passage=Genesis1.1&callback=myCallbackFunction&key=9fb4b5e1b6aa039451f4df65bf90f3ba"



