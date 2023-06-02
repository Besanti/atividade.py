import streamlit as st
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

#df = pd.read_csv('starwars.csv')

#ages_count = df.Age.value_counts()

#x = ages_count.index
#y = ages_count.values

#plt.bar(sorted(x),y)
#plt.tittle('Star Wars Gráfico')

#for index, value in enumerate(y):
#    plt.text(index - 0,4, value, str(value))
    
#plt.show();


#st.bar_chart(df)

chart_datao = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_datao)
