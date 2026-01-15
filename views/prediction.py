import streamlit as st
import pandas as pd
import time
import os
import json 
from streamlit_lottie import st_lottie 

# Import fungsi wajib dari utils
from utils import safe_transform, calculate_active_count, get_synergy_limits

# --- FUNGSI BACA FILE JSON DARI LAPTOP (OFFLINE) ---
def load_lottiefile(filepath):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def show_banner(image_path):
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        st.write("")

def show_prediction(model, le_comm, le_gogo, all_commanders):
    
    # --- 1. LOAD ANIMASI DARI FOLDER ASSETS ---
    # Python akan mencari file ini di laptop kamu
    lottie_win = load_lottiefile("assets/animations/win.json")
    lottie_lose = load_lottiefile("assets/animations/lose.json")

    limits = get_synergy_limits()

    # --- 2. JUDUL HALAMAN ---
    st.markdown("""
    <div style="text-align: center; padding-bottom: 20px;">
        <h1 class="hero-title" style="font-size: 3rem;">BATTLE SIMULATION</h1>
        <p style="color: #94a3b8; letter-spacing: 2px; text-transform: uppercase; font-size: 0.9rem;">
            Sistem Analisis Taktis v2.0 • <span style="color:#00C9FF;">Offline Mode</span>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    show_banner("assets/images/banner_top.png")

    # --- 3. INPUT COMMANDER ---
    st.markdown("""
    <div style="background: rgba(15, 23, 42, 0.6); padding: 15px; border-radius: 12px; border-left: 4px solid #00C9FF; margin-bottom: 20px;">
        <h3 style="margin:0; color:white; font-size: 1.2rem;">🟢 KONFIGURASI COMMANDER</h3>
        <p style="margin:0; color:#94a3b8; font-size: 0.85rem;">Pilih penguasa papan catur Anda.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<label style='color:#00C9FF; font-weight:bold; font-size:0.9rem;'>COMMANDER UTAMA</label>", unsafe_allow_html=True)
        selected_commander = st.selectbox("Pilih Hero", all_commanders, key="comm", label_visibility="collapsed")
        img_path = f"assets/images/commanders/{selected_commander.lower().replace(' ', '_')}.png"
        if os.path.exists(img_path): st.image(img_path, width=150)

    with col2:
        st.markdown("<label style='color:#00C9FF; font-weight:bold; font-size:0.9rem;'>GOGO COMMANDER</label>", unsafe_allow_html=True)
        selected_gogo = st.selectbox("Pilih Gogo", all_commanders, key="gogo", label_visibility="collapsed")
        img_path_gogo = f"assets/images/commanders/{selected_gogo.lower().replace(' ', '_')}.png"
        if os.path.exists(img_path_gogo): st.image(img_path_gogo, width=150)

    # --- 4. INPUT SINERGI ---
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background: rgba(15, 23, 42, 0.6); padding: 15px; border-radius: 12px; border-left: 4px solid #d946ef; margin-bottom: 10px;">
        <h3 style="margin:0; color:white; font-size: 1.2rem;">🟣 DATA SINERGI & ROLE</h3>
        <p style="margin:0; color:#94a3b8; font-size: 0.85rem;">Masukkan data sinergi aktif di papan.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🛠️  BUKA PANEL INPUT DETAIL", expanded=True):
        st.info("Masukkan jumlah hero. Status Tier akan muncul otomatis.")
        
        tab1, tab2 = st.tabs(["FACTIONS (RAS)", "ROLES (KELAS)"])
        input_data = {}
        
        # --- TAB FACTIONS ---
        with tab1:
            col_f1, col_f2 = st.columns(2)
            factions_list = [
                "KOF", "Soul Vessels", "Starwing", "Luminexus", "Aspirant", 
                "Toy Mischief", "Shadowcell", "Metro Zero", "Mortal Rival", 
                "Glory League", "Beyond the Clouds"
            ]
            
            for i, f in enumerate(factions_list):
                key = f.lower().replace(" ", "_")
                max_val = limits.get(key, 10)
                target_col = col_f1 if i < len(factions_list) // 2 else col_f2
                
                val = target_col.number_input(f, min_value=0, max_value=max_val, key=f"f_{key}")
                input_data[key] = val
                
                tier_aktif = calculate_active_count(val, key)
                if tier_aktif > 0:
                    target_col.markdown(f"<div style='background:#064e3b; color:#4ade80; padding:2px 8px; border-radius:4px; font-size:0.8rem; display:inline-block; margin-bottom:10px;'>✅ Aktif: Tier {tier_aktif}</div>", unsafe_allow_html=True)
                else:
                    target_col.markdown(f"<div style='color:#64748b; font-size:0.8rem; margin-bottom:10px;'>❌ Tidak Aktif</div>", unsafe_allow_html=True)

        # --- TAB ROLES ---
        with tab2:
            col_r1, col_r2 = st.columns(2)
            roles_list = [
                "Weapon Master", "Marksman", "Mage", "Defender", 
                "Bruiser", "Dauntless", "Stargazer", "Swiftblade", 
                "Phasewarper", "Scavenger"
            ]
            
            for i, r in enumerate(roles_list):
                key = r.lower().replace(" ", "_")
                max_val = limits.get(key, 10)
                target_col = col_r1 if i < len(roles_list) // 2 else col_r2
                
                val = target_col.number_input(r, min_value=0, max_value=max_val, key=f"r_{key}")
                input_data[key] = val
                
                tier_aktif = calculate_active_count(val, key)
                if tier_aktif > 0:
                    target_col.markdown(f"<div style='background:#064e3b; color:#4ade80; padding:2px 8px; border-radius:4px; font-size:0.8rem; display:inline-block; margin-bottom:10px;'>✅ Aktif: Tier {tier_aktif}</div>", unsafe_allow_html=True)
                else:
                    target_col.markdown(f"<div style='color:#64748b; font-size:0.8rem; margin-bottom:10px;'>❌ Tidak Aktif</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 5. LOGIKA TOMBOL & HASIL ---
    if st.button("JALANKAN SIMULASI PERTEMPURAN 🚀", use_container_width=True):
        
        with st.spinner('Menganalisis Strategi...'):
            time.sleep(0.5) # Cepat saja karena offline
            
            # Persiapan Data
            comm_val = safe_transform(le_comm, selected_commander)
            gogo_val = safe_transform(le_gogo, selected_gogo)
            
            active_tiers = {}
            for syn, raw_count in input_data.items():
                active_tiers[syn] = calculate_active_count(raw_count, syn)

            data_payload = {
                'commander_name': [comm_val],
                'gogo_comander': [gogo_val],
                'synergy_count_shadowcell': [active_tiers.get('shadowcell', 0)],
                'synergy_count_mortal_rival': [active_tiers.get('mortal_rival', 0)],
                'synergy_count_kof': [active_tiers.get('kof', 0)],
                'synergy_count_soul_vessels': [active_tiers.get('soul_vessels', 0)],
                'synergy_count_starwing': [active_tiers.get('starwing', 0)],
                'synergy_count_luminexus': [active_tiers.get('luminexus', 0)],
                'synergy_count_aspirant': [active_tiers.get('aspirant', 0)],
                'synergy_count_toy_mischief': [active_tiers.get('toy_mischief', 0)],
                'synergy_count_glory_league': [active_tiers.get('glory_league', 0)],
                'synergy_count_metro_zero': [active_tiers.get('metro_zero', 0)],
                'synergy_count_beyond_the_clouds': [active_tiers.get('beyond_the_clouds', 0)],
                'synergy_count_bruiser': [active_tiers.get('bruiser', 0)],
                'synergy_count_defender': [active_tiers.get('defender', 0)],
                'synergy_count_dauntless': [active_tiers.get('dauntless', 0)],
                'synergy_count_weapon_master': [active_tiers.get('weapon_master', 0)],
                'synergy_count_marksman': [active_tiers.get('marksman', 0)],
                'synergy_count_stargazer': [active_tiers.get('stargazer', 0)],
                'synergy_count_swiftblade': [active_tiers.get('swiftblade', 0)],
                'synergy_count_mage': [active_tiers.get('mage', 0)],
                'synergy_count_phasewarper': [active_tiers.get('phasewarper', 0)],
                'synergy_count_scavenger': [active_tiers.get('scavenger', 0)],
            }
            
            try:
                X_pred = pd.DataFrame(data_payload)
                prediction = model.predict(X_pred)[0]
                proba = model.predict_proba(X_pred)[0]
                win_prob = proba[1] * 100
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # --- TAMPILAN HASIL (ANIMASI LOKAL) ---
                col_res1, col_res2, col_res3 = st.columns([1, 2, 1])
                
                with col_res2:
                    if prediction == 1:
                        # === KONDISI MENANG ===
                        st.markdown(f"""
                        <div class="cyber-card" style="border-color: #4ade80; background: linear-gradient(145deg, rgba(6, 78, 59, 0.9), rgba(15, 23, 42, 0.9)); text-align: center;">
                            <h2 style="color: #4ade80; font-weight: 800; letter-spacing: 2px; margin-top: 0;">VICTORY PREDICTED</h2>
                            <h1 style="font-size: 3.5rem; color: white; margin: 10px 0;">{win_prob:.1f}%</h1>
                            <p style="color: #bbf7d0; font-size: 1.1rem;">Setup ini sangat potensial!</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Load Animasi Lokal
                        if lottie_win:
                            st_lottie(lottie_win, height=250, key="win_anim", quality="medium")
                        else:
                            st.warning("⚠️ File 'win.json' belum ditemukan di folder assets/animations")
                            
                    else:
                        # === KONDISI KALAH ===
                        st.markdown(f"""
                        <div class="cyber-card" style="border-color: #f87171; background: linear-gradient(145deg, rgba(127, 29, 29, 0.9), rgba(15, 23, 42, 0.9)); text-align: center;">
                            <h2 style="color: #f87171; font-weight: 800; letter-spacing: 2px; margin-top: 0;">DEFEAT RISK</h2>
                            <h1 style="font-size: 3.5rem; color: white; margin: 10px 0;">{win_prob:.1f}%</h1>
                            <p style="color: #fecaca; font-size: 1.1rem;">Strategi terlalu berisiko.</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Load Animasi Lokal
                        if lottie_lose:
                            st_lottie(lottie_lose, height=250, key="lose_anim", quality="medium")
                        else:
                            st.warning("⚠️ File 'lose.json' belum ditemukan di folder assets/animations")

            except Exception as e:
                st.error(f"Terjadi kesalahan teknis: {e}")