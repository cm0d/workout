import streamlit as st
import random

# Set up Streamlit layout
st.set_page_config(page_title="Zach's Gaydar", page_icon="🏳️‍🌈", layout="wide")

# Custom CSS for Apple/Tesla-inspired modern UI
st.markdown(
    """
    <style>
        body {
            background-color: #0E0E0E;
            color: #EAEAEA;
            font-family: 'SF Pro Display', sans-serif;
        }
        .main {
            background: rgba(255, 255, 255, 0.05);
            padding: 20px;
            border-radius: 16px;
            box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
            backdrop-filter: blur(12px);
        }
        .question-card {
            background: rgba(255, 255, 255, 0.08);
            padding: 15px;
            border-radius: 12px;
            margin-bottom: 12px;
            box-shadow: 0px 2px 8px rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease-in-out;
        }
        .question-card:hover {
            transform: translateY(-2px);
            box-shadow: 0px 4px 12px rgba(255, 255, 255, 0.15);
        }
        h1 {
            text-align: center;
            font-size: 48px;
            color: white;
            font-weight: 600;
            letter-spacing: -1px;
        }
        h3 {
            text-align: center;
            font-size: 24px;
            font-weight: 300;
            color: #B0B0B0;
        }
        .stButton>button {
            width: 100%;
            padding: 14px;
            border-radius: 10px;
            background: linear-gradient(90deg, #333, #111);
            color: white;
            font-size: 18px;
            font-weight: 500;
            border: none;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            background: linear-gradient(90deg, #111, #333);
            box-shadow: 0px 4px 12px rgba(255, 255, 255, 0.15);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with modern typography
st.markdown("<h1>AM I GAY?</h1>", unsafe_allow_html=True)
st.markdown("<h3>Answer 10 fun questions to find out.</h3>", unsafe_allow_html=True)

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
        submitted = st.form_submit_button("Get My Results 🏳️‍🌈")

# Show results
if submitted:
    st.snow()  # 🎉 Subtle animation effect
    st.markdown("<h2 style='text-align: center; color: #EAEAEA;'>🎉 The Results Are In! 🎉</h2>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 40px; color: #FFFFFF;'>You're Gay.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px; color: #B0B0B0;'>Embrace it. Live it. Love it.</p>", unsafe_allow_html=True)
