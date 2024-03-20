import streamlit as st
import plotly.express as px
import json
import pandas as pd

# Load the data from the JSON file
@st.cache_data
def load_data():
    with open('trending_repositories.json', 'r') as file:
        data = json.load(file)
    return data

# Load data
data = load_data()

# Convert data to a format suitable for Plotly
repos = [repo['name'] for repo in data]
stars_today = [repo['stars_today'] for repo in data]
df = pd.DataFrame({'Repository': repos, 'Stars Today': stars_today})

# Create a bar chart using Plotly
fig = px.bar(df, x='Repository', y='Stars Today', title='GitHub Trending Repositories - Stars Today')

# Display the chart
st.title('GitHub Trending Repositories')
st.plotly_chart(fig)
