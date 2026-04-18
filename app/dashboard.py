import sys
import os

# ✅ Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd

from src.data_loader import generate_climate_data
from src.preprocessing import preprocess
from src.anomaly_detection import detect_anomalies
from src.forecasting import forecast_temperature
from src.visualization import plot_temperature, plot_anomalies

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Climate Trend Analyzer", layout="wide")

# -------------------- CUSTOM STYLE --------------------
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🌍 Climate Trend Analyzer</h1>
    <p style='text-align: center;'>Analyze climate patterns, detect anomalies & forecast future trends</p>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------
st.sidebar.title("⚙️ Controls")
days = st.sidebar.slider("Select Data Size (Days)", 365, 365*10, 365*5)

st.sidebar.markdown("---")
st.sidebar.info("Built using Python, Streamlit & Prophet")

# -------------------- DATA PIPELINE --------------------
df = generate_climate_data(days)
df = preprocess(df)
df = detect_anomalies(df)

# -------------------- METRICS --------------------
st.markdown("## 📊 Key Insights")

col1, col2, col3 = st.columns(3)

col1.metric("🌡 Avg Temp", f"{df['temperature'].mean():.2f} °C")
col2.metric("🌧 Avg Rainfall", f"{df['rainfall'].mean():.2f} mm")
col3.metric("⚠️ Anomalies", f"{df['anomaly'].sum()}")

st.markdown("---")

# -------------------- DATA TABLE --------------------
st.markdown("## 📄 Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

# -------------------- DOWNLOAD BUTTONS --------------------
st.markdown("## ⬇️ Download Data")

csv_full = df.to_csv(index=False).encode('utf-8')
csv_anomaly = df[df['anomaly'] == 1].to_csv(index=False).encode('utf-8')

col1, col2 = st.columns(2)

with col1:
    st.download_button(
        "📥 Download Full Data",
        csv_full,
        "full_climate_data.csv",
        "text/csv"
    )

with col2:
    st.download_button(
        "⚠️ Download Anomalies Only",
        csv_anomaly,
        "anomalies.csv",
        "text/csv"
    )

# -------------------- GRAPHS --------------------
st.markdown("## 📈 Climate Analysis")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🌡 Temperature Trend")
    fig1 = plot_temperature(df)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.markdown("### ⚠️ Anomaly Detection")
    fig2 = plot_anomalies(df)
    st.plotly_chart(fig2, use_container_width=True)

# -------------------- FORECAST --------------------
st.markdown("## 🔮 Forecast (Next 1 Year)")

with st.spinner("Running forecasting model..."):
    model, forecast = forecast_temperature(df)

forecast_df = forecast[['ds', 'yhat']].set_index('ds')

st.line_chart(forecast_df)

# -------------------- FOOTER --------------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center;'>Made with ❤️ using Python, Streamlit & Machine Learning</p>",
    unsafe_allow_html=True
)