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

def graph_section(node_client):
    container = st.container(border=True)
    with container:
        data = {
                "Time": pd.date_range(start="2023-08-01", periods=24, freq="h"),
                "Temperature": np.random.normal(
                    loc=25, scale=5, size=24
                ),  # Example temperature data
            }
        df = pd.DataFrame(data)
        currentTime = int(time.time())    #to means recent time
        pastHour_Time = int(currentTime - 86400)

        # multislect_cols = st.columns([0.7,1], gap="small")
        # with multislect_cols[0]:
        #     show_charts=st.multiselect("Select Charts",placeholder="Select Charts",options=["Phloton Unit Battery SoC","Battery Voltage","Flask Temperature"],label_visibility="hidden")
        
        
        r1_graph_cols = st.columns([1,1], gap="small")
        with r1_graph_cols[0]:
            unit_battery_soc_data=node_client.get_data("temperature", pastHour_Time, currentTime)
            # st.write(unit_battery_soc_data)
            draw_chart(chart_title="Phloton Unit Battery SoC",chart_data=unit_battery_soc_data,y_axis_title="Temperature")
        with r1_graph_cols[1]:
            # draw_chart(chart_title="Battery Voltage",chart_data=df,y_axis_title="Voltage(V)")
            pass
        # with r1_graph_cols[2]:
        #     draw_chart(chart_title="Flask Temperature",chart_data=df,y_axis_title="Celsius(°C)")

        r2_graph_cols = st.columns([1,1,1], gap="small") 
        with r2_graph_cols[0]:
            # draw_chart(chart_title="Ambient Temperature",chart_data=df,y_axis_title="Celsius(°C)")
            pass