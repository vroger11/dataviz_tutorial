import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

st.write("""# Dataviz tutorial
Interactive course to do dataviz (work in progress)""")


df=px.data.tips()

st.write("""## Data""")
st.dataframe(df)


st.write("""## Excercice""")
st.write("""We want to visualise the proportion of bills per day from the previouly shown data.""")
option = st.selectbox(
    'What type of chart you want to use?',
    ('None', 'Bar charts', 'Pie charts'))

if option == "Bar charts":
    horizontal = st.checkbox("Horizontal bars?", value=False)
    if horizontal:
        fig=px.bar(df,x='total_bill',y='day', orientation='h', title='Bills per day of the week')
    else:
        fig=px.bar(df,x='day',y='total_bill', orientation='v', title='Bills per day of the week')
elif option == 'Pie charts':
    fig = px.pie(df, values='total_bill', names='day', title='Bills per day of the week')

else:
    fig = ""

st.write(fig)

