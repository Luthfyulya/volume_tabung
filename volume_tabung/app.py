import streamlit as st
import math

def hitung_volume_tabung(jari_jari, tinggi):
    """
    Menghitung volume tabung berdasarkan jari-jari dan tinggi.
    """
    luas_alas = math.pi * (jari_jari ** 2)
    volume = luas_alas * tinggi
    return luas_alas, volume

# --- Konfigurasi Halaman Streamlit ---
st.set_page_config(
    page_title="Kalkulator Volume Tabung",
    page_icon=" cylindrical_roman_temple", # Icon untuk tab browser
    layout="centered", # Layout halaman bisa wide atau centered
    initial_sidebar_state="expanded" # Sidebar defaultnya terbuka
)

# --- Judul dan Deskripsi ---
st.title(" 🧪 Kalkulator Volume Tabung Interaktif")
st.markdown("---")
st.write("""
Aplikasi ini akan membantu Anda menghitung volume tabung dengan mudah.
Cukup masukkan nilai **jari-jari** dan **tinggi** tabung, lalu lihat hasilnya!
""")

# --- Input Pengguna ---
st.header("Masukkan Dimensi Tabung")

# Menggunakan kolom untuk tata letak yang lebih baik
col1, col2 = st.columns(2)

with col1:
    jari_jari = st.number_input(
        "**Jari-jari (r)**",
        min_value=0.0,
        value=5.0,
        step=0.1,
        help="Jarak dari pusat lingkaran ke tepi alas tabung."
    )

with col2:
    tinggi = st.number_input(
        "**Tinggi (t)**",
        min_value=0.0,
        value=10.0,
        step=0.1,
        help="Jarak vertikal dari alas ke tutup tabung."
    )

st.markdown("---")

# --- Tombol Hitung ---
if st.button("🚀 Hitung Volume!"):
    if jari_jari <= 0 or tinggi <= 0:
        st.error("Jari-jari dan tinggi harus lebih besar dari nol.")
    else:
        luas_alas, volume = hitung_volume_tabung(jari_jari, tinggi)

        st.success("🎉 Hasil Perhitungan!")

        # Menampilkan langkah-langkah perhitungan dengan warna
        st.subheader("Detail Perhitungan:")
        st.info(f"**Langkah 1: Hitung Luas Alas**")
        st.code(f"Rumus Luas Alas = π * r²")
        st.markdown(f"Luas Alas = `{math.pi:.4f}` * `{jari_jari}`² = `{luas_alas:.2f}`")

        st.info(f"**Langkah 2: Hitung Volume Tabung**")
        st.code(f"Rumus Volume = Luas Alas * Tinggi")
        st.markdown(f"Volume = `{luas_alas:.2f}` * `{tinggi}` = **`{volume:.2f}`**")

        st.balloons() # Efek balon saat hasil muncul

        st.markdown(f"""
        <div style="background-color:#e0ffe0; padding: 15px; border-radius: 10px; border: 2px solid #66bb6a;">
            <h3 style="color:#2e7d32;">Kesimpulan:</h3>
            <p style="font-size:18px;">
                Volume tabung dengan jari-jari <b>{jari_jari}</b> dan tinggi <b>{tinggi}</b> adalah
                <b style="color:#c62828; font-size:20px;">{volume:.2f}</b> satuan kubik.
            </p>
            <p style="font-size:14px; color:#555;">
                *Pastikan satuan volume sesuai dengan satuan input Anda (misal cm³ jika menggunakan cm).*
            </p>
        </div>
        """, unsafe_allow_html=True)

# --- Sidebar (untuk informasi tambahan atau riwayat) ---
st.sidebar.title("ℹ️ Tentang Aplikasi Ini")
st.sidebar.info(
    "Aplikasi ini dibuat menggunakan Streamlit untuk demonstrasi kalkulator volume tabung. "
    "Dirancang agar interaktif dan mudah dipahami. "
)
st.sidebar.markdown("---")
st.sidebar.text("© 2025 Python Programmer")
