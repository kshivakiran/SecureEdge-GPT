import os

# --- Model Settings ---
MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"  # Small & Powerful
ADAPTER_RANK = 8
ADAPTER_ALPHA = 16
ADAPTER_DROPOUT = 0.05

# --- Federated Learning Settings ---
NUM_ROUNDS = 3
NUM_CLIENTS = 2
MIN_FIT_CLIENTS = 2
FRACTION_FIT = 1.0

# --- Privacy Settings ---
# Adaptive Privacy Levels
SENSITIVITY_LEVELS = {
    "NORMAL": {"noise_multiplier": 0.5, "max_grad_norm": 1.0},
    "HIGH": {"noise_multiplier": 1.5, "max_grad_norm": 1.2},
    "CRITICAL": {"noise_multiplier": 3.0, "max_grad_norm": 1.5},
}

# Default training settings
LEARNING_RATE = 2e-4
BATCH_SIZE = 1
LOCAL_EPOCHS = 1
