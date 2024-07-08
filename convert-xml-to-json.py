import xmltodict
import json
import streamlit as st
import pandas as pd
import ujson

st.set_page_config(layout="wide")
with st.container():arquivo_xml = 'livros.xml'
def converter_xml_para_json(arquivo_xml):
    with open(arquivo_xml, 'r') as file:
        xml_data = file.read()
        dict_data = xmltodict.parse(xml_data)
        json_data = json.dumps(dict_data, indent=4)
        return json_data

json_data = converter_xml_para_json(arquivo_xml)

print(json_data)

my_data = json.dumps(json_data, indent=4)

my_data

with open("dados.json", "w") as file:
    ujson.dump(json_data, file)

# Criando um DataFrame com os dados
# df = pd.DataFrame(json_data)

# # Escrevendo os dados no arquivo JSON
# df.to_json("dados.json")



# ('novo_json.json')

# arquivo_xml


