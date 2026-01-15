import streamlit as st
import os
from views import home, prediction, about, contact
from utils import load_model_assets, local_css, img_to_bytes 

# --- 1. SETUP HALAMAN ---
st.set_page_config(
    page_title="Magic Chess AI S4",
    page_icon="♟️",
    layout="wide",
    initial_sidebar_state="expanded"
)

local_css("assets/css/style.css")

# --- 2. LOAD ASSETS ---
model, le_comm, le_gogo = load_model_assets()
all_commanders = [
    "Aamon", "Angela", "Aurora", "Chou", "Cyclops", "Dyrroth", "Fanny", 
    "Guinevere", "Gusion", "Harley", "Johnson", "Kagura", "Karina", 
    "Lancelot", "Layla", "Ling", "Lukas", "Lunox", "Lylia", "Minotaur", 
    "Miya", "Moscov", "Nana", "Paquito", "Popol dan Kupa", "Vale", 
    "Valir", "Wanwan", "Yu Zhong", "Zilong"
]

# --- 3. SIDEBAR ---
with st.sidebar:
    # --- LOGO UTAMA (ATAS) ---
    logo_sidebar_path = "assets/images/logo_sidebar.png"
    if os.path.exists(logo_sidebar_path):
        st.image(logo_sidebar_path, use_container_width=True)
    else:
        st.markdown("<h1 style='text-align:center; color:#00C9FF;'>♟️ MC-AI</h1>", unsafe_allow_html=True)

    st.write("") 

    # --- MENU NAVIGASI ---
    selected = st.radio(
        "NAVIGATION MENU",
        ["Home", "Prediksi AI", "About", "Contact"], 
        index=0,
        label_visibility="collapsed"
    )

    st.markdown("---")
    
    # --- SYSTEM INFO (Tengah) ---
    st.markdown("""
    <div style="background: rgba(255,255,255,0.05); padding: 15px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.1); margin-bottom: 20px;">
        <div style="margin-bottom: 10px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 5px;">
            <span style="color: #94a3b8; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px;">System Info</span>
        </div>
        <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
            <span style="color: #cbd5e1; font-size: 0.9rem;">App Version:</span>
            <span style="color: #00C9FF; font-size: 0.9rem; font-weight: bold;">v2.0 (Reborn)</span>
        </div>
        <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
            <span style="color: #cbd5e1; font-size: 0.9rem;">Game Patch:</span>
            <span style="color: #fbbf24; font-size: 0.9rem;">v1.8.92</span> 
        </div>
        <div style="display: flex; justify-content: space-between;">
            <span style="color: #cbd5e1; font-size: 0.9rem;">Model Acc:</span>
            <span style="color: #4ade80; font-size: 0.9rem; font-weight: bold;">92.5%</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- LOGO KEDUA (PINDAHAN DARI FOOTER) ---
    # Kita taruh di sini agar terlihat jelas & besar
    footer_logo_path = "assets/images/logo_footer.png"
    
    if os.path.exists(footer_logo_path):
        st.markdown("<div style='text-align: center; margin-top: 10px;'>", unsafe_allow_html=True)
        st.image(footer_logo_path, width=120) # Ukuran bisa diatur (misal 100-150px)
        st.markdown("</div>", unsafe_allow_html=True)

# --- 4. KONTEN HALAMAN ---
if selected == "Home":
    home.show_home()
elif selected == "Prediksi AI":
    if model and le_comm and le_gogo:
        prediction.show_prediction(model, le_comm, le_gogo, all_commanders)
    else:
        st.error("⚠️ Model AI belum siap! Cek folder models.")
elif selected == "About":
    about.show_about()
elif selected == "Contact":
    contact.show_contact()

# --- 5. FOOTER (BERSIH - HANYA TEKS) ---
# Tidak ada lagi gambar logo di sini, jadi lebih rapi dan fokus ke copyright
st.markdown(f"""
<div class="fixed-footer">
    <div style="display: flex; align-items: center;">
        <span class="status-dot"></span> 
        SERVER: <b>ASIA (MYTHIC)</b>
    </div>
    <div style="display: flex; align-items: center; justify-content: center;">
        <span>COPYRIGHT © 2026 <b>APRILIANO BOIMAU</b></span>
    </div>
    <div style="width: 100px;"></div> 
</div>
""", unsafe_allow_html=True)