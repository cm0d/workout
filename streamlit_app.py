import streamlit as st
import pandas as pd
import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Zyn & Gym Tracker", page_icon="💪", layout="centered")

# --- STYLING (Tesla/Apple-Inspired) ---
st.markdown("""
    <style>
        /* Global Styles */
        body { background-color: #0E0E0E; color: #EAEAEA; font-family: 'Helvetica Neue', sans-serif; }
        .container { max-width: 600px; margin: auto; padding: 40px; }
        h1 { text-align: center; font-size: 48px; font-weight: 600; color: white; margin-bottom: 20px; }
        h3 { text-align: center; font-size: 20px; font-weight: 300; color: #A0A0A0; margin-bottom: 30px; }
        .stButton>button { width: 100%; padding: 14px; border-radius: 10px; background: white; color: black; font-size: 18px; font-weight: 500; transition: all 0.3s ease-in-out; }
        .stButton>button:hover { background: rgba(255, 255, 255, 0.2); color: white; transform: scale(1.05); }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE (STORING DATA) ---
if "zyn_data" not in st.session_state:
    st.session_state.zyn_data = pd.DataFrame(columns=["Date", "Pouches Used"])

if "gym_data" not in st.session_state:
    st.session_state.gym_data = pd.DataFrame(columns=["Date", "Workout Intensity", "Muscle Soreness"])

# --- TITLE ---
st.markdown("<h1>Zyn & Gym Tracker</h1>", unsafe_allow_html=True)
st.markdown("<h3>Optimize your nicotine & fitness balance</h3>", unsafe_allow_html=True)

# --- ZYN TRACKER ---
st.subheader("💨 Zyn Usage Log")
today = datetime.date.today()
pouches_used = st.slider("How many Zyn pouches today?", 0, 20, 2)

if st.button("Log Zyn Usage"):
    new_entry = pd.DataFrame({"Date": [today], "Pouches Used": [pouches_used]})
    st.session_state.zyn_data = pd.concat([st.session_state.zyn_data, new_entry], ignore_index=True)
    st.success(f"Logged {pouches_used} Zyn pouches for {today}!")

# Show Zyn Usage Data
if not st.session_state.zyn_data.empty:
    st.subheader("📊 Zyn Usage History")
    st.dataframe(st.session_state.zyn_data.sort_values("Date", ascending=False))

# --- GYM STRAIN TRACKER ---
st.subheader("💪 Gym Strain Tracker")
workout_intensity = st.slider("How intense was your workout? (1-10)", 1, 10, 5)
muscle_soreness = st.slider("How sore do you feel? (1-10)", 1, 10, 5)

if st.button("Log Workout Strain"):
    new_gym_entry = pd.DataFrame({"Date": [today], "Workout Intensity": [workout_intensity], "Muscle Soreness": [muscle_soreness]})
    st.session_state.gym_data = pd.concat([st.session_state.gym_data, new_gym_entry], ignore_index=True)
    st.success(f"Logged workout intensity: {workout_intensity}, soreness: {muscle_soreness} for {today}!")

# Show Gym Strain Data
if not st.session_state.gym_data.empty:
    st.subheader("📊 Workout History")
    st.dataframe(st.session_state.gym_data.sort_values("Date", ascending=False))

# --- RECOMMENDATION SYSTEM ---
st.subheader("🧠 Smart Insights")
if not st.session_state.zyn_data.empty and not st.session_state.gym_data.empty:
    avg_zyn = st.session_state.zyn_data["Pouches Used"].mean()
    avg_soreness = st.session_state.gym_data["Muscle Soreness"].mean()
    
    if avg_zyn > 5:
        st.warning("⚠️ You're using a high amount of Zyn! Consider reducing for better recovery.")
    else:
        st.success("✅ Your Zyn usage is within a balanced range.")

    if avg_soreness > 7:
        st.warning("⚠️ You're experiencing high muscle soreness! Consider adding rest or more hydration.")
    else:
        st.success("✅ Your recovery levels look great!")

st.markdown("<p style='text-align: center; font-size: 14px; color: #A0A0A0;'>Stay balanced, stay strong.</p>", unsafe_allow_html=True)
