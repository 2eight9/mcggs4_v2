import streamlit as st
import os

def show_home():
    # --- HERO SECTION ---
    # Membuka container tengah
    st.markdown("""
<div style="padding-top: 20px; text-align: center;">
""", unsafe_allow_html=True)
    
    # 1. LOGO (Pengganti Judul Teks)
    col_h1, col_h2, col_h3 = st.columns([1.5, 2, 1.5])
    with col_h2:
        # Menggunakan logo yang sama dengan about agar konsisten
        logo_path = "assets/images/logo_about.png" 
        if os.path.exists(logo_path):
            st.image(logo_path, use_container_width=True)
    
    # 2. SUBJUDUL / TAGLINE (Tanpa Judul Besar Lagi)
    # HTML Rata Kiri Mentok
    st.markdown("""
<div style="margin-top: 10px;"> <p class="hero-subtitle" style="margin-bottom: 40px;">
        Dominasi Land of Dawn dengan Kekuatan <span style="color: #00C9FF; font-weight:bold; text-shadow: 0 0 10px rgba(0,201,255,0.6);">Data Science</span>.
        <br>
        <small style="color: #64748b;">Season 4 • GoGo Commander • XGBoost Engine</small>
    </p>
</div>
</div> """, unsafe_allow_html=True)
    
    # --- KARTU FITUR ---
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
<div class="floating-card">
    <h1 style="font-size: 3.5rem; margin:0;">🤖</h1>
    <h3 style="color:white; margin-top:10px;">AI Core</h3>
    <p style="color:#94a3b8; font-size:0.9rem;">
        Otak cerdas yang dilatih dengan ribuan data match Mythic.
    </p>
</div>
""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
<div class="floating-card" style="animation-delay: 1s;"> 
    <h1 style="font-size: 3.5rem; margin:0;">📊</h1>
    <h3 style="color:white; margin-top:10px;">Deep Stats</h3>
    <p style="color:#94a3b8; font-size:0.9rem;">
        Analisis mendalam terhadap kombinasi Sinergi terkuat.
    </p>
</div>
""", unsafe_allow_html=True)

    with col3:
        st.markdown("""
<div class="floating-card" style="animation-delay: 2s;">
    <h1 style="font-size: 3.5rem; margin:0;">⚡</h1>
    <h3 style="color:white; margin-top:10px;">Real-Time</h3>
    <p style="color:#94a3b8; font-size:0.9rem;">
        Prediksi Win Rate instan dalam hitungan milidetik.
    </p>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.info("💡 **Tips Pro:** Masuk ke menu **'Prediksi AI'** di sidebar kiri untuk memulai!")