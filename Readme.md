<div style="text-align: center;">
  <img src="assets/images/logo_about.png" alt="Project Logo" width="180"/>

  <h1>Magic Chess AI Predictor (V2)</h1>

  <p>
    <b>Decision Support System Using Machine Learning<br/>
    for Magic Chess (Mobile Legends) Win Probability Prediction</b>
  </p>

  <a href="https://streamlit.io/">
    <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white"/>
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Language-Python_3.10-3776AB?style=flat&logo=python&logoColor=white"/>
  </a>
  <a href="https://xgboost.readthedocs.io/">
    <img src="https://img.shields.io/badge/Model-XGBoost-orange?style=flat"/>
  </a>
  <img src="https://img.shields.io/badge/Version-2.0-blue?style=flat"/>
</div>

---

## Project Overview

Magic Chess AI Predictor is a web-based Decision Support System (DSS) designed to assist Magic Chess (Mobile Legends) players in evaluating strategic decisions during gameplay.

The system applies Machine Learning techniques, specifically the XGBoost algorithm, to estimate the probability of winning based on:
- Commander selection
- Active synergies
- Team composition patterns

The model is trained using historical match data from high-rank gameplay.

---

## Version 2.0 Improvements

- Optimized XGBoost hyperparameters for better prediction stability
- Modern cyberpunk-inspired user interface
- Responsive layout for desktop and mobile devices
- Offline animation assets for improved performance

---

## Core Features

- Real-time win probability prediction
- Visual strategy analysis
- Lightweight and fast inference pipeline

---

## System Analysis

Advantages:
- Fast computation with minimal latency
- Robust ensemble learning model
- Simple and intuitive user workflow

Limitations:
- Dependent on current game meta
- Random in-game factors (RNG) not included

---

## Machine Learning Approach

Algorithm      : XGBoost  
Learning Type  : Supervised Learning (Classification)  
Input Features : Commander, synergy combinations  
Output         : Win probability score  
Model Storage  : Joblib  

---

## Technology Stack

Programming Language : Python 3.10  
Web Framework        : Streamlit  
Machine Learning     : XGBoost, Scikit-Learn  
Data Processing      : Pandas, NumPy  
UI & Styling         : CSS3, Streamlit-Lottie  

---

## Local Installation (Quick Start)

# 1. Clone Repository
git clone https://github.com/2eight9/mcggs4_v2.git
cd mcggs4_v2

# 2. Install Dependencies
pip install -r requirements.txt

# 3. Run Application
streamlit run app.py

---

## Project Structure

mcggs4_v2/
├── assets/
│   ├── animations/
│   ├── css/
│   └── images/
├── models/
├── views/
├── app.py
├── utils.py
├── requirements.txt
└── README.md

---

## Disclaimer

This project is developed for educational and research purposes only.  
Prediction results do not guarantee actual match outcomes.

---

## Author

Apriliano Ernando Benyamin Boimau 
Informatics Engineering Student  
