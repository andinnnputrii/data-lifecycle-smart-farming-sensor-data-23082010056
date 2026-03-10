
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🌱 Smart Farming Dashboard")
st.write("Monitoring Sensor IoT Pertanian 2026")

df = pd.read_csv('../outputs/cleaned_data.csv')
st.line_chart(df[['soil_moisture_%', 'temperature_C']].head(100))
st.write("Statistik Yield:", df['yield_kg_per_hectare'].describe())
