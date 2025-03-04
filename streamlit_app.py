import streamlit as st
import time

# Set up Streamlit layout
st.set_page_config(page_title="Zach's Gaydar", page_icon="🏳️‍🌈", layout="centered")

# Custom CSS for Tesla/Apple-inspired UI
st.markdown(
    """
    <style>
        /* Global Styles */
        body {
            background-color: #000000;
            color: #FFFFFF;
            font-family: 'Helvetica Neue', sans-serif;
        }
        .container {
            max-width: 600px;
            margin: auto;
            padding: 40px;
        }
        /* Title */
        h1 {
            text-align: center;
            font-size: 52px;
            font-weight: 600;
            color: white;
            margin-bottom: 20px;
        }
        /* Progress Bar */
        .progress-bar {
            width: 100%;
            height: 6px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            overflow: hidden;
            margin-bottom: 20px;
        }
        .progress-fill {
            height: 100%;
            background: white;
            width: 0%;
            transition: width 0.4s ease-in-out;
        }
        /* Question Styling */
        .question {
            font-size: 24px;
            font-weight: 500;
            text-align: center;
            padding: 20px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease-in-out;
        }
        /* Button */
        .stButton>button {
            width: 100%;
            padding: 16px;
            border-radius: 10px;
            background: white;
            color: black;
            font-size: 20px;
            font-weight: 500;
            border: none;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background: rgba(255, 255, 255, 0.2);
            color: white;
            transform: scale(1.05);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# NSFW Wild Questions
questions = [
    "Have you ever made out with someone of the same gender just for fun?",
    "Do you feel a weird excitement watching same-sex makeout scenes?",
    "Have you ever stared too long at someone of the same gender in the locker room?",
    "Ever had a wild thought about your best friend that you won’t admit?",
    "Do you get way too invested in reality TV drama?",
    "Have you ever used ‘it’s not gay if…’ as an excuse?",
    "Ever found yourself unintentionally flirting with a same-gender stranger?",
    "Do you know what ‘bussy’ means?",
    "Have you ever ‘accidentally’ ended up at a gay bar?",
    "Would you rather be trapped in an elevator with Timothée Chalamet or Megan Fox?",
]

# Track Question Number
if "question_index" not in st.session_state:
    st.session_state.question_index = 0

# Display Progress Bar
progress_percentage = int((st.session_state.question_index / len(questions)) * 100)
st.markdown(
    f"""
    <div class="progress-bar">
        <div class="progress-fill" style="width: {progress_percentage}%;"></div>
    </div>
    """,
    unsafe_allow_html=True
)

# Display Question One at a Time
if st.session_state.question_index < len(questions):
    current_question = questions[st.session_state.question_index]
    st.markdown(f"<div class='question'>{current_question}</div>", unsafe_allow_html=True)
    
    # Show Answer Buttons
    if st.button("Yes"):
        st.session_state.question_index += 1
        time.sleep(0.3)  # Smooth transition effect
        st.experimental_rerun()
    elif st.button("No"):
        st.session_state.question_index += 1
        time.sleep(0.3)  # Smooth transition effect
        st.experimental_rerun()
else:
    # Show Final Result
    st.snow()  # 🎉 Fun effect for results
    st.markdown("<h1 style='text-align: center;'>RESULT:</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: white;'>You're GAY. 😈🔥</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #A0A0A0;'>Congrats. It’s time to embrace it.</p>", unsafe_allow_html=True)
