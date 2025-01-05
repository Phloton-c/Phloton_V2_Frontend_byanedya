"""Phloton Dashboard."""

import streamlit as st
import os
import pytz
from datetime import date, datetime, timedelta, time
from streamlit_autorefresh import st_autorefresh


from streamlit_db.session_storage import initialize_session_state
from cloud.firestore.firestore_client_handler import firebase_db_setup
from cloud.firestore.firestore_client_handler import firestore_client
from streamlit_db.users_management import phloton_users
from css.control_streamlit_cloud_features import hide_streamlit_style
from cloud.anedya import anedya_config
from cloud.anedya import get_nodeList
from users_ui.admin.admin_dashboard import drawAdminDashboard
from users_ui.users.users_units_dashboard import drawUsersDashboard


st.set_page_config(page_title="Phloton IoT Dashboard", layout="wide")

refresh_interval = 30000
st_autorefresh(interval=refresh_interval, limit=None, key="auto-refresh-handler")


# --------------- HELPER FUNCTIONS -----------------------
def V_SPACE(lines):
    for _ in range(lines):
        st.write("&nbsp;")


def main():

    # ------------------- Project Configuration -----------------------
    initialize_session_state() # Initialize Session State
    firebase_db_setup()  # Firebase client Setup
    # Manage Anedya Connection Credentials
    API_KEY=st.secrets["API_KEY"]
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # ---------------------- UI ---------------------------------------
    if st.session_state.LoggedIn is False:
        drawLogin()
    else:
        success = anedya_config(API_KEY=API_KEY)
        if not success:
            st.stop()
        else:
            if st.session_state.view_role == "admin":
                drawAdminDashboard()
            else:
                drawUsersDashboard()


def drawLogin():
    current_dir=os.getcwd()
    pages = {
        "Units": [
            st.Page(f"{current_dir}/units/unit_1.py", title="Unit 1"),
        ]
    }
    st.navigation(pages,position="hidden")

    cols = st.columns([1, 1.2, 1], gap="small")
    with cols[0]:
        pass
    with cols[1]:
            st.title("Phloton Dashboard Login", anchor=False)
            username_inp = st.text_input("Username").strip()
            password_inp = st.text_input("Password", type="password").strip()
            submit_button = st.button(label="Submit")
            if submit_button:
                check_credentials(username_inp, password_inp)
            

def check_credentials(username,password):
    phloton_u = firestore_client.collection("users").get(username)
    st.write(phloton_u)
    st.stop()
    if (
        username in phloton_users["admins"]
        and phloton_users["admins"][username]["password"] == password
    ):
        st.session_state.view_role = "admin"
        st.session_state.LoggedIn = True
        st.rerun()
    elif (
        username in phloton_users["user"]
        and phloton_users["user"][username]["password"] == password
    ):
        st.session_state.view_role = "user"
        st.session_state.LoggedIn = True
        st.rerun()
    else:
        st.error("Invalid Credential!")

if __name__ == "__main__":
    main()
