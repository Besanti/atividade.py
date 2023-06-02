import streamlit as st
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

df = pd.read_csv('starwars.csv')

chart_data = pd.DataFrame(
    np.df(2, 3),
    columns=["name", "height", "mass"])


df = pd.read_csv('starwars.csv')

arq = open('starwars.csv')
for registro in csv.DictReader(arq, delimiter=','):


 st.dataframe(registro)

st.bar_chart(df)
