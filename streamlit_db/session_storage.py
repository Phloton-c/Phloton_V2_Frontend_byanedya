import streamlit as st


def initialize_session_state():

    if "view_role" not in st.session_state:
        st.session_state.view_role = "admin"

    if "user_permissions" not in st.session_state:
        st.session_state.user_permissions = []
    
    # ======== Anedya ====================
    if "anedya_client" not in st.session_state:
        st.session_state.anedya_client = None

    if "nodeIds" not in st.session_state:
        st.session_state.nodesId = {}
        
    if "variablesIdentifier" not in st.session_state:
        st.session_state.variablesIdentifier = {}
    
    # ======== Firestore =================
    if "firestore_client" not in st.session_state:
        st.session_state.firestore_client = None

    # ======== HTTP ======================
    if "http_client" not in st.session_state:
        st.session_state.http_client = None



