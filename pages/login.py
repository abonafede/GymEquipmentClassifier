import streamlit as st
import json
from streamlit_extras.switch_page_button import switch_page

# Function to check if the user is logged in
def is_logged_in():
    return st.session_state.is_logged_in

# Function to log in the user
def login(username, password):
    if username in user_data and user_data[username] == password:
        st.session_state.is_logged_in = True
        st.session_state.username = username
        st.success("Logged in successfully!")
    else:
        st.error("Invalid username or password")

# Function to log out the user
def logout():
    st.session_state.is_logged_in = False
    st.session_state.username = None
    st.success("Logged out successfully!")

# Path to the JSON file
JSON_FILE_PATH = 'db/users.json'

# Load the users data from the JSON file
with open(JSON_FILE_PATH, 'r') as f:
    user_data = json.load(f)

# Streamlit app
def auth():
    st.title("User Authentication")

    # Initialize the session state
    if 'is_logged_in' not in st.session_state:
        st.session_state.is_logged_in = False
        st.session_state.username = None

    if not is_logged_in():
        # Show the login form if the user is not logged in
        st.subheader("Log in")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Log in"):
            login(username, password)
        st.markdown("Don't have an account?")
        if st.button("Register"):
            switch_page('register')
    else:
        # Show the logout button if the user is logged in
        st.subheader(f"Logged in as {st.session_state.username}")
        if st.button("Log out"):
            logout()


if __name__ == '__main__':
    auth()
