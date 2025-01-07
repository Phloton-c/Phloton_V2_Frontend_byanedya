import streamlit as st
from components.ui.unit_ui_components import unit_header
from components.ui.unit_ui_components import unit_details
from components.ui.unit_ui_components import gauge_section
from components.ui.unit_ui_components import graph_section
from cloud.anedya_cloud import Anedya
import time
def draw_unit_1_dashboard():
    anedya= Anedya()
    NODE_ID= st.session_state.nodesId["node_1"]
    VARIABLES_IDENTIFIER= st.session_state.variablesIdentifier

    node=anedya.new_node(st.session_state.anedya_client, nodeId=NODE_ID)
    device_status_res=node.get_deviceStatus()
    unit_header("Phloton Unit 1", device_status_res=device_status_res)

    unit_details()

    gauge_data_list=[0,0,0,0,0]
    unit_battery_soc_res=node.get_latestData(VARIABLES_IDENTIFIER["variable_1"].get("identifier"))
    if unit_battery_soc_res.get("isSuccess") and unit_battery_soc_res.get("data") is not None:
        unit_battery_soc=unit_battery_soc_res.get("data")
        gauge_data_list[0]=unit_battery_soc
    battery_voltage_res=node.get_latestData(VARIABLES_IDENTIFIER["variable_2"].get("identifier"))
    if battery_voltage_res.get("isSuccess") and battery_voltage_res.get("data") is not None:    
        battery_voltage=battery_voltage_res.get("data")
        gauge_data_list[1]=battery_voltage
    flask_temperature_res=node.get_latestData(VARIABLES_IDENTIFIER["variable_3"].get("identifier"))
    if flask_temperature_res.get("isSuccess") and flask_temperature_res.get("data") is not None:
        flask_temperature=flask_temperature_res.get("data")
        gauge_data_list[2]=flask_temperature
    ambient_temperature_res=node.get_latestData(VARIABLES_IDENTIFIER["variable_4"].get("identifier"))
    if ambient_temperature_res.get("isSuccess") and ambient_temperature_res.get("data") is not None:
        ambient_temperature=ambient_temperature_res.get("data")
        gauge_data_list[3]=ambient_temperature
        ambient_temperature=ambient_temperature_res.get("timestamp")
        gauge_data_list[4]=ambient_temperature
    gauge_section(gauge_data_list)

    currentTime = int(time.time())    #to means recent time
    pastHour_Time = int(currentTime - 86400)

    chart_data_list=[0,0,0,0]
    unit_battery_soc_data=node.get_data(VARIABLES_IDENTIFIER["variable_1"].get("identifier"), pastHour_Time, currentTime)
    battery_voltage_data=node.get_data(VARIABLES_IDENTIFIER["variable_2"].get("identifier"), pastHour_Time, currentTime)
    flask_temperature_data=node.get_data(VARIABLES_IDENTIFIER["variable_3"].get("identifier"), pastHour_Time, currentTime)
    ambient_temperature_data=node.get_data(VARIABLES_IDENTIFIER["variable_4"].get("identifier"), pastHour_Time, currentTime)
    chart_data_list[0]=unit_battery_soc_data
    chart_data_list[1]=battery_voltage_data
    chart_data_list[2]=flask_temperature_data
    chart_data_list[3]=ambient_temperature_data
    graph_section(node)

draw_unit_1_dashboard()