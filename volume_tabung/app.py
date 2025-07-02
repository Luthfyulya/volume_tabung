import streamlit as st
import math

# --- Konfigurasi Halaman Streamlit ---
st.set_page_config(
    page_title="Kalkulator Volume Tabung",
    layout="centered",
    initial_sidebar_state="collapsed",
    # Gunakan emoji sebagai ikon tab browser
    icon="📏"
)

# --- CSS Kustom untuk Tampilan Lebih Menarik ---
st.markdown("""
<style>
    /* Latar belakang aplikasi keseluruhan */
    .stApp {
        background-color: #f0f8ff; /* Warna biru muda pastel */
        color: #333333;
    }
    /* Kontainer utama aplikasi */
    .main .block-container {
        padding-top: 3rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 3rem;
    }
    /* Judul utama */
    h1 {
        color: #004d99; /* Biru gelap */
        text-align: center;
        font-family: 'Poppins', sans-serif;
        font-size: 2.8em;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 0.5em;
    }
    /* Sub-judul dan teks pendukung */
    .stMarkdown p {
        font-size: 1.1em;
        line-height: 1.6;
        text-align: center;
        color: #555555;
    }
    /* Input Angka */
    .stNumberInput div input {
        background-color: #ffffff;
        border: 2px solid #a8dadc; /* Biru kehijauan */
        border-radius: 10px;
        padding: 12px 15px;
        font-size: 1.1em;
        color: #333333;
        box-shadow: 1px 1px 3px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    .stNumberInput div input:focus {
        border-color: #457b9d; /* Biru lebih gelap saat fokus */
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }
    /* Tombol */
    .stButton > button {
        background-color: #2a9d8f; /* Hijau toska */
        color: white;
        font-size: 1.2em;
        padding: 12px 25px;
        border-radius: 10px;
        border: none;
        box-shadow: 3px 3px 6px rgba(0,0,0,0.2);
        transition: all 0.3s ease-in-out;
        cursor: pointer;
        font-weight: bold;
        width: 100%; /* Membuat tombol selebar kolom */
    }
    .stButton > button:hover {
        background-color: #218579; /* Hijau toska lebih gelap saat hover */
        transform: translateY(-2px);
        box-shadow: 4px 4px 8px rgba(0,0,0,0.3);
    }
    /* Pesan Sukses */
    .stSuccess {
        background-color: #d4edda; /* Hijau muda */
        color: #155724; /* Hijau gelap */
        border-left: 8px solid #28a745; /* Hijau cerah */
        padding: 15px;
        border-radius: 8px;
        font-size: 1.2em;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    /* Pesan Peringatan */
    .stWarning {
        background-color: #fff3cd; /* Kuning muda */
        color: #856404; /* Kuning gelap */
        border-left: 8px solid #ffc107; /* Kuning cerah */
        padding: 15px;
        border-radius: 8px;
        font-size: 1.1em;
        text-align: center;
        margin-top: 20px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    /* Gambar ilustrasi */
    .stImage {
        border-radius: 15px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.2);
        margin-bottom: 1.5em;
    }
    /* Footer */
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #cccccc;
        color: #777777;
        font-size: 0.9em;
    }
</style>
""", unsafe_allow_html=True)

# --- Konten Aplikasi ---

st.title("💡 Hitung Volume Tabung Bareng Yuk! 💡")

st.markdown("""
<p>Halo, para penjelajah matematika! 👋 Di sini, kita akan seru-seruan menghitung volume tabung.</p>
<p>Cukup masukkan berapa <strong>jari-jari</strong> alasnya dan <strong>tinggi</strong> tabungnya, nanti kita lihat hasilnya!</p>
""", unsafe_allow_html=True)

# Gambar ilustrasi tabung (gunakan URL gambar online atau local jika sudah di-deploy)
# Untuk deploy, sebaiknya gunakan gambar yang sudah ada di repo Anda atau URL online.
# Jika Anda punya gambar 'cylinder.png' di folder yang sama saat deploy, bisa gunakan:
# st.image("cylinder.png", caption="Ilustrasi Tabung", use_column_width=True)
# Contoh menggunakan URL gambar placeholder:
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Cylinder_3D.svg/1200px-Cylinder_3D.svg.png",
         caption="Ini dia bentuk tabung yang akan kita hitung volumenya!",
         use_column_width=True)

st.markdown("---") # Garis pemisah

st.markdown("### Masukkan Ukuran Tabungmu di Bawah Ini:")

# Input dari pengguna dengan kolom untuk tampilan yang rapi
col_jari_jari, col_tinggi = st.columns(2)

with col_jari_jari:
    jari_jari = st.number_input(
        "📏 Jari-jari Alas (cm)",
        min_value=0.0,
        format="%.2f",
        help="Jarak dari titik tengah alas tabung ke tepinya."
    )

with col_tinggi:
    tinggi = st.number_input(
        "📐 Tinggi Tabung (cm)",
        min_value=0.0,
        format="%.2f",
        help="Jarak dari alas ke tutup tabung."
    )

# Tombol untuk menghitung
st.markdown("---") # Garis pemisah
col_btn1, col_btn2, col_btn3 = st.columns([1,2,1]) # Kolom untuk menengahkan tombol

with col_btn2:
    if st.button("✨ Hitung Volume Sekarang! ✨"):
        if jari_jari > 0 and tinggi > 0:
            volume = math.pi * (jari_jari**2) * tinggi
            st.success(f"🥳 Wow! Volume tabungmu adalah **{volume:.2f} cm³**. Hebat!")
            st.balloons() # Efek balon yang menyenangkan
            st.snow()    # Efek salju untuk perayaan
        else:
            st.warning("🚨 Ups! Jari-jari dan Tinggi harus lebih besar dari nol. Coba lagi ya!")

st.markdown("---")
st.markdown("""
<div class="footer">
    Dibuat oleh Luthfy Arum Rifqi.
</div>
""", unsafe_allow_html=True)
