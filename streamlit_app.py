import streamlit as st
import random

# Define pride colors
pride_colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#8B00FF"]

# Fun questions to ask
questions = [
    "Do you enjoy a good brunch?",
    "Have you ever sung along to a Beyoncé song?",
    "Do you use emojis in your texts?",
    "Have you ever binge-watched RuPaul’s Drag Race?",
    "Do you know what 'yas queen' means?",
    "Have you ever called a friend 'girl' unironically?",
    "Do you like musicals?",
    "Is Lady Gaga an icon?",
    "Have you ever worn something just because it looked fabulous?",
    "Do you have a favorite Mariah Carey song?"
]

# Set up Streamlit layout
st.set_page_config(page_title="Zach's Gaydar", page_icon="🏳️‍🌈", layout="centered")

# Title with rainbow effect
st.markdown("<h1 style='text-align: center; font-size: 50px;'>🌈 AM I GAY? 🌈</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Answer these 10 questions and we'll tell you the truth!</h3>", unsafe_allow_html=True)

# Create a form
with st.form("gaydar_quiz"):
    answers = []
    for i, question in enumerate(questions):
        color = pride_colors[i % len(pride_colors)]  # Cycle through pride colors
        st.markdown(f"<h4 style='color: {color};'>{question}</h4>", unsafe_allow_html=True)
        answers.append(st.radio(f"Question {i+1}", ["Yes", "No"], index=random.choice([0, 1])))

    # Submit button
    submitted = st.form_submit_button("Get My Results 🏳️‍🌈")

# Show results
if submitted:
    st.balloons()
    st.markdown("<h2 style='text-align: center; color: #8B00FF;'>🎉 Surprise! 🎉</h2>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 40px; color: #FF0000;'>You're Gay! 🏳️‍🌈</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px;'>Don't fight it, just embrace it. Welcome to the club! 💖💜💙</p>", unsafe_allow_html=True)
