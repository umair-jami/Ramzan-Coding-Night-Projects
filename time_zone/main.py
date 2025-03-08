import streamlit as st
from datetime import datetime, time
from zoneinfo import ZoneInfo


TIME_ZONES =[
    "UTC",
    "Asia/Karachi",
    "Asia/Tokyo",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Asia/Dubai",
    "Asia/Kolkata"
]
st.title("Time Zone App")
selected_time_zone=st.multiselect("Select Time Zones",TIME_ZONES,default=["UTC","Asia/Karachi"])

st.header("Selected Time Zones")
for tz in selected_time_zone:
    current_time=datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.subheader(f"**{tz}**: {current_time}")
    
st.subheader("Convert Time Between Time Zones")
time_now_str = st.text_input("Current Time (HH:MM AM/PM)", value=datetime.now().strftime("%I:%M %p"))
from_tz=st.selectbox("From Time Zone",TIME_ZONES,index=0)
to_tz=st.selectbox("To Time Zone",TIME_ZONES,index=1)

if st.button("Convert Time"):
    try:
        time_now = datetime.strptime(time_now_str, "%I:%M %p").time()
        dt = datetime.combine(datetime.today(), time_now).replace(tzinfo=ZoneInfo(from_tz))
        converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
        st.success(f"Converted Time: {converted_time}")
    except ValueError:
        st.error("Invalid time format. Please use HH:MM AM/PM format.")