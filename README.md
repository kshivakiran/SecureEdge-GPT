---
title: SecureEdge-GPT
emoji: 🛡️
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
pinned: false
---

# 🛡️ SecureEdge-GPT: Distributed Privacy-Preserving medical AI

**SecureEdge-GPT** is a state-of-the-art distributed model training system designed for the healthcare industry. It enables multiple hospitals to collaboratively train a **Medical Assistant AI** (Microsoft Phi-3) using real clinical transcripts without ever sharing patient data.

---

## 🎯 Project Aim
To solve the "Privacy vs. Intelligence" dilemma in healthcare. Hospitals have valuable data but cannot share it due to strict privacy laws (GDPR/HIPAA). This project uses **Federated Learning** and **Adaptive Differential Privacy** to train a global AI that can categorize medical specialties accurately while keeping every single patient note 100% confidential.

## 🌟 Key Features
-   **Real-World Medical Data**: Uses the **MTSamples** dataset (clinical transcripts) for training.
-   **Federated Intelligence**: Centralized learning without centralized data (using **Flower**).
-   **Adaptive Privacy Guard**: A "Dimmable Security Switch" that adds more mathematical noise to highly sensitive surgery data.
-   **Efficient Fine-Tuning**: Uses **LoRA** (Low-Rank Adaptation) to train the model on standard hardware.
-   **Live Monitoring**: A professional dashboard to track node health and privacy budgets.

---

## 🏗️ System Architecture
The system consists of a **Central Aggregator** and **Distributed Hospital Nodes**:
1.  **Hospital-East**: Specializes in Cardiology and Neurology data.
2.  **Hospital-West**: Specializes in Orthopedic and Surgery data (High Sensitivity).
3.  **Secure Aggregator**: Combines the "mathematical knowledge" from both without seeing the raw text.

---

## 🚦 How to Run the Project

### 1. Prerequisites
-   Python 3.10 to 3.14
-   At least 8GB RAM (16GB recommended)
-   Stable internet connection (to download the AI model)

### 2. Setup
```bash
# Clone the repository
git clone https://github.com/your-username/SecureEdge-GPT.git
cd SecureEdge-GPT

# Install all necessary AI and Privacy libraries
pip install -r requirements.txt
```

### 3. Launch the Simulation
Everything is automated in a single command:
```bash
python run_simulation.py
```
This command will:
1.  Download and prepare the **Medical Transcripts** dataset.
2.  Start the **Federated Server**.
3.  Launch **two Hospital Clients** (East and West).
4.  Open the **Monitoring Dashboard** on your browser.

---

## 📊 Viewing the Results
Once the simulation starts, open your browser to **http://localhost:8501** (or the port shown in your terminal). You will see the live training progress, node status, and the security budget being managed by the AI.

---

## 📜 Business Value
This project demonstrates a **Zero-Trust AI Architecture** that is ready for deployment in highly regulated sectors like Healthcare, Finance, and Legal. It ensures 100% compliance with data protection laws while delivering the power of Generative AI.
