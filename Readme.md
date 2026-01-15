<div align="center">
  <img src="assets/images/logo_about.png" alt="Logo Project" width="200">

  <h1 style="border-bottom: none;">♟️ Magic Chess AI Predictor (S4)</h1>

  <p>
    <b>Sistem Pendukung Keputusan (SPK) Berbasis Machine Learning untuk Prediksi Kemenangan Mobile Legends</b>
  </p>

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
    <img src="https://img.shields.io/badge/Status-Skripsi-green?style=flat" alt="Status">
  </a>

  <br><br>

  <a href="https://mcggai-v2.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀_COBA_APLIKASI_SEKARANG_(LIVE_DEMO)-00C9FF?style=for-the-badge&logo=appveyor" alt="Live Demo">
  </a>
  <br>
  <br>
</div>

---

## 📖 Tentang Proyek

**Magic Chess AI Predictor** adalah aplikasi web interaktif yang dirancang untuk membantu pemain *Magic Chess (Mobile Legends)* dalam menganalisis strategi mereka. Aplikasi ini menggunakan algoritma kecerdasan buatan (**XGBoost**) yang telah dilatih dengan ribuan data pertandingan rank Mythic untuk memprediksi persentase kemenangan (*Win Rate*) secara real-time.

Proyek ini dikembangkan sebagai **Tugas Akhir / Skripsi** Program Studi Informatika, Universitas Amikom Yogyakarta.

---

## ⭐ Fitur Utama

* 🔮 **Prediksi Real-Time:** Menghitung peluang menang berdasarkan kombinasi Commander, Level, dan Sinergi.
* ⚡ **Offline Mode Ready:** Menggunakan animasi lokal (Lottie Files) sehingga aplikasi tetap ringan dan cepat.
* 🎨 **Cyberpunk UI:** Antarmuka modern dengan tema gelap futuristik dan efek glassmorphism.
* 📊 **Analisis Data:** Menampilkan detail kekuatan sinergi aktif secara visual.

---

## ⚖️ Kelebihan & Kekurangan Sistem

### ✅ Kelebihan (Pros)
1.  **Akurasi Tinggi:** Menggunakan *Ensemble Learning* (XGBoost) yang terbukti lebih akurat dibanding Single Decision Tree.
2.  **Responsif & Cepat:** Optimasi *caching* membuat proses prediksi berjalan dalam hitungan milidetik.
3.  **User Friendly:** Desain antarmuka dibuat semudah mungkin untuk dipahami pemain awam sekalipun.
4.  **Tanpa Backend Rumit:** Dibangun sepenuhnya dengan Python (Streamlit), memudahkan maintenance.

### ⚠️ Kekurangan (Cons)
1.  **Ketergantungan Data Patch:** Akurasi prediksi sangat bergantung pada Meta game saat ini. Jika Mobile Legends melakukan update besar (Nerf/Buff), model AI perlu dilatih ulang.
2.  **Faktor RNG:** Sistem tidak dapat memprediksi faktor keberuntungan in-game seperti *Item Drop* atau *Critical Hit*.
3.  **Terbatas pada Sinergi:** Prediksi berfokus pada komposisi Sinergi & Commander.

---

## 🛠️ Teknologi yang Digunakan

* **Bahasa Pemrograman:** Python 3.10
* **Framework Web:** Streamlit
* **Machine Learning:** Scikit-Learn, XGBoost, Joblib
* **Pengolahan Data:** Pandas, NumPy
* **Visualisasi:** Streamlit-Lottie, CSS3 Custom

---

## 💻 Cara Menjalankan (Instalasi Lokal)

Jika Anda ingin menjalankan proyek ini di laptop Anda sendiri:

### 1. Clone Repository
```bash
git clone [https://github.com/2eight9/mcggs4_v2.git](https://github.com/2eight9/mcggs4_v2.git)
cd mcggs4_v2

### 3. Install Library
Install semua kebutuhan sistem yang ada di `requirements.txt`:

    pip install -r requirements.txt

### 4. Jalankan Aplikasi

    streamlit run app.py

Aplikasi akan otomatis terbuka di browser Anda di alamat `http://localhost:8501`.

---

## 📂 Struktur Folder

    magic-chess-ai/
    ├── 📂 assets/              # Aset statis
    │   ├── 📂 animations/      # File JSON animasi (Win/Lose)
    │   ├── 📂 css/             # File style.css untuk tampilan
    │   └── 📂 images/          # Logo dan gambar commander
    ├── 📂 models/              # File otak AI (.sav / .joblib)
    ├── 📂 views/               # Halaman menu (Home, Prediction, About)
    ├── 📜 app.py               # File utama aplikasi
    ├── 📜 utils.py             # Fungsi bantuan (Rumus & Encoder)
    ├── 📜 requirements.txt     # Daftar library wajib
    └── 📜 README.md            # Dokumentasi ini

