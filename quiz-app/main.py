import streamlit as st
import random
import time

st.title("📝 Quiz Application")

questions = [
    {
        "question": "Who is the founder of Pakistan?",
        "options": ["Allama Iqbal", "Liaquat Ali Khan", "Quaid-e-Azam", "Sir Syed Ahmed Khan"],
        "answer": "Quaid-e-Azam"
    },
    {
        "question": "What is the national language of Pakistan?",
        "options": ["Punjabi", "Pashto", "Urdu", "Sindhi"],
        "answer": "Urdu"
    },
    {
        "question": "Which city is known as the 'City of Lights'?",
        "options": ["Lahore", "Karachi", "Islamabad", "Quetta"],
        "answer": "Karachi"
    },
    {
        "question": "What is the national sport of Pakistan?",
        "options": ["Cricket", "Hockey", "Football", "Kabaddi"],
        "answer": "Hockey"
    },
    {
        "question": "Who wrote the national anthem of Pakistan?",
        "options": ["Faiz Ahmed Faiz", "Hafeez Jalandhari", "Allama Iqbal", "Ahmed Faraz"],
        "answer": "Hafeez Jalandhari"
    },
    {
        "question": "Which is the largest province of Pakistan by area?",
        "options": ["Punjab", "Sindh", "Balochistan", "Khyber Pakhtunkhwa"],
        "answer": "Balochistan"
    },
    {
        "question": "Which year did Pakistan conduct nuclear tests?",
        "options": ["1995", "1998", "2000", "2002"],
        "answer": "1998"
    },
    {
        "question": "What is the name of the highest peak in Pakistan?",
        "options": ["Nanga Parbat", "Rakaposhi", "K2", "Broad Peak"],
        "answer": "K2"
    },
    {
        "question": "Who was the first Prime Minister of Pakistan?",
        "options": ["Benazir Bhutto", "Liaquat Ali Khan", "Zulfiqar Ali Bhutto", "Ayub Khan"],
        "answer": "Liaquat Ali Khan"
    },
    {
        "question": "Which Pakistani scientist won the Nobel Prize in Physics?",
        "options": ["Dr. Abdul Qadeer Khan", "Abdus Salam", "Dr. Samar Mubarakmand", "Pervez Hoodbhoy"],
        "answer": "Abdus Salam"
    }
]

if "current_question" not in st.session_state:
    st.session_state.current_question=random.choice(questions)

question=st.session_state.current_question
st.subheader(question["question"])
selected_option=st.radio("Select an option",question["options"])
if st.button("Submit Answer"):
    if selected_option==question["answer"]:
        st.success("Correct Answer! 🎉")
    else:
        st.error("Wrong Answer! 😢")
    st.session_state.current_question=random.choice(questions)
    time.sleep(2)  # Wait for 2 seconds before showing the next question
    st.rerun()  # Rerun the app to show the next question