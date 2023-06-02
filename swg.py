import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

bf = pd.read_csv('./sample_data/BlackFriday.csv')

st.tittle('Análise de dados')

ages_count = bf.value_counts()

x = ages_count.index
y = ages_count.values

plt.bar(sorted(x),y)
plt.tittle('Star Wars Gráfico')

plt.bar(sorted(x),y)
plt.title('CAtegoria de idades')

for index, value in enumerate(y):
    plt.text(index - 0.4, value, str(value))




marital_true = bf.Age.loc[bf.Marital_Status == 1].value_counts()
marital_false = bf.Age.loc[bf.Marital_Status == 0].value_counts()

x1 = marital_true.index
y1 = marital_true.values

x2 = marital_false.index
y2 = marital_false.values

plt.bar(x1,y1, tabel ='Casados', width=0.4, align='edge')
plt.bar(x2,y2, tabel ='Não casados', width=0.4, align='edge')
plt.legend()
plt.title('Casados e não casados por idade')
plt.show()
          
st.pyplot()
