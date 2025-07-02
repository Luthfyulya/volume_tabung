import streamlit as st
import math

st.set_page_config(page_title="🧮Kalkulator Volume Tabung", layout="centered", icon=" cilindro.png") # Added icon

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        background-color: #F0F2F6;
        padding: 20px;
        border-radius: 10px;
    }
    .stApp {
        background-color: #e6f2ff; /* Light blue background for the whole app */
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #45a049;
        transform: translateY(-2px);
    }
    .stNumberInput>div>div>input {
        background-color: #FFFFFF;
        border: 2px solid #2196F3;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
    }
    .stSuccess {
        background-color: #e6ffe6;
        color: #1a531a;
        border-left: 6px solid #4CAF50;
        padding: 10px;
        border-radius: 5px;
        font-size: 18px;
        font-weight: bold;
    }
    .stWarning {
        background-color: #fff3e6;
        color: #b35900;
        border-left: 6px solid #FF9800;
        padding: 10px;
        border-radius: 5px;
        font-size: 16px;
    }
    h1 {
        color: #2196F3;
        text-align: center;
        font-family: 'Arial Black', Gadget, sans-serif;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    .stMarkdown {
        text-align: center;
        font-size: 18px;
        color: #333333;
    }
</style>
""", unsafe_allow_html=True)

st.title("📏 Kalkulator Volume Tabung 🧪") # Added more emojis

st.markdown("---") # Separator
st.markdown("### Masukkan dimensi tabung Anda di bawah ini untuk menghitung volumenya!")

# Layout with columns for better organization
col1, col2 = st.columns(2)

with col1:
    jari_jari = st.number_input("Masukkan Jari-jari alas (cm)", min_value=0.0, format="%.2f", help="Ukuran dari pusat lingkaran alas ke tepi.")

with col2:
    tinggi = st.number_input("Masukkan Tinggi tabung (cm)", min_value=0.0, format="%.2f", help="Ukuran vertikal tabung dari alas ke tutup.")

st.markdown("---") # Separator

# Centering the button
col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
with col_btn2:
    if st.button("Hitung Volume"):
        if jari_jari > 0 and tinggi > 0:
            volume = math.pi * jari_jari**2 * tinggi
            st.success(f"🎉 **Volume tabung adalah: {volume:.2f} cm³**")
            st.balloons() # Fun animation
        else:
            st.warning("⚠️ **Mohon masukkan nilai jari-jari dan tinggi yang valid (harus lebih dari 0).**")

st.markdown("---")
st.markdown("Dibuat oleh Luthfy-Arum-Rifqi. Selamat menghitung!")
