import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")
def generate_money():
    return random.randint(1,1000)

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting Money...")
    time.sleep(2)
    st.success(f"Congratulations! You have generated ${generate_money()}")
    
def fetch_side_hustle():
    try:
        response=requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustle=response.json()
            return hustle["side_hustle"]
        else:
            return ("No side hustles available")
        
    except:
        return ("Failed to fetch side hustles")
    

    
st.subheader("Side Hustle Generator")
if st.button("Generate Hustle"):
    hustle=fetch_side_hustle()
    st.success(hustle)
    
def fetch_money_quote():
    try:
        response=requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            quote=response.json()
            return quote["money_quote"]
        else:
            return ("No money quotes available")
    except:
        return ("Failed to fetch money quotes")
st.subheader("Money Quote Generator")
if st.button("Generate Quote"):
    quote=fetch_money_quote()
    st.info(quote)