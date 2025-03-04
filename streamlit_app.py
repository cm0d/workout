import streamlit as st
import random

# Set up Streamlit layout
st.set_page_config(page_title="Zach's Gaydar", page_icon="🏳️‍🌈", layout="wide")

# Custom CSS for modern styling
st.markdown(
    """
    <style>
        body {
            background-color: #121212;
            color: white;
        }
        .main {
            background-color: #181818;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.1);
        }
        .question-card {
            background-color: #222;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 10px;
            box-shadow: 0px 2px 5px rgba(255, 255, 255, 0.1);
        }
        h1 {
            text-align: center;
            font-size: 50px;
            background: -webkit-linear-gradient(45deg, #ff0000, #ff9900, #ffff00, #33cc33, #3399ff, #9933ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .stButton>button {
            width: 100%;
            padding: 12px;
            border-radius: 8px;
            background: linear-gradient(90deg, #ff007f, #8B00FF);
            color: white;
            font-size: 18px;
            font-weight: bold;
            transition: 0.3s;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            background: linear-gradient(90deg, #8B00FF, #ff007f);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with a gradient effect
st.markdown("<h1>🌈 AM I GAY? 🌈</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Answer 10 fun questions to find out!</h3>", unsafe_allow_html=True)

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

# Pride Colors for each question
pride_colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#8B00FF"]

# Centered layout
with st.container():
    with st.form("gaydar_quiz"):
        answers = []
        for i, question in enumerate(questions):
            color = pride_colors[i % len(pride_colors)]  # Cycle through pride colors
            st.markdown(f"<div class='question-card'><h4 style='color: {color};'>{question}</h4></div>", unsafe_allow_html=True)
            answers.append(st.radio(f"Question {i+1}", ["Yes", "No"], index=random.choice([0, 1]), key=i))

        # Submit button
        submitted = st.form_submit_button("Get My Results 🏳️‍🌈")

# Show results
if submitted:
    st.snow()  # 🎉 Adds a fun confetti effect
    st.markdown("<h2 style='text-align: center; color: #8B00FF;'>🎉 Surprise! 🎉</h2>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 40px; color: #FF0000;'>You're Gay! 🏳️‍🌈</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px;'>Don't fight it, just embrace it. Welcome to the club! 💖💜💙</p>", unsafe_allow_html=True)
