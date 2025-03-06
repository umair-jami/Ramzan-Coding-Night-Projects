import random
import string
import streamlit as st
import pyperclip

def generate_password(length=12):
    """Generate a random password of specified length with at least one number and one special character."""
    if length < 6:
        raise ValueError("Password length must be at least 6 characters.")
    
    numbers = random.choice(string.digits)
    special_chars = random.choice(string.punctuation)
    letters = [random.choice(string.ascii_letters) for _ in range(length - 2)]
    
    password_list = list(numbers + special_chars + ''.join(letters))
    random.shuffle(password_list)
    
    return ''.join(password_list)

# Streamlit UI
st.title("🔑 Password Generator")

length = st.number_input("Enter password length:", min_value=6, max_value=100, value=12)

if st.button("Generate Password"):
    password = generate_password(length)
    st.session_state["password"] = password  # Store password in session state
    st.text_input("Generated Password:", password, key="password_display", disabled=True)

if "password" in st.session_state and st.button("Copy Password"):
    pyperclip.copy(st.session_state["password"])
    st.success("Password copied to clipboard!")
