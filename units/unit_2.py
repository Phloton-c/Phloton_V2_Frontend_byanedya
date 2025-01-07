import streamlit as st
from components.ui.unit_ui_components import unit_header
from components.ui.unit_ui_components import unit_details
from components.ui.unit_ui_components import gauge_section
from components.ui.unit_ui_components import graph_section
from cloud.anedya_cloud import Anedya
def draw_unit_2_dashboard():
    anedya= Anedya()
    node_id= st.session_state.nodesId["node_2"]
    node=anedya.new_node(st.session_state.anedya_client, nodeId=node_id)
    device_status_res=node.get_deviceStatus()
    unit_header("Phloton Unit 2",device_status_res=device_status_res)

    unit_details()

    gauge_data_list=[0,0,0,0,0]
    unit_battery_soc_res=node.get_latestData("temperature")
    if unit_battery_soc_res.get("isSuccess") and unit_battery_soc_res.get("data") is not None:
        unit_battery_soc=unit_battery_soc_res.get("data")
        gauge_data_list[0]=unit_battery_soc
    battery_voltage_res=node.get_latestData("temperature")
    if battery_voltage_res.get("isSuccess") and battery_voltage_res.get("data") is not None:    
        battery_voltage=battery_voltage_res.get("data")
        gauge_data_list[1]=battery_voltage
    flask_temperature_res=node.get_latestData("temperature")
    if flask_temperature_res.get("isSuccess") and flask_temperature_res.get("data") is not None:
        flask_temperature=flask_temperature_res.get("data")
        gauge_data_list[2]=flask_temperature
    ambient_temperature_res=node.get_latestData("temperature")
    if ambient_temperature_res.get("isSuccess") and ambient_temperature_res.get("data") is not None:
        ambient_temperature=ambient_temperature_res.get("data")
        gauge_data_list[3]=ambient_temperature
        ambient_temperature=ambient_temperature_res.get("timestamp")
        gauge_data_list[4]=ambient_temperature
    gauge_section(gauge_data_list)
    
    graph_section()

draw_unit_2_dashboard()