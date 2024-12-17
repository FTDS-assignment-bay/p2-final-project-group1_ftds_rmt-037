import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Shoevibe App",
    page_icon="🔥",
    layout="wide",
)

# Center the logo using columns
col1, col2, col3 = st.columns([2, 3, 1])
with col2:
    st.image("shoevibe.png")

# Main header and subheader, centered
st.markdown("<h1 style='text-align: center;'>Welcome to the Shoevibe App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Use the navigation menu to explore our application.</h2>", unsafe_allow_html=True)

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'Home'


