import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page

def display_exercises():
    st.title("Exercise List")
    st.write(st.session_state['equipment'])
if __name__ == '__main__':
    display_exercises()