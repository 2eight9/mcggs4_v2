import streamlit as st

def show_contact():
    col1, col2, col3 = st.columns([1, 6, 1]) 
    
    with col2:
        st.markdown("<h2 style='text-align: center; color: #00C9FF;'>HUBUNGI DEVELOPER</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #94a3b8; margin-bottom: 30px;'>Kirim laporan bug atau saran pengembangan langsung ke markas.</p>", unsafe_allow_html=True)
        
        # --- LINK FORMSPREE ANDA ---
        formspree_endpoint = "https://formspree.io/f/xqeealwb" 
        
        contact_form = f"""
<form action="{formspree_endpoint}" method="POST">
<label style="color: #00C9FF; font-size: 0.9rem; font-weight: bold;">NAMA LENGKAP</label>
<input type="text" name="name" required placeholder="Masukkan nama Anda" style="width: 100%; padding: 12px; margin: 8px 0 20px 0; border: 1px solid #475569; border-radius: 8px; background-color: #1e293b; color: white; outline: none;">
<label style="color: #00C9FF; font-size: 0.9rem; font-weight: bold;">ALAMAT EMAIL</label>
<input type="email" name="email" required placeholder="email@contoh.com" style="width: 100%; padding: 12px; margin: 8px 0 20px 0; border: 1px solid #475569; border-radius: 8px; background-color: #1e293b; color: white; outline: none;">
<label style="color: #00C9FF; font-size: 0.9rem; font-weight: bold;">PESAN ANDA</label>
<textarea name="message" required placeholder="Tuliskan keluhan atau saran Anda di sini..." style="width: 100%; height: 120px; padding: 12px; margin: 8px 0 20px 0; border: 1px solid #475569; border-radius: 8px; background-color: #1e293b; color: white; outline: none; font-family: sans-serif;"></textarea>
<button type="submit" style="width: 100%; background: linear-gradient(90deg, #00C9FF, #0072ff); color: white; padding: 14px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 16px; transition: 0.3s; text-transform: uppercase; letter-spacing: 1px;">
KIRIM PESAN
</button>
</form>
"""
        st.markdown(contact_form, unsafe_allow_html=True)