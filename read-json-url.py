import requests
import json
import streamlit as st
st.set_page_config(layout="wide")


def buscar_dados():
    request = requests.get("https://example.vercel.app/get-all")
    todos = json.loads(request.content)
    todos
    # print(todos)
    print(todos[1]['title'])
    print(todos[1]['author'])

if __name__ == '__main__':
  buscar_dados()

