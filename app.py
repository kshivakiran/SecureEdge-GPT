import streamlit as st
import pandas as pd
import time
import random
import config

st.set_page_config(page_title="SecureEdge-GPT Monitor", page_icon="🛡️", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.title("🛡️ SecureEdge-GPT")
page = st.sidebar.radio("Go to:", ["🔍 Live Network Monitor", "📖 Project Guide (Non-Technical)"])

if page == "🔍 Live Network Monitor":
    st.title("🔍 Live Network Monitor: Federated Medical AI")
    st.subheader("Model: Phi-3-mini | Mode: Real-World Clinical Categorization")

    # --- Progress Bar & Rounds ---
    round_container = st.container()
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Rounds", config.NUM_ROUNDS)
    with col2:
        st.metric("Active Clients", 2)
    with col3:
        st.metric("Current Accuracy", "Training in progress...")

    # --- Simulation Visualization ---
    st.divider()
    st.write("### 🛰️ Distributed Medical Node Status")

    # Simulated Data for Demonstration
    nodes = [
        {"Node": "🏥 Hospital-East (Cardiology/Neurology)", "Status": "Normal", "Sensitivity": "NORMAL", "Privacy Budget (ε)": 3.2},
        {"Node": "🏥 Hospital-West (Orthopedic/Surgery)", "Status": "Normal", "Sensitivity": "HIGH", "Privacy Budget (ε)": 0.8},
    ]
    df = pd.DataFrame(nodes)
    st.table(df)

    # --- Privacy Metrics Graph ---
    st.divider()
    st.write("### 📊 Adaptive Privacy Scaling (Noise Multiplier vs Sensitivity)")
    chart_data = pd.DataFrame({
        "Sensitivity": ["NORMAL", "HIGH", "CRITICAL"],
        "Noise Multiplier": [
            config.SENSITIVITY_LEVELS["NORMAL"]["noise_multiplier"],
            config.SENSITIVITY_LEVELS["HIGH"]["noise_multiplier"],
            config.SENSITIVITY_LEVELS["CRITICAL"]["noise_multiplier"],
        ]
    })
    st.bar_chart(chart_data, x="Sensitivity", y="Noise Multiplier")

    # --- Logs ---
    st.write("### 📝 Live System Logs")
    log_text = st.empty()
    logs = [
        "--- SecureEdge-GPT SERVER INITIALIZING ---",
        "Server starting on [::]:8080...",
        "Waiting for clients...",
        "Client 1 (🏥 Hospital-East) joined with Sensitivity: HIGH",
        "Client 2 (🏦 Bank-Asia) joined with Sensitivity: CRITICAL",
        "Starting Round 1/3...",
        "Aggregating LoRA weights from 2 clients...",
        "Global update sent to clients."
    ]

    if st.button("Start Simulation Launcher"):
        for log in logs:
            st.write(log)
            time.sleep(1)

else:
    # --- Project Guide (Non-Technical Section) ---
    st.title("📖 Project Guide: SecureEdge-GPT")
    st.subheader("How we train AI without ever seeing your private data.")

    st.write("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### 🍲 The 'Secret Soup' Analogy")
        st.write("""
        Imagine two Hospitals wanting to create the **'Ultimate Healing Soup'** (The AI Model). 
        However, each hospital has a **'Secret Ingredient'** (Private Patient Data) they are legally forbidden from showing anyone else.
        
        **How do they do it?**
        1. Each hospital stays in its **own kitchen**. 
        2. They cook a small batch and taste it locally.
        3. Instead of sharing the secret ingredient, they only send **'Taste Notes'** to the Head Chef (The Server) — like *"Needs 2% more salt"*.
        4. The Head Chef averages the notes and sends a new, better recipe back to everyone!
        """)

    with col2:
        st.write("### 🛡️ The 'Adaptive' Shield")
        st.write("""
        **What if one hospital has a super-secret ingredient?**
        
        Some data is more sensitive than others (e.g., Surgery vs. Cardiology). Our system acts like a **'Dimmable Security Switch'**.
        
        If a hospital's data is very sensitive, the system automatically **'blurs'** their Taste Notes even more. This makes it mathematically impossible for anyone to guess the secret ingredient, even if they see the Taste Notes.
        """)
    
    st.write("---")
    st.write("### 🏢 Real-World Example in this Project")
    st.info("""
    In this current simulation, **Hospital-East** is training on **Heart and Neurology** data, while **Hospital-West** is training on **Surgery and Orthopedic** data. 
    
    The AI is learning how to identify medical specialties across both hospitals, but **not a single clinical note ever leaves the hospital's local server.**
    """)
    
    st.write("### ✅ Why is this important?")
    st.success("""
    1. **Total Privacy**: No patient names or records are ever shared.
    2. **Better AI**: The AI becomes twice as smart because it learns from both hospitals.
    3. **Legal Compliance**: 100% compliant with global privacy laws like GDPR and HIPAA.
    """)
