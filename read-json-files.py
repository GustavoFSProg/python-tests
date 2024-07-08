import json
import streamlit as st
import xml.etree.ElementTree as et

st.set_page_config(layout="wide") 

with open("dados.json") as file:
   data= json.load(file)

   print(data)

data



