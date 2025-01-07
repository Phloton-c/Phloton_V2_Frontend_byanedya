import streamlit as st
import streamviz as sv
from datetime import datetime
import pytz
import numpy as np
import pandas as pd
import time

from components.charts import draw_chart

def unit_header(title, des=None, device_status_res=None):
    if title is None:
        st.error("Please provide a valid title.")
    headercols = st.columns([1,0.06,0.11,0.12, 0.12], gap="small")
    with headercols[0]:
        st.title(title, anchor=False)
    with headercols[1]:
        st.button("0",disabled=True,use_container_width=True)
    with headercols[2]:
        if device_status_res is not None or device_status_res.get("status") is True:
            device_status=None
            if device_status_res.get("device_status"):
                device_status="Online"
            else:
                device_status="Offline"
        else:
            device_status="..."
        st.button(device_status,disabled=True,use_container_width=True)
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

def gauge_section(data:list=None):
    container = st.container(border=True,height=300)
    with container:
        
        if data[4]!=0:
            indian_time_zone = pytz.timezone('Asia/Kolkata')   # set time zone
            hr_timestamp = datetime.fromtimestamp(data[4], indian_time_zone)
            fm_hr_timestamp=hr_timestamp.strftime('%Y-%m-%d %H:%M:%S %Z')
        else:
            fm_hr_timestamp="0"
        st.text(f"Last Updated: {fm_hr_timestamp}")
        r1_guage_cols = st.columns([1,1,1,1], gap="small")

        with r1_guage_cols[0]:
            sv.gauge(data[0]/100,"Phloton Unit Battery SoC",cWidth=True,gSize="MED",sFix="%")
        with r1_guage_cols[1]:
            sv.gauge(data[1],"Battery Voltage",gMode="number",cWidth=True,gSize="MED",sFix="V")
        with r1_guage_cols[2]:
            sv.gauge(data[2],"Flask Temperature",cWidth=True,gSize="MED",sFix="°C",arTop=45)
        with r1_guage_cols[3]:
            sv.gauge(data[3],"Ambient Temperature",cWidth=True,gSize="MED",sFix="°C",arTop=45)

def graph_section(node_client=None):
    if node_client is None:
        st.stop()
    container = st.container(border=True)
    with container:
        currentTime = int(time.time())    #to means recent time
        pastHour_Time = int(currentTime - 86400)

        options:list=None
        if st.session_state.view_role == "user":
            options=["Unit Battery SoC","Battery Voltage","Flask Temperature","Ambient Temperature"]
        else:
            options=["Unit Battery SoC","Battery Voltage","Flask Temperature", "Ambient Temperature"]

        VARIABLES=st.session_state.variablesIdentifier
        # st.write(VARIABLES)

        multislect_cols = st.columns([0.7,1], gap="small")
        with multislect_cols[0]:
            show_charts=st.multiselect("Select Charts",placeholder="Select Charts",options=options,label_visibility="hidden")
        if (show_charts is None) or (len(show_charts)==0):
            st.stop()

        if len(show_charts)>0:
            r1_graph_cols = st.columns([1,1,1], gap="small")
            with r1_graph_cols[0]:
                identifier = get_identifier_by_name(VARIABLES, show_charts[0])
                unit_battery_soc_data=node_client.get_data(identifier, pastHour_Time, currentTime)
                draw_chart(chart_title=show_charts[0],chart_data=unit_battery_soc_data,y_axis_title="Temperature")
            with r1_graph_cols[1]:
                if len(show_charts)>1:
                    identifier = get_identifier_by_name(VARIABLES, show_charts[1])
                    data=node_client.get_data(identifier, pastHour_Time, currentTime)
                    draw_chart(chart_title=show_charts[1],chart_data=data,y_axis_title="Voltage(V)")
            with r1_graph_cols[2]:
                if len(show_charts)>2:
                    identifier = get_identifier_by_name(VARIABLES, show_charts[2])
                    data=node_client.get_data(identifier, pastHour_Time, currentTime)
                    draw_chart(chart_title=show_charts[2],chart_data=data,y_axis_title="Celsius(°C)")

        if len(show_charts)>3:
            r2_graph_cols = st.columns([1,1,1], gap="small") 
            with r2_graph_cols[0]:
                identifier = get_identifier_by_name(VARIABLES, show_charts[3])
                data=node_client.get_data(identifier, pastHour_Time, currentTime)
                draw_chart(chart_title=show_charts[3],chart_data=data,y_axis_title="Celsius(°C)")


def get_identifier_by_name(data, search_name):
    for variable in data.values():
        if variable["name"] == search_name:
            return variable["identifier"]
    return None  # Return None if not found