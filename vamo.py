import csv
import streamlit as st

arquii = 'C:dplyr/data-raw/starwars.csv'

def listar_conteudo(arquii):
    with open(arquii, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            st.write(linha)

arquivo_csv = 'starwars.csv'
listar_conteudo(arquivo_csv)
