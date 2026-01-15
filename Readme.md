<div style="text-align: center;">
<!-- LOGO PROJECT -->
<img src="assets/images/logo_about.png" alt="Logo Project" width="200">

<h1 style="border-bottom: none;">♟️ Magic Chess AI Predictor (V2)</h1>

<p>
<b>Sistem Pendukung Keputusan (SPK) Berbasis Machine Learning untuk Prediksi Kemenangan Mobile Legends</b>
</p>

<!-- BADGES -->

<a href="https://streamlit.io/">
<img src="https://img.shields.io/badge/Streamlit-v1.31-FF4B4B?style=flat&logo=streamlit&logoColor=white" alt="Streamlit">
</a>
<a href="https://www.python.org/">
<img src="https://img.shields.io/badge/Python-3.10-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
</a>
<a href="https://xgboost.readthedocs.io/">
<img src="https://img.shields.io/badge/Model-XGBoost-orange?style=flat&logo=xgboost&logoColor=white" alt="XGBoost">
</a>
<a href="#">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Version-2.0_Upgrade-blue%3Fstyle%3Dflat" alt="Version">
</a>





<!-- TOMBOL LIVE DEMO -->

<a href="https://mcggai-v2.streamlit.app/">
<img src="https://img.shields.io/badge/🚀_COBA_APLIKASI_SEKARANG_(LIVE_DEMO)-00C9FF?style=for-the-badge&logo=appveyor" alt="Live Demo">
</a>







</div>

🚀 Versi Upgrade (V2.0)

Aplikasi ini merupakan versi pengembangan yang telah dioptimasi untuk performa dan pengalaman pengguna:

🎨 Visual Overhaul: Antarmuka modern dengan tema Cyberpunk dan efek glassmorphism.

📈 Better Algorithm: Implementasi model XGBoost yang lebih stabil untuk prediksi kemenangan.

📱 Mobile Responsive: Tata letak yang adaptif untuk penggunaan di perangkat seluler.

⚡ Fast Loading: Animasi Lottie dimuat dari direktori lokal untuk efisiensi data dan kecepatan akses.

📖 Tentang Proyek

Magic Chess AI Predictor adalah aplikasi berbasis web yang dirancang untuk membantu pemain Magic Chess (Mobile Legends) menganalisis kekuatan strategi mereka. Sistem ini memberikan estimasi peluang kemenangan (Win Rate) secara real-time berdasarkan data historis pertandingan rank tinggi.

⭐ Fitur Utama

🔮 Prediksi Real-Time: Simulasi kemenangan berdasarkan kombinasi Commander dan sinergi aktif.

⚡ Offline Mode Ready: Aset animasi Lottie tersimpan secara lokal sehingga aplikasi tetap ringan dan cepat.

📊 Analisis Visual: Visualisasi data kekuatan strategi yang intuitif bagi pemain.

⚖️ Analisis Sistem

✅ Kelebihan

Responsif: Hasil prediksi muncul secara instan tanpa proses loading yang lama.

Akurasi Optimal: Menggunakan algoritma XGBoost yang unggul dalam menangani variabel data yang kompleks.

Kemudahan Penggunaan: Antarmuka yang simpel memudahkan input data strategi pemain.

⚠️ Kekurangan

Dinamika Meta: Akurasi dapat dipengaruhi oleh pembaruan game (Buff/Nerf) dari pengembang resmi.

Variabel RNG: Tidak dapat memperhitungkan faktor keberuntungan dalam game seperti Item Drop.

🛠️ Teknologi yang Digunakan

Bahasa Pemrograman: Python 3.10

Framework Web: Streamlit

Machine Learning: Scikit-Learn, XGBoost, Joblib

Pengolahan Data: Pandas, NumPy

Aset Visual: Streamlit-Lottie, CSS3 Custom Style

💻 Instalasi Lokal

Silakan ikuti instruksi di bawah ini untuk menjalankan aplikasi di lingkungan lokal Anda:

1. Clone Repository

git clone [https://github.com/2eight9/mcggs4_v2.git](https://github.com/2eight9/mcggs4_v2.git)
cd mcggs4_v2


2. Install Library

Pastikan Anda sudah menginstal Python, kemudian jalankan:

pip install -r requirements.txt


3. Jalankan Aplikasi

streamlit run app.py


📂 Struktur Folder

mcggs4_v2/
├── 📂 assets/              # Aset statis (Gambar, CSS, Animasi)
│   ├── 📂 animations/      # File JSON animasi Lottie
│   ├── 📂 css/             # Custom styling aplikasi
│   └── 📂 images/          # Logo dan aset visual commander
├── 📂 models/              # Penyimpanan model AI terkompresi
├── 📂 views/               # Modul halaman (Home, Prediction, About)
├── 📜 app.py               # File utama aplikasi (Streamlit Entry)
├── 📜 utils.py             # Fungsi bantuan & logika pemrosesan
├── 📜 requirements.txt     # Daftar dependensi library
└── 📜 README.md            # Dokumentasi proyek


<div style="text-align: center;">
<small>Dikembangkan dengan ❤️ oleh <b>Apriliano Boimau</b></small>
</div>