import csv
import pandas as pd
import requests
import streamlit as st

df = pd.read_csv('starwars.csv')

arq = open('starwars.csv')
for registro in csv.DictReader(arq, delimiter=','):


 st.dataframe(registro)
