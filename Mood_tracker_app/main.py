import streamlit as st  # For web UI
import pandas as pd  # For data handling
import datetime  # For working with dates
import csv  # For reading/writing CSV files
import os  # For file operations

MOOD_FILE = "mood_log.csv"

# Function to load mood data safely
def load_mood_data():
    if not os.path.exists(MOOD_FILE) or os.stat(MOOD_FILE).st_size == 0:
        return pd.DataFrame(columns=["Date", "Mood"])  # Return empty DataFrame

    try:
        data = pd.read_csv(MOOD_FILE)
        if "Date" not in data.columns or "Mood" not in data.columns:
            return pd.DataFrame(columns=["Date", "Mood"])  # Return empty if headers are wrong
        return data
    except Exception:
        return pd.DataFrame(columns=["Date", "Mood"])  # Handle corrupted files safely

# Function to save mood data with proper headers
def save_mood_data(date, mood):
    file_exists = os.path.exists(MOOD_FILE)

    with open(MOOD_FILE, "a", newline="") as file:  
        writer = csv.writer(file)

        if not file_exists or os.stat(MOOD_FILE).st_size == 0:
            writer.writerow(["Date", "Mood"])  # Ensure headers exist

        writer.writerow([date, mood])

# Streamlit UI
st.title("Mood Tracker App 😊")

today = datetime.date.today()

st.subheader("How are you feeling today?")
mood = st.selectbox("Select mood", ["Happy", "Neutral", "Angry", "Sad"])

if st.button("Log Mood"):
    save_mood_data(today, mood)
    st.success("Mood Logged Successfully!")

# Load and display mood trends
data = load_mood_data()

if not data.empty:
    st.subheader("Mood Trends Over Time")

    # Ensure correct column formatting
    if "Date" in data.columns:
        data["Date"] = pd.to_datetime(data["Date"], errors="coerce")  # Convert with error handling

    # Count occurrences of each mood
    mood_counts = data["Mood"].value_counts()

    # Display bar chart
    st.bar_chart(mood_counts)
else:
    st.info("No mood data logged yet. Start logging your mood!")
