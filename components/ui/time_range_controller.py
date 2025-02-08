import streamlit as st
import pytz
from datetime import date, datetime,timedelta,time


def auto_update_time_range(param_hold_or_start: bool = True):
    # st.session_state.counter=st.session_state.counter+1
    # st.write(st.session_state.counter)
    if param_hold_or_start:
        st.session_state.var_auto_update_time_range = True
    else:
        st.session_state.var_auto_update_time_range = False

def is_within_tolerance(time1, time2, tolerance=timedelta(seconds=60)):
    datetime1 = datetime.combine(date.min, time1)
    datetime2 = datetime.combine(date.min, time2)
    return abs((datetime1 - datetime2).total_seconds()) <= tolerance.total_seconds()


def get_default_time_range():
    
    # Get the current date and time in the Indian time zone
    indian_time_zone = pytz.timezone('Asia/Kolkata')
    current_date = datetime.now(indian_time_zone)

    # Extract the year, month, and day
    current_year = current_date.year
    current_month = current_date.month
    current_day = current_date.day
    # Create a date object
    current_date_object = date(current_year, current_month, current_day)
    # st.session_state.to_date = current_date_object

    # Extract the hour and minute
    hour = current_date.hour
    minute = current_date.minute
    # Create a time object
    current_time_object = time(hour, minute)
    # Assuming `st` is your Streamlit session state
    # st.session_state.to_time = current_time_object

    # Extract the year, month, and day
    reset_date = current_date - timedelta(hours=3.8)
    hour = reset_date.hour
    minute = reset_date.minute
    # Create a date object
    from_time_object = time(hour, minute)       
    # st.session_state.from_time = from_time_object
    
    # Subtract one day to get yesterday's date
    yesterday_date = current_date - timedelta(days=1)
    # Extract the year, month, and day
    yesterday_year = yesterday_date.year
    yesterday_month = yesterday_date.month
    yesterday_day = yesterday_date.day
    # Create a date object for yesterday
    yesterday_date_object = date(yesterday_year, yesterday_month, yesterday_day)
    # st.session_state.from_date = yesterday_date_object

    return[current_date_object, current_time_object, yesterday_date_object, from_time_object]

def reset_time_range():
    
    default_time_range=get_default_time_range()

    st.session_state.to_date = default_time_range[0]
    st.session_state.to_time = default_time_range[1]
    st.session_state.from_date = default_time_range[2]
    st.session_state.from_time = default_time_range[3]
    # st.write(st.session_state.to_date, st.session_state.to_time, st.session_state.from_date, st.session_state.from_time)
    # st.rerun()

st.cache_data(ttl=10, show_spinner=False)
def update_time_range():
    st.session_state.var_auto_update_time_range = True
    reset_time_range()
    return 0