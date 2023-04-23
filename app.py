import streamlit as st

def run_ui():
    st.set_page_config(
        page_title="Workout Helper",
        page_icon="",
        layout="wide")

    st.title("Workout Helper")
    st.markdown("""---""")
    st.markdown("**Upload Files**")

if __name__ == '__main__':
    run_ui()