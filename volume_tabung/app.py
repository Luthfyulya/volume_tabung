
import streamlit as st
import math

st.set_page_config(page_title="Kalkulator Volume Tabung", layout="centered")

st.title("🧮 Kalkulator Volume Tabung")

st.markdown("Masukkan jari-jari dan tinggi tabung untuk menghitung volumenya.")

# Input dari pengguna
jari_jari = st.number_input("Jari-jari alas (cm)", min_value=0.0, format="%.2f")
tinggi = st.number_input("Tinggi tabung (cm)", min_value=0.0, format="%.2f")

if st.button("Hitung Volume"):
    if jari_jari > 0 and tinggi > 0:
        volume = math.pi * jari_jari**2 * tinggi
        st.success(f"Volume tabung adalah **{volume:.2f} cm³**")
    else:
        st.warning("Masukkan nilai jari-jari dan tinggi yang lebih dari 0.")
