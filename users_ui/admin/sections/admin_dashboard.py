import streamlit as st

from cloud.firestore.firestore_client_handler import firestore_client
from Home import anedya_client

def adminDashboard():
    headercols = st.columns([1,0.1, 0.1], gap="small")
    with headercols[0]:
        st.title("Admin Dashboard", anchor=False)
    with headercols[1]:
        on = st.button("Refresh")
        if on:
            st.rerun()
    with headercols[2]:
        logout = st.button("Logout")

    if logout:
        st.session_state.LoggedIn = False
        st.rerun()
    st.markdown("Phloton Last mile vaccine Delivery system.")

    container = st.container(border=True)
    with container:
        st.subheader("Overview")
        r1_metrics_cols = st.columns([1,1,1], gap="small")
        with r1_metrics_cols[0]:
            st.metric("Total Units", "10",border=True)
        with r1_metrics_cols[1]:
            total_users = firestore_client.collection("users").stream()
            st.metric("Total Users", len(list(total_users)),border=True)

adminDashboard()