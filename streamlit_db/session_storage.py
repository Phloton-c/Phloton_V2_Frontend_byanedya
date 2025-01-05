import streamlit as st


def initialize_session_state():

    if "LoggedIn" not in st.session_state:
        st.session_state.LoggedIn = True

    if "view_role" not in st.session_state:
        st.session_state.view_role = "admin"

    if "users_permissions" not in st.session_state:
        st.session_state.users_permissions = {}
    
    # ======== Anedya ====================
    if "nodeIds" not in st.session_state:
        st.session_state.nodeIds = []