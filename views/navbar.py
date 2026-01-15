import streamlit as st
from streamlit_option_menu import option_menu

def create_navbar():
    with st.sidebar:
        st.markdown("<h1 style='text-align:center; color:#00C9FF; margin-bottom:0;'>MCGG AI</h1>", unsafe_allow_html=True)
        st.caption("Magic Chess Predictor S4")
        st.markdown("---")
        
        # OPSI MENU NAVIGASI
        selected = option_menu(
            menu_title=None, 
            options=["Home", "Prediksi AI", "About", "Contact"], 
            icons=["house-fill", "cpu-fill", "info-circle-fill", "envelope-fill"], 
            menu_icon="cast", 
            default_index=0,
            orientation="vertical",
            styles={
                # 1. Container menu kita paksa HITAM (#000000)
                "container": {"padding": "0!important", "background-color": "#000000"},
                
                # 2. Ikon berwarna Cyan
                "icon": {"color": "#00C9FF", "font-size": "20px"}, 
                
                # 3. Teks menu kita paksa Putih & Background Hitam
                "nav-link": {
                    "font-size": "16px", 
                    "text-align": "left", 
                    "margin": "5px", 
                    "color": "white",
                    "background-color": "#000000",
                },
                
                # 4. Warna saat menu dipilih (Cyan dengan teks Hitam)
                "nav-link-selected": {
                    "background-color": "#00C9FF", 
                    "color": "black",
                    "font-weight": "bold"
                },
            }
        )
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        return selected