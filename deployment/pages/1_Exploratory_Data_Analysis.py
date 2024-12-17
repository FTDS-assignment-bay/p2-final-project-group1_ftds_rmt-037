import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import os

# Set page configuration
st.set_page_config(
    page_title="ShoeVibe Analysis App",
    page_icon="🔥",
    layout="wide",
)

# Title and Header
st.title("Exploratory Data Analysis 🔥")
st.header("🔥 ShoeVibe Dashboard")

# Embed the Tableau dashboard
tableau_url = "https://public.tableau.com/views/ShoeVibeApp/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
components.html(
    f'<iframe src="{tableau_url}?:embed=true" width="100%" height="800px" style="border:none;"></iframe>',
    height=800,
)

# Data Loading
data_file = os.path.join("pages", "cleaned_data_eda.csv")
if os.path.exists(data_file):
    data = pd.read_csv(data_file)
    st.success("Data loaded successfully!")
    # Proceed with your data processing and visualization
else:
    st.error(f"Data file not found at {data_file}. Please ensure the file exists.")
    st.stop()
