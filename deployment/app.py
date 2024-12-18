import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Shoevibe App",
    page_icon="🚀",
    layout="wide",
)

# Center the logo using columns
col1, col2, col3 = st.columns([2, 3, 1])
with col2:
    st.image("shoevibe.PNG")

# Main header and subheader, centered
st.markdown("<h1 style='text-align: center;'>Welcome to the Shoevibe App</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>ShoeVibe is an NLP-based application that analyzes customer sentiment for men's shoes on Tokopedia by extracting key terms from positive and negative reviews. It highlights frequent words to help buyers and sellers identify product strengths and weaknesses, enabling informed decision-making.</h4>", unsafe_allow_html=True)

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'Home'


