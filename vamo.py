import csv
import streamlit as st

def listar_conteudo(starwars_csv):
    with open(starwars_csv, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            st.write(linha)

arquivo_csv = 'starwars.csv'
listar_conteudo(arquivo_csv)
