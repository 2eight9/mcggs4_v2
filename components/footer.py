import streamlit as st
from datetime import datetime

def render_footer():
    year = datetime.now().year
    st.markdown(f"""
    <div class="custom-footer" style="
        text-align: center; 
        margin-top: 50px; 
        padding: 20px; 
        border-top: 1px solid rgba(255,255,255,0.1); 
        color: rgba(255,255,255,0.4); 
        font-size: 0.9rem;">
        <p>&copy; {year} Developed by <strong style="color: #00C9FF;">Apriliano Boimau</strong> | Magic Chess S4</p>
    </div>
    """, unsafe_allow_html=True)