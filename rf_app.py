import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("rf_energy_model.pkl")

st.title("⚡ Energy Consumption Prediction (Random Forest)")

st.write("Provide input values:")

# Time features
year = st.number_input("Year", min_value=2000, max_value=2100, value=2024)
month = st.slider("Month", 1, 12)
day = st.slider("Day", 1, 31)
day_of_week = st.slider("Day of Week (0=Mon, 6=Sun)", 0, 6)
hour = st.slider("Hour", 0, 23)

# Lag features (renamed for clarity)
st.subheader("Previous Consumption Values")

lag_1 = st.number_input("Last Hour Consumption (MW)")
lag_24 = st.number_input("Same Hour Yesterday (MW)")
lag_168 = st.number_input("Same Hour Last Week (MW)")

# Rolling features (renamed)
st.subheader("Trend Features")

rolling_mean_24 = st.number_input("24-Hour Average Consumption (MW)")
rolling_mean_168 = st.number_input("7-Day Average Consumption (MW)")

# Combine features (IMPORTANT: order must match training)
features = np.array([[ 
    year, month, day, day_of_week, hour,
    lag_1, lag_24, lag_168,
    rolling_mean_24, rolling_mean_168
]])

# Predict
if st.button("Predict"):
    prediction = model.predict(features)
    st.success(f"Predicted Energy Consumption: {prediction[0]:.2f} MW")