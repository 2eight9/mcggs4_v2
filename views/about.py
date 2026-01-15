import streamlit as st
import os

def show_about():
    # --- LOGO & JUDUL ---
    col_h1, col_h2, col_h3 = st.columns([1, 2, 1])
    with col_h2:
        logo_path = "assets/images/logo_about.png"
        if os.path.exists(logo_path):
            st.image(logo_path, use_container_width=True)
    
    st.markdown("<h2 style='text-align: center; color: #00C9FF; margin-top: 10px; margin-bottom: 30px; text-transform: uppercase; letter-spacing: 3px;'>Database Project</h2>", unsafe_allow_html=True)

    # --- BAGIAN 1: DESKRIPSI ---
    html_desc = """<div style="background: linear-gradient(135deg, rgba(15, 23, 42, 0.9) 0%, rgba(30, 41, 59, 0.9) 100%); border: 1px solid rgba(255,255,255,0.1); border-left: 5px solid #00C9FF; padding: 30px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0, 201, 255, 0.15); margin-bottom: 20px;"><h3 style="color: white; margin-top: 0; font-family: sans-serif; letter-spacing: 1px;">♟️ MAGIC CHESS AI PREDICTOR S4</h3><p style="color: #cbd5e1; text-align: justify; line-height: 1.8; font-size: 1rem; margin-top: 15px;">Aplikasi ini adalah <b>Sistem Pendukung Keputusan (SPK)</b> berbasis kecerdasan buatan (<i>Artificial Intelligence</i>) yang dirancang untuk menganalisis meta permainan. Project ini membantu pemain menentukan strategi terbaik dengan memprediksi peluang kemenangan (<i>Win Rate</i>) secara <b>Real-Time</b> menggunakan algoritma Machine Learning mutakhir.</p></div>"""
    st.markdown(html_desc, unsafe_allow_html=True)

    # --- BAGIAN 2: KELEBIHAN & KEKURANGAN ---
    html_pros = """<div style="display: flex; flex-wrap: wrap; gap: 20px; margin-bottom: 30px;"><div style="flex: 1; min-width: 250px; background: rgba(6, 78, 59, 0.3); border: 1px solid #065f46; padding: 20px; border-radius: 12px;"><h4 style="color: #4ade80; margin-top:0; margin-bottom: 15px; border-bottom: 1px solid #065f46; padding-bottom: 10px;">✅ SYSTEM ADVANTAGE</h4><ul style="color: #d1fae5; font-size: 0.9rem; padding-left: 20px; line-height: 1.6;"><li><b>High Accuracy:</b> Dilatih dengan ribuan data Mythic.</li><li><b>Dual-Engine:</b> Random Forest + XGBoost.</li><li><b>Instant Logic:</b> Prediksi dalam milidetik.</li></ul></div><div style="flex: 1; min-width: 250px; background: rgba(127, 29, 29, 0.3); border: 1px solid #991b1b; padding: 20px; border-radius: 12px;"><h4 style="color: #f87171; margin-top:0; margin-bottom: 15px; border-bottom: 1px solid #991b1b; padding-bottom: 10px;">⚠️ SYSTEM LIMITATION</h4><ul style="color: #fee2e2; font-size: 0.9rem; padding-left: 20px; line-height: 1.6;"><li><b>Data Dependency:</b> Bergantung pada update dataset Season.</li><li><b>Meta Shift:</b> Perlu retrain saat ada Patch Note baru.</li><li><b>RNG Factor:</b> Tidak memprediksi faktor hoki in-game.</li></ul></div></div>"""
    st.markdown(html_pros, unsafe_allow_html=True)

    # --- BAGIAN 3: PROFIL DEVELOPER ---
    html_profile = """<div style="background: rgba(15, 23, 42, 0.8); border: 1px solid #334155; padding: 25px; border-radius: 15px; display: flex; align-items: center; gap: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.3);"><div style="font-size: 3rem;">👨‍💻</div><div style="width: 100%;"><h4 style="color: #94a3b8; margin: 0; text-transform: uppercase; font-size: 0.8rem; letter-spacing: 1px;">Lead Developer</h4><h2 style="margin: 5px 0; color: #00C9FF; text-transform: uppercase; letter-spacing: 1px;">APRILIANO BOIMAU</h2><div style="border-top: 1px solid #334155; margin-top: 10px; padding-top: 10px; display: flex; justify-content: space-between; flex-wrap: wrap; color: #cbd5e1; font-size: 0.9rem;"><span>📍 SoE (Kobelete), TTS, NTT</span><span>🎓 Universitas Amikom Yogyakarta</span></div></div></div>"""
    st.markdown(html_profile, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- TEKNOLOGI (IKON DIKEMBALIKAN DISINI) ---
    st.markdown("<h3 style='text-align:center; color:white; margin-bottom: 15px; opacity: 0.7;'>POWERED BY</h3>", unsafe_allow_html=True)
    
    # Perhatikan bagian <a ...> di bawah ini sudah ada emoji-nya lagi
    html_tech = """<style>.tech-badge-large {display: inline-block; padding: 10px 20px; margin: 5px;background: rgba(30, 41, 59, 0.5); border: 1px solid #334155;border-radius: 8px; color: #94a3b8 !important; text-decoration: none;font-weight: 600; font-size: 0.9rem; transition: all 0.3s ease;}.tech-badge-large:hover {background: #00C9FF; color: black !important;border-color: #00C9FF; box-shadow: 0 0 15px rgba(0, 201, 255, 0.5); transform: translateY(-2px);}</style><div style="text-align: center; display: flex; flex-wrap: wrap; justify-content: center;"><a href="#" class="tech-badge-large">🐍 Python 3.10</a><a href="#" class="tech-badge-large">👑 Streamlit</a><a href="#" class="tech-badge-large">🐼 Pandas</a><a href="#" class="tech-badge-large">🤖 Scikit-Learn</a><a href="#" class="tech-badge-large">🚀 XGBoost</a><a href="#" class="tech-badge-large">🎨 Custom CSS3</a></div>"""
    st.markdown(html_tech, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)