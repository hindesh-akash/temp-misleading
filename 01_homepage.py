# Import necessary libraries
import streamlit as st
from streamlit_player import st_player
from utils import set_api_key

st.set_page_config(
    page_title="Smart With Sebi",
    page_icon=":detective:",
    layout="wide",
)

with st.columns(3)[1]:
    st.image("media/smart_with_sebi.jpeg", width=200)

st.markdown("<h2 style='text-align: center; color: black;'>Welcome to Smart with SEBI portal<hr></h1>", unsafe_allow_html=True)

# Display the input field in the sidebar only if API key is not set
with st.sidebar:
    if not st.session_state.api_key:
        user_api_key = st.text_area("Enter your API Key here:")
        if st.button("Submit") and user_api_key:
            set_api_key(user_api_key)
            st.success("API Key set successfully!")
            st.session_state.api_key = user_api_key
    else:
        st.write(f"Your API key is: {st.session_state.api_key}")

st.markdown("<h3 style='text-align: left; color: black;'><hr> About this project:</h3>", unsafe_allow_html=True)

st.sidebar.success("Select a page above!")

st_player("https://www.youtube.com/watch?v=jNVTSDwTm14")
