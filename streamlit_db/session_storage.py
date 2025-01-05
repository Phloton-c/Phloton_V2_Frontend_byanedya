import streamlit as st


def initialize_session_state():

    if "LoggedIn" not in st.session_state:
        st.session_state.LoggedIn = False

    if "view_role" not in st.session_state:
        st.session_state.view_role = "admin"

    if "user_permissions" not in st.session_state:
        st.session_state.user_permissions = []
    
    # ======== Anedya ====================
    if "nodeIds" not in st.session_state:
        st.session_state.nodeIds = []