import subprocess
import time
import os
import sys

def main():
    python_exe = sys.executable
    print("Starting SecureEdge-GPT Simulation Launcher...")

    # 1. Prepare Data
    print("--- Preparing Real Medical Dataset ---")
    subprocess.run([python_exe, "data_manager.py"])
    time.sleep(2)

    # 2. Start Server in background

    # 3. Start Clients (Simulated Nodes)
    print("--- Starting Hospital-East Client (NORMAL Sensitivity) ---")
    client1_proc = subprocess.Popen([python_exe, "client.py", "--hospital", "Hospital-East", "--sensitivity", "NORMAL"])
    
    print("--- Starting Hospital-West Client (HIGH Sensitivity) ---")
    client2_proc = subprocess.Popen([python_exe, "client.py", "--hospital", "Hospital-West", "--sensitivity", "HIGH"])

    # 3. Start Dashboard
    print("--- Starting Monitoring Dashboard ---")
    dashboard_proc = subprocess.Popen([
        python_exe, "-m", "streamlit", "run", "dashboard.py",
        "--server.headless", "true",
        "--browser.gatherUsageStats", "false"
    ])

    print("--- Simulation Ready! Check the Dashboard for progress. ---")
    
    try:
        # Keep launcher running until interrupted
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n--- Stopping Simulation ---")
        server_proc.terminate()
        client1_proc.terminate()
        client2_proc.terminate()
        dashboard_proc.terminate()

if __name__ == "__main__":
    main()
