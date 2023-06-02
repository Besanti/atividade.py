import streamlit as st
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from bokeh.plotting import figure

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

import streamlit as st


x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)
