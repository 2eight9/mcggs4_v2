<div style="text-align: center;">
  <img src="assets/images/logo_about.png" alt="Logo Magic Chess AI Predictor" width="150" height="150">
  <h1>Magic Chess AI Predictor (V2)</h1>
  <p>Sistem Pendukung Keputusan (SPK) untuk memprediksi peluang kemenangan (Win Rate) di game Magic Chess (Mobile Legends) berdasarkan kombinasi Commander dan Sinergi.</p>
</div>

<div style="text-align: center;">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/XGBoost-FF6B35?style=for-the-badge&logo=xgboost&logoColor=white" alt="XGBoost">
  <img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
</div>

<div style="text-align: center;">
  <a href="https://mcggai-v2.streamlit.app/">
    <img src="https://img.shields.io/badge/LIVE%20DEMO-FF6B35?style=for-the-badge&logo=streamlit&logoColor=white" alt="LIVE DEMO">
  </a>
</div>

## Tentang Proyek

Magic Chess AI Predictor (V2) adalah aplikasi berbasis kecerdasan buatan yang dirancang untuk membantu pemain Magic Chess dalam Mobile Legends membuat keputusan strategis. Dengan menggunakan algoritma XGBoost Classifier, aplikasi ini menganalisis kombinasi Commander dan Sinergi untuk memprediksi peluang kemenangan (Win Rate) secara akurat. Aplikasi ini dibangun dengan fokus pada pengalaman pengguna yang menarik melalui tema Cyberpunk dan elemen Glassmorphism, serta responsivitas penuh untuk perangkat mobile.

Proyek ini dikembangkan oleh Apriliano Boimau dan tersedia di [GitHub Repository](https://github.com/2eight9/mcggs4_v2.git).

## Fitur Unggulan

- **Prediksi Win Rate**: Analisis real-time berdasarkan kombinasi Commander dan Sinergi.
- **Antarmuka Cyberpunk**: Desain visual futuristik dengan efek Glassmorphism.
- **Responsif Mobile**: Optimasi penuh untuk perangkat seluler.
- **Animasi Offline Lottie**: Elemen interaktif tanpa koneksi internet.
- **Model Machine Learning**: Menggunakan XGBoost untuk akurasi tinggi.
- **Integrasi Streamlit**: Aplikasi web yang mudah diakses.

## Teknologi

Proyek ini dibangun menggunakan teknologi berikut:

- **Bahasa Pemrograman**: Python 3.10
- **Framework UI**: Streamlit
- **Library Data**: Pandas, NumPy
- **Machine Learning**: Scikit-Learn, XGBoost, Joblib
- **Styling**: Tema Cyberpunk dengan Glassmorphism

## Kelebihan & Kekurangan

### Kelebihan
- Akurasi prediksi tinggi berkat algoritma XGBoost.
- Antarmuka pengguna yang intuitif dan menarik secara visual.
- Responsif di berbagai perangkat, termasuk mobile.
- Tidak memerlukan koneksi internet untuk animasi dan fungsi dasar.
- Mudah diintegrasikan dan dikembangkan lebih lanjut.

### Kekurangan
- Terbatas pada data pelatihan yang tersedia; akurasi dapat bervariasi dengan pembaruan game.
- Membutuhkan sumber daya komputasi untuk model ML, meskipun ringan.
- Fokus pada kombinasi Commander dan Sinergi; tidak mencakup faktor eksternal seperti skill pemain.

## Instalasi Lokal

Untuk menjalankan aplikasi secara lokal, ikuti langkah-langkah berikut:

1. Pastikan Anda memiliki Python 3.10 atau versi lebih tinggi terinstal.
2. Buka terminal atau command prompt, lalu jalankan perintah berikut secara berurutan:

   ```bash
   git clone https://github.com/2eight9/mcggs4_v2.git
   cd mcggs4_v2
   pip install -r requirements.txt
   streamlit run app.py

## 📂 Struktur Proyek
```text
├── 📂 assets/                # Aset visual (Background, Logo, CSS kustom)
├── 📂 components/            # Komponen UI Modular (Header & Footer)
├── 📂 images/                # Galeri gambar Hero & Commander
├── 📂 views/                 # Manajemen halaman (Home, Prediction, About, Contact)
├── app.py                   # 🚀 Entry Point Utama Streamlit
├── utils.py                 # Logika Backend & Preprocessing Data
├── model_magic_chess_final.pkl # 🤖 Model AI Utama
├── encoder_commander_name.pkl  # Label Encoder untuk Commander
├── encoder_gogo_commander.pkl   # Label Encoder untuk Skill Gogo
├── requirements.txt         # Daftar Library Python
└── readme.md                # Dokumentasi Proyek



