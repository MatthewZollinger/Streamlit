import pandas as pd
import plotly.express as px
import streamlit as st

# Load the data
url = 'https://github.com/esnt/Data/raw/main/Names/popular_names.csv'
df = pd.read_csv(url)

# Define the Streamlit app
st.title('Baby Name Popularity')

name = st.text_input('Type a name', placeholder = "name")

fig = px.scatter(df[df["name"] == name], x='year',y='n', color='sex', hover_data=['n'], color_discrete_map = {"M" :"blue", "F": "pink"})
fig.update_layout(title=f'Name Popularity Over Time for {name}')
st.plotly_chart(fig)

