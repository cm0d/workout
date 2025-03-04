import streamlit as st
import random

# Set up Streamlit layout
st.set_page_config(page_title="Zach's Gaydar", page_icon="🏳️‍🌈", layout="centered")

# Custom CSS for Tesla-Inspired UI
st.markdown(
    """
    <style>
        /* General Styles */
        body {
            background-color: #000000;
            color: #EAEAEA;
            font-family: 'Helvetica Neue', sans-serif;
        }
        .main-container {
            max-width: 600px;
            margin: auto;
            padding: 40px;
        }
        /* Title Styling */
        h1 {
            text-align: center;
            font-size: 54px;
            font-weight: 600;
            color: white;
            margin-bottom: 10px;
        }
        h3 {
            text-align: center;
            font-size: 22px;
            font-weight: 300;
            color: #A0A0A0;
            margin-bottom: 30px;
        }
        /* Question Cards */
        .question-card {
            background: rgba(255, 255, 255, 0.08);
            padding: 18px;
            border-radius: 10px;
            margin-bottom: 16px;
            transition: all 0.3s ease-in-out;
            box-shadow: 0px 4px 12px rgba(255, 255, 255, 0.05);
        }
        .question-card:hover {
            transform: translateY(-2px);
            box-shadow: 0px 8px 16px rgba(255, 255, 255, 0.08);
        }
        /* Button Styling */
        .stButton>button {
            width: 100%;
            padding: 16px;
            border-radius: 8px;
            background: #111111;
            color: white;
            font-size: 20px;
            font-weight: 500;
            border: 2px solid white;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background: white;
            color: black;
            border: 2px solid white;
            transform: scale(1.05);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Tesla-Style Layout
with st.container():
    st.markdown("<h1>AM I GAY?</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Answer 10 simple questions to find out.</h3>", unsafe_allow_html=True)

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

# Centered layout
with st.container():
    with st.form("gaydar_quiz"):
        answers = []
        for i, question in enumerate(questions):
            st.markdown(f"<div class='question-card'><h4>{question}</h4></div>", unsafe_allow_html=True)
            answers.append(st.radio(f"Question {i+1}", ["Yes", "No"], index=random.choice([0, 1]), key=i))

        # Submit button
        submitted = st.form_submit_button("Get My Results")

# Show results
if submitted:
    st.snow()  # 🎉 Subtle animation effect
    st.markdown("<h2 style='text-align: center; color: #EAEAEA;'>🎉 The Results Are In! 🎉</h2>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 40px; color: #FFFFFF;'>You're Gay.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #A0A0A0;'>Embrace it. Live it. Love it.</p>", unsafe_allow_html=True)
