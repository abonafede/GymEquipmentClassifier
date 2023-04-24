import streamlit as st
import json

# Path to the JSON file
JSON_FILE_PATH = 'db/users.json'

# Load the users data from the JSON file
with open(JSON_FILE_PATH, 'r') as f:
    user_data = json.load(f)

# Function to add a new user to the database
def add_user(username, password):
    if username not in user_data:
        user_data[username] = password
        with open(JSON_FILE_PATH, 'w') as f:
            json.dump(user_data, f)
        st.success("User created!")
    else:
        st.error("Username already exists")

def register():
    # Show the registration form if the user clicked on the "Register" button
    st.subheader("Register")
    new_username = st.text_input("New username")
    new_password = st.text_input("New password", type="password")
    if st.button("Create account"):
        add_user(new_username, new_password)

if __name__ == '__main__':
    register()