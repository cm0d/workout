import streamlit as st
import datetime

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Function to estimate daily calorie needs
def calculate_calories(age, weight, height, activity_level, gender):
    if gender == "Male":
        bmr = 88.36 + (13.4 * weight) + (4.8 * height * 100) - (5.7 * age)
    else:
        bmr = 447.6 + (9.2 * weight) + (3.1 * height * 100) - (4.3 * age)
    
    activity_multipliers = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725,
        "Super Active": 1.9
    }
    
    return bmr * activity_multipliers[activity_level]

# Function to calculate water intake
def calculate_water_intake(weight):
    return weight * 0.033  # Recommended daily water intake in liters

# Streamlit App
st.title("IMAGINE ZYN & Fitness Tracker")

st.sidebar.header("User Information")
name = st.sidebar.text_input("Enter your name:")
age = st.sidebar.number_input("Age", min_value=10, max_value=100, value=25)
weight = st.sidebar.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
height = st.sidebar.number_input("Height (m)", min_value=1.0, max_value=2.5, value=1.75)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
activity_level = st.sidebar.selectbox("Activity Level", 
                                      ["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Super Active"])

if st.sidebar.button("Calculate"):
    bmi = calculate_bmi(weight, height)
    calorie_needs = calculate_calories(age, weight, height, activity_level, gender)
    water_needs = calculate_water_intake(weight)

    st.subheader(f"👤 {name}'s Health Summary")
    
    st.write(f"💡 **BMI**: {bmi:.2f}")
    if bmi < 18.5:
        st.write("🔵 Underweight")
    elif 18.5 <= bmi < 24.9:
        st.write("🟢 Normal weight")
    elif 25 <= bmi < 29.9:
        st.write("🟠 Overweight")
    else:
        st.write("🔴 Obese")

    st.write(f"🔥 **Daily Calorie Requirement**: {calorie_needs:.2f} kcal")
    st.write(f"💧 **Recommended Daily Water Intake**: {water_needs:.2f} liters")

st.markdown("---")

### Zyn Usage Tracker
st.header("🚬 Zyn Usage Tracker")

# Load previous data from session state
if "zyn_usage" not in st.session_state:
    st.session_state.zyn_usage = []

st.subheader("Track Your Nicotine Pouch Usage")

today = datetime.date.today()
pouches_used = st.number_input(f"Zyn pouches used today ({today}):", min_value=0, max_value=50, value=0)

if st.button("Log Zyn Usage"):
    st.session_state.zyn_usage.append((today, pouches_used))
    st.success(f"Logged {pouches_used} pouches for {today}")

# Display Usage History
if st.session_state.zyn_usage:
    st.subheader("📊 Zyn Usage History")
    for date, usage in st.session_state.zyn_usage:
        st.write(f"📅 {date}: {usage} pouches used")

st.markdown("📌 *Track your health, manage nicotine intake, and stay fit!* 🚀")

