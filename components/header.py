import streamlit as st

def render_header():
    st.markdown("""
    <div class="custom-header" style="text-align: center; margin-bottom: 30px;">
        <h1 style="
            font-size: 3.5rem; 
            font-weight: 800;
            background: -webkit-linear-gradient(0deg, #00C9FF, #92FE9D); 
            -webkit-background-clip: text; 
            -webkit-text-fill-color: transparent;
            margin-bottom: 0px;
            font-family: 'Rajdhani', sans-serif;">
            MAGIC CHESS AI
        </h1>
        <p style="
            font-size: 1.2rem; 
            font-style: italic; 
            color: #b0c4de; 
            margin-top: -10px;
            letter-spacing: 1px;">
            "Dominasi Land of Dawn dengan Strategi Data"
        </p>
    </div>
    """, unsafe_allow_html=True)