# Show Overview data like total users, total units..
import streamlit as st
import os


def drawAdminDashboard():
    
    current_dir=os.getcwd()
    pages = {
        "Admin": [
            st.Page(f"{current_dir}/users_ui/admin/sections/admin_dashboard.py", title="Admin Dashboard"),
            st.Page(f"{current_dir}/users_ui/admin/sections/create_users.py", title="Create Users",default=True),
            st.Page(f"{current_dir}/users_ui/admin/sections/users_managements.py", title="Users Managements"),
        ],
        "Units": [
            st.Page(f"{current_dir}/units/unit_1.py", title="Unit 1", icon="🛜"),
            st.Page(f"{current_dir}/units/unit_2.py", title="Unit 2",icon="🛜"),
            st.Page(f"{current_dir}/units/unit_3.py", title="Unit 3",icon="🛜"),
            st.Page(f"{current_dir}/units/unit_4.py", title="Unit 4",icon="🛜"),
            st.Page(f"{current_dir}/units/unit_5.py", title="Unit 5",icon="🛜"),
            st.Page(f"{current_dir}/units/unit_6.py", title="Unit 6",icon="🛜"),
            st.Page(f"{current_dir}/units/unit_7.py", title="Unit 7",icon="🛜"),
            st.Page(f"{current_dir}/units/unit_8.py", title="Unit 8",icon="🛜"),
            st.Page(f"{current_dir}/units/unit_9.py", title="Unit 9",icon="🛜"),
            st.Page(f"{current_dir}/units/unit_10.py", title="Unit 10",icon="🛜"),
            st.Page(f"{current_dir}/units/unit_11.py", title="Unit 11", icon="🛜"),
            st.Page(f"{current_dir}/units/unit_12.py", title="Unit 12",icon="🛜"),
            st.Page(f"{current_dir}/units/unit_13.py", title="Unit 13",icon="🛜"),
            st.Page(f"{current_dir}/units/unit_14.py", title="Unit 14",icon="🛜"),
            st.Page(f"{current_dir}/units/unit_15.py", title="Unit 15",icon="🛜"),
            st.Page(f"{current_dir}/units/unit_16.py", title="Unit 16",icon="🛜"),
            st.Page(f"{current_dir}/units/unit_17.py", title="Unit 17",icon="🛜"),
            st.Page(f"{current_dir}/units/unit_18.py", title="Unit 18",icon="🛜"),
            st.Page(f"{current_dir}/units/unit_19.py", title="Unit 19",icon="🛜"),
            st.Page(f"{current_dir}/units/unit_20.py", title="Unit 20",icon="🛜"),
            st.Page(f"{current_dir}/units/unit_21.py", title="Unit 21",icon="🛜"),
        ]
    }
    pg = st.navigation(pages)
    st.logo(f"{current_dir}/images/phloton_logo.png",size="large")
    st.sidebar.subheader("Phloton IoT Dashboard")
    st.sidebar.markdown("Phloton Last mile vaccine Delivery system.")
    pg.run()
    
    





