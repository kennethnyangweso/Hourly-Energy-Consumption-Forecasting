import streamlit as st
import numpy as np
import pandas as pd
import pickle
from tensorflow.keras.models import load_model
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Energy Forecasting Dashboard", layout="wide")

# -----------------------------
# Load Model and Scaler (1-feature)
# -----------------------------
model = load_model("bilstm_energy_forecast.h5", compile=False)

with open("scaler_bilstm.pkl", "rb") as f:  # NOTE: 1-feature scaler
    scaler = pickle.load(f)

# -----------------------------
# Title & Description
# -----------------------------
st.title("⚡ Hourly Energy Consumption Forecasting Dashboard")
st.write("""
This dashboard predicts **the next hour energy consumption** using a **BiLSTM deep learning model**.
The model is trained on the **last 24 hours of energy consumption (MW)**.
""")

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("energy_dataset_cleaned.csv")

st.subheader("Last 24 Hours of Energy Consumption")
last_24 = df['energy_consumption(MW)'].values[-24:]
st.line_chart(last_24)

# -----------------------------
# Prediction Button
# -----------------------------
if st.sidebar.button("Predict Next Hour Energy Consumption"):

    # Scale last 24 values (reshape for scaler)
    last_24_scaled = scaler.transform(last_24.reshape(-1,1))

    # Reshape for BiLSTM: (1 sample, 24 timesteps, 1 feature)
    X_input = last_24_scaled.reshape((1, 24, 1))

    # Predict
    prediction_scaled = model.predict(X_input)

    # Convert back to original scale
    prediction_actual = scaler.inverse_transform(prediction_scaled)

    st.subheader("Prediction Result")
    st.success(f"⚡ Predicted Energy Consumption (Next Hour): {prediction_actual[0][0]:.2f} MW")

# -----------------------------
# Example Visualization Section
# -----------------------------
st.subheader("Energy Consumption Trend (Demo)")
data = pd.DataFrame({
    "hour": list(range(24)),
    "energy_consumption": np.random.uniform(3000, 6000, 24)
})
fig = px.line(
    data,
    x="hour",
    y="energy_consumption",
    title="Hourly Energy Consumption Pattern"
)
st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Model Feature Info
# -----------------------------
st.subheader("Model Features Used")
st.write(["energy_consumption(MW) (last 24 hours sequence)"])

# Footer
st.markdown("---")
st.write("Built with Streamlit and BiLSTM Deep Learning")