import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set halaman
st.set_page_config(page_title="Smart Farming Dashboard", layout="wide")

st.title("🌾 Smart Farming Sensor Dashboard")
st.write("Monitoring Yield Prediction & Sensor Data")

# Fungsi untuk memuat data dengan path yang benar
@st.cache_data
def load_data():
    # Menggunakan path relatif dari root repositori
    path = "outputs/cleaned_data.csv"
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        return None

df = load_data()

if df is not None:
    # 1. Metrik Sederhana (Gauge Meter Sim)
    col1, col2, col3 = st.columns(3)
    avg_temp = df['Average_Temperature'].mean()
    avg_hum = df['Average_Humidity'].mean()
    
    col1.metric("Avg Temperature", f"{avg_temp:.2f} °C")
    col2.metric("Avg Humidity", f"{avg_hum:.2f} %")
    
    # Alert System
    if avg_hum < 60:
        st.error("⚠️ ALERT: Kelembaban rata-rata rendah! Perlu irigasi tambahan.")
    else:
        st.success("✅ Kondisi Kelembaban Optimal.")

    # 2. Visualisasi Time Series
    st.subheader("📈 Tren Sensor (Time Series)")
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.lineplot(data=df.iloc[:50], x=df.index[:50], y='Average_Temperature', label='Temp')
    sns.lineplot(data=df.iloc[:50], x=df.index[:50], y='Average_Humidity', label='Humidity')
    plt.legend()
    st.pyplot(fig)

    # 3. Heatmap Korelasi
    st.subheader("🔥 Heatmap Korelasi Sensor")
    fig2, ax2 = plt.subplots()
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax2)
    st.pyplot(fig2)

else:
    st.error("File 'outputs/cleaned_data.csv' tidak ditemukan. Pastikan folder dan file sudah di-upload ke GitHub.")
