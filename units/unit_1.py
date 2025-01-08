import streamlit as st
from components.ui.unit_ui_components import unit_header
from components.ui.unit_ui_components import unit_details
from components.ui.unit_ui_components import gauge_section
from components.ui.unit_ui_components import graph_section
from components.ui.unit_ui_components import map_section
from cloud.anedya_cloud import Anedya

UNIT_NUMBER=1
def draw_unit_1_dashboard():
    
    anedya= Anedya()
    NODE_ID= st.session_state.nodesId[f"node_{UNIT_NUMBER}"]
    VARIABLES= st.session_state.variablesIdentifier

    node=None
    node=anedya.new_node(st.session_state.anedya_client, nodeId=NODE_ID)
    device_status_res=node.get_deviceStatus()
    unit_header(f"Phloton Unit {UNIT_NUMBER}",node_client=node,device_status_res=device_status_res)

    unit_details(node)

    gauge_data_list=[0,0,0,0,0]
    unit_battery_soc_res=node.get_latestData(VARIABLES["variable_1"].get("identifier"))
    if unit_battery_soc_res.get("isSuccess") and unit_battery_soc_res.get("data") is not None:
        unit_battery_soc=unit_battery_soc_res.get("data")
        gauge_data_list[0]=unit_battery_soc
    else:
        gauge_data_list[0]=-1
    battery_voltage_res=node.get_latestData(VARIABLES["variable_2"].get("identifier"))
    if battery_voltage_res.get("isSuccess") and battery_voltage_res.get("data") is not None:
        battery_voltage=battery_voltage_res.get("data")
        gauge_data_list[1]=battery_voltage
    else:
        gauge_data_list[1]=-1
    flask_temperature_res=node.get_latestData(VARIABLES["variable_3"].get("identifier"))
    if flask_temperature_res.get("isSuccess") and flask_temperature_res.get("data") is not None:
        flask_temperature=flask_temperature_res.get("data")
        gauge_data_list[2]=flask_temperature
    else:
        gauge_data_list[2]=-1
    ambient_temperature_res=node.get_latestData(VARIABLES["variable_4"].get("identifier"))
    if ambient_temperature_res.get("isSuccess") and ambient_temperature_res.get("data") is not None:
        ambient_temperature=ambient_temperature_res.get("data")
        gauge_data_list[3]=ambient_temperature
        ambient_temperature=ambient_temperature_res.get("timestamp")
        gauge_data_list[4]=ambient_temperature
    else:
        gauge_data_list[3]=-1
        gauge_data_list[4]=0
    gauge_section(gauge_data_list)
    
    graph_section(node)
    map_section(node)

draw_unit_1_dashboard()