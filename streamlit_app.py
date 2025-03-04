import streamlit as st
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="Terp Calculator", page_icon="💪", layout="wide")

# --- CSS (Tesla-Style Full Page + Left Menu) ---
st.markdown("""
    <style>
        /* Layout */
        .main-container { display: flex; height: 100vh; }
        .sidebar { width: 300px; background: #111; padding: 40px; color: white; }
        .content { flex-grow: 1; padding: 40px; }
        /* Sidebar Styling */
        .sidebar h1 { font-size: 32px; margin-bottom: 20px; }
        .sidebar p { font-size: 16px; color: #999; }
        /* Content Styling */
        h1 { text-align: center; font-size: 50px; color: white; font-weight: bold; margin-bottom: 10px; }
        .question { font-size: 24px; font-weight: 500; text-align: center; padding: 20px; background: rgba(255, 255, 255, 0.1); border-radius: 12px; box-shadow: 0px 4px 12px rgba(255, 255, 255, 0.1); margin-bottom: 20px; }
        /* Progress Bar */
        .progress-container { width: 100%; height: 6px; background: rgba(255, 255, 255, 0.2); border-radius: 10px; margin-bottom: 20px; }
        .progress-bar { height: 100%; background: white; width: 0%; transition: width 0.4s ease-in-out; }
        /* Buttons */
        .stButton>button { width: 100%; padding: 14px; border-radius: 10px; background: white; color: black; font-size: 18px; font-weight: bold; border: none; transition: all 0.3s ease-in-out; }
        .stButton>button:hover { background: rgba(255, 255, 255, 0.2); color: white; transform: scale(1.05); }
    </style>
""", unsafe_allow_html=True)

# --- QUESTIONS ---
questions = [
    "Are you gay?",
    "Do you like jews?",
    "Are you black?",
    "Do you have a Kamala butt plug?",
    "Are you vegan?",
    "Do you HODL?",
    "Do you own plats?",
    "Do you like 2007 Camrys?",
    "Have you ever been to a Stadie Wedding?",
    "Do you owe Mantis money?"
]

# --- SESSION STATE (Track Progress) ---
if "question_index" not in st.session_state:
    st.session_state.question_index = 0

# --- LAYOUT (Two-Column Full Width) ---
col1, col2 = st.columns([1, 3])

# --- LEFT SIDEBAR MENU ---
with col1:
    st.markdown("<div class='sidebar'>", unsafe_allow_html=True)
    st.markdown("<h1>TERP CALCULATOR</h1>", unsafe_allow_html=True)
    st.markdown("<p>Find out if you're a real Terp.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- MAIN CONTENT (Centered Questions) ---
with col2:
    progress_percentage = int((st.session_state.question_index / len(questions)) * 100)
    
    # Progress Bar
    st.markdown(
        f"""
        <div class="progress-container">
            <div class="progress-bar" style="width: {progress_percentage}%;"></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Display Question One at a Time
    if st.session_state.question_index < len(questions):
        current_question = questions[st.session_state.question_index]
        st.markdown(f"<div class='question'>{current_question}</div>", unsafe_allow_html=True)
        
        # Answer Buttons
        if st.button("Yes ✅"):
            st.session_state.question_index += 1
            time.sleep(0.3)  # Smooth transition effect
            st.rerun()
        elif st.button("No ❌"):  # <-- Fixed the missing quote here
            st.session_state.question_index += 1
            time.sleep(0.3)  # Smooth transition effect
            st.rerun()
    else:
        # Final Result
        st.snow()  # 🎉 Fun effect for results
        st.markdown("<h1 style='text-align: center;'>RESULT:</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: white;'>You're a REAL TERP. 🏋️‍♂️🔥</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 18px; color: #A0A0A0;'>Time to hit the gym and eat more steak.</p>", unsafe_allow_html=True)
