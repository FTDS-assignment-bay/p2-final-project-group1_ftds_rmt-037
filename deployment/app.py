import streamlit as st
st.set_page_config(layout="wide")

pg = st.navigation([
    st.Page("home.py", title="Word Clouds", icon="🔥"),
    st.Page("prediction.py", title="Tokopedia Comments Analysis", icon="💬"),
])

pg.run()

