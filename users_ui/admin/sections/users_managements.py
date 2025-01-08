import pandas as pd
import streamlit as st



def manage_users_ui():
    headercols = st.columns([1, 0.1, 0.1], gap="small")
    with headercols[0]:
        st.title("User Managements", anchor=False)
    with headercols[1]:
        on = st.button("Refresh")
        if on:
            st.rerun()
    with headercols[2]:
        logout = st.button("Logout")

    if logout:
        st.session_state.LoggedIn = False
        st.rerun()

    container = st.container(border=True)
    with container:
        tab1, tab2 = st.tabs(["Edit User", "Delete User"])
        with tab1:
            edits_user_ui()
        with tab2:
            delete_user_ui()

    list_users_ui()


def delete_user_ui():
    st.subheader("Delete User")
    delete_user_col = st.columns([0.3, 1, 0.3], gap="small")
    with delete_user_col[0]:
        pass
    with delete_user_col[1]:
        with st.form(key="delete_user", clear_on_submit=True, border=False):
            email = st.text_input("Email", placeholder="Email").strip()
            submit_button = st.form_submit_button(label="Submit")
            if submit_button:
                if email == "":
                    st.error("Please provide a valid email")
                else:
                    delete_user(email)


def delete_user(email):
    try:
        response = st.session_state.firestore_client.collection("users").document(email).delete()
        if response is not None:
            st.toast("User deleted successfully", icon="🎉")
        else:
            st.error("Error in user deletion")

    except Exception as e:
        st.error(e)


def edit_user(email, edit_req_payload):
    try:
        response = (
            st.session_state.firestore_client.collection("users")
            .document(email)
            .update(edit_req_payload)
        )
        if response is not None:
            st.toast("User updated successfully", icon="🎉")
        else:
            st.error("Error in user update")

    except Exception as e:
        st.error(e)


def edits_user_ui():

    st.subheader("Edit User")
    edit_user_col = st.columns([0.3, 1, 0.3], gap="small")
    with edit_user_col[0]:
        pass
    with edit_user_col[1]:
        email = st.text_input("Email", placeholder="Email").strip()
        edit_key = st.multiselect(
            "Select Credentials",
            placeholder="Select Credentials",
            options=["Name", "Password", "Permissions"],
        )

        edit_req_payload = {}
        with st.form(key="edit_user", clear_on_submit=True, border=False):

            if "Name" in edit_key:
                name = st.text_input("Name").strip()
                edit_req_payload["name"] = name
            if "Password" in edit_key:
                password = st.text_input("Password", type="password").strip()
                edit_req_payload["password"] = password
            if "Permissions" in edit_key:
                options = [
                    "Unit-1",
                    "Unit-2",
                    "Unit-3",
                    "Unit-4",
                    "Unit-5",
                    "Unit-6",
                    "Unit-7",
                    "Unit-8",
                    "Unit-9",
                    "Unit-10",
                ]
                permissions = st.pills("Permissions", options, selection_mode="multi")
                edit_req_payload["permissions"] = permissions
            submit_button = st.form_submit_button(label="Submit")
            if submit_button:
                if email == "":
                    st.toast("Please provide a valid email", icon="🚫")
                elif "name" in edit_key and edit_req_payload["name"] == "":
                    st.toast("Please provide a valid name", icon="🚫")
                elif "password" in edit_key and edit_req_payload["password"] == "":
                    st.toast("Please provide a valid password", icon="🚫")
                else:
                    edit_user(email, edit_req_payload)


def list_users_ui():
    container = st.container(border=True)
    list_users = st.session_state.firestore_client.collection("users").stream()
    user_dict = {user.id: user.to_dict() for user in list_users}

    formatted_data = {
        "Name": [user["name"] for user in user_dict.values()],
        "Email": [user["email"] for user in user_dict.values()],
        "Permissions": [", ".join(user["permissions"]) for user in user_dict.values()],
    }

    data_df = pd.DataFrame(formatted_data)
    data_df.index += 1

    with container:
        st.subheader("Users List")
        st.dataframe(
            data_df,
            use_container_width=True,
        )


manage_users_ui()
