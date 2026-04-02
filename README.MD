# security-alert-project
# 🏴‍☠️ Team Pixel Pirates: Cloud Security & Threat Detection


Deployment link : https://security-alert-project-78d0.onrender.com/

## 🚀 Project Overview
Humne ek real-time **Cloud Security System** banaya hai jo suspicious activities ko detect karta hai aur admin ko alert karta hai.

### ✨ Key Features
- **Real-time Monitoring:** `logger.py` se logs generate hote hain.
- **Threat Detection:** `detector.py` critical threats ko identify karta hai.
- **AI Anomaly Detection:** `ai_bonus.py` use karta hai Machine Learning (Isolation Forest) outliers dhundne ke liye.
- **Dockerized:** Poora project Docker container mein chalta hai.

### 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** Scikit-Learn, Numpy
- **DevOps:** Docker, Git, Linux (WSL)

### 🏃 How to Run
1. Build Image: `docker build -t cloud-security-app .`
2. Run Container: `docker run cloud-security-app`
