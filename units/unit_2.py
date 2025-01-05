import streamlit as st
from components.ui.unit_ui_components import unit_header
from components.ui.unit_ui_components import unit_details
from components.ui.unit_ui_components import gauge_section
from components.ui.unit_ui_components import graph_section

def draw_unit_2_dashboard():
    unit_header("Phloton Unit 2")
    unit_details()
    gauge_section()
    graph_section()

draw_unit_2_dashboard()