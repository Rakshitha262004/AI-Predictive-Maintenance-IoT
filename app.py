import streamlit as st
import numpy as np
import joblib
import os

st.title("🔧 AI Predictive Maintenance System")

# Check if model exists
if not os.path.exists("models/model.pkl"):
    st.error("⚠️ Model not found! Please run main.py first.")
    st.stop()

model = joblib.load("models/model.pkl")

st.header("Enter Sensor Values")

air_temp = st.number_input("Air Temperature (K)", value=300.0)
process_temp = st.number_input("Process Temperature (K)", value=310.0)
speed = st.number_input("Rotational Speed (rpm)", value=1500)
torque = st.number_input("Torque (Nm)", value=40.0)
tool_wear = st.number_input("Tool Wear (min)", value=200)

type_option = st.selectbox("Machine Type", ["L", "M", "H"])

# One-hot encoding
type_L = 1 if type_option == "L" else 0
type_M = 1 if type_option == "M" else 0
type_H = 1 if type_option == "H" else 0

if st.button("Predict"):

    input_data = np.array([
        air_temp, process_temp, speed,
        torque, tool_wear,
        type_L, type_M, type_H
    ]).reshape(1, -1)

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Machine Failure Likely")
    else:
        st.success("✅ Machine is Healthy")