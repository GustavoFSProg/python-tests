import requests
import json
import streamlit as st
st.set_page_config(layout="wide")


def buscar_dados():
    request = requests.get("https://pcsdetran.rs.gov.br/")
    todos = json.loads(request.content)
    todos
    # print(todos)
    # print(todos[1]['title'])
    # print(todos[1]['text'])

if __name__ == '__main__':
  buscar_dados()

