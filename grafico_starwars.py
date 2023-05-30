import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('starwars.csv')

chart_data = pd.DataFrame(
    np.starwars.cvs(2, 3),
    columns=["name", "height", "mass"])

st.bar_chart(chart_data)
