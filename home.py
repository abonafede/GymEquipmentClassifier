import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
from pred import predict
import json

def run_ui():
    st.set_page_config(
        page_title="Workout Helper",
        page_icon="",
        layout="wide")

    st.title("Workout Helper")
    # Initialize the session state
    if 'is_logged_in' not in st.session_state:
        st.session_state.is_logged_in = False
        st.session_state.username = None

    if 'equipment' not in st.session_state:
        st.session_state['equipment'] = None
    
    if not st.session_state.is_logged_in:
        if st.button("Log in"):
            switch_page('login')
    else:
        st.caption('Hello ' + str(st.session_state.username)+'!')

    st.markdown("""---""")
    image_upload = st.file_uploader("Upload images", type=['jpg', 'jpeg', 'png'],accept_multiple_files=True)
    
    equipment = set()
    if image_upload is not None:
        if len(image_upload) > 0:
            for image in image_upload:
                labels = predict(image)
                for label in labels:
                    if label[1] > 0.25:
                        equipment.add(label[0])
            st.session_state['equipment'] = equipment
            st.subheader("You have access to the following equipment:")
            for piece in equipment:
                st.write(piece)
            ex = st.button(label="Click here to view possible exercises")
            if ex:
                switch_page('exercises')
if __name__ == '__main__':
    run_ui()