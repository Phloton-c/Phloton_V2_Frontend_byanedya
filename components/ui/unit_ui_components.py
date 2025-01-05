import streamlit as st
import streamviz as sv
import numpy as np
import pandas as pd

from components.charts import draw_chart

def unit_header(title, des=None):
    if title is None:
        st.error("Please provide a valid title.")
    headercols = st.columns([1,0.06,0.11,0.12, 0.12], gap="small")
    with headercols[0]:
        st.title(title, anchor=False)
    with headercols[1]:
        st.button("0",disabled=True,use_container_width=True)
    with headercols[2]:
        st.button("Online",disabled=True,use_container_width=True)
    with headercols[3]:
        on = st.button("Refresh")
        if on:
            st.rerun()
    with headercols[4]:
        logout = st.button("Logout")
        if logout:
            st.session_state.LoggedIn = False
            st.rerun()
    if des is not None:
        st.markdown(des)

def unit_details(details:list=None):
    st.text("Device ID: ")
    st.text("MAC ID: ")
    st.text("IMEI No.: ")

def gauge_section():
    container = st.container(border=True,height=300)
    with container:
        st.text("Last Updated: ")
        r1_guage_cols = st.columns([1,1,1,1], gap="small")

        with r1_guage_cols[0]:
            sv.gauge(55/100,"Phloton Unit Battery SoC",cWidth=True,gSize="MED",sFix="%")
        with r1_guage_cols[1]:
            sv.gauge(16,"Battery Voltage",gMode="number",cWidth=True,gSize="MED",sFix="V")
        with r1_guage_cols[2]:
            sv.gauge(2,"Flask Temperature",cWidth=True,gSize="MED",sFix="°C",arTop=45)
        with r1_guage_cols[3]:
            sv.gauge(25,"Ambient Temperature",cWidth=True,gSize="MED",sFix="°C",arTop=45)

def graph_section():
    container = st.container(border=True)
    with container:
        data = {
                "Time": pd.date_range(start="2023-08-01", periods=24, freq="h"),
                "Temperature": np.random.normal(
                    loc=25, scale=5, size=24
                ),  # Example temperature data
            }
        df = pd.DataFrame(data)

        multislect_cols = st.columns([0.7,1], gap="small")
        with multislect_cols[0]:
            show_charts=st.multiselect("Select Charts",placeholder="Select Charts",options=["Phloton Unit Battery SoC","Battery Voltage","Flask Temperature"],label_visibility="hidden")
        
        
        r1_graph_cols = st.columns([1,1,1], gap="small")
        with r1_graph_cols[0]:
            draw_chart(chart_title="Phloton Unit Battery SoC",chart_data=df,y_axis_title="Percentage(%)")
        with r1_graph_cols[1]:
            draw_chart(chart_title="Battery Voltage",chart_data=df,y_axis_title="Voltage(V)")
        with r1_graph_cols[2]:
            draw_chart(chart_title="Flask Temperature",chart_data=df,y_axis_title="Celsius(°C)")
