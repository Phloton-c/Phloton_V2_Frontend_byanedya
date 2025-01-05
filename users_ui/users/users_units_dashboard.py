# Show Overview data like total users, total units..
import streamlit as st
import os


def drawUsersDashboard():
    current_dir=os.getcwd()
    pages = {
        "Units": [
            st.Page(f"{current_dir}/units/unit_1.py", title="Unit 1", icon="🛜",default=True),
            st.Page(f"{current_dir}/units/unit_2.py", title="Unit 2",icon="🛜"),
            st.Page(f"{current_dir}/units/unit_3.py", title="Unit 3",icon="🛜"),
        ]
    }
    pg = st.navigation(pages)
    st.logo(f"{current_dir}/images/phloton_logo.png",size="large")
    st.sidebar.subheader("Phloton IoT Dashboard")
    pg.run()
    
    
