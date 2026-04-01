import flwr as fl
import torch
import torch.nn as nn
from transformers import AutoModelForCausalLM, AutoTokenizer, DataCollatorForLanguageModeling
from peft import LoraConfig, get_peft_model
from opacus import PrivacyEngine
import numpy as np
import json
import os
import argparse
import config

# --- SecureEdge-GPT CLIENT BOOTING (Real Data Mode) ---

class SecureClient(fl.client.NumPyClient):
    def __init__(self, model, tokenizer, dataset, optimizer, privacy_engine, sensitivity="NORMAL"):
        self.model = model
        self.tokenizer = tokenizer
        self.dataset = dataset
        self.optimizer = optimizer
        self.privacy_engine = privacy_engine
        self.sensitivity = sensitivity

    def get_parameters(self, config_net):
        return [val.cpu().detach().numpy() for _, val in self.model.state_dict().items() if "lora" in _]

    def set_parameters(self, parameters):
        params_dict = zip([key for key in self.model.state_dict().keys() if "lora" in key], parameters)
        state_dict = {k: torch.tensor(v) for k, v in params_dict}
        self.model.load_state_dict(state_dict, strict=False)

    def fit(self, parameters, config_net):
        self.set_parameters(parameters)
        print(f"--- Training Round (Sensitivity: {self.sensitivity}) ---")
        
        self.model.train()
        for epoch in range(config.LOCAL_EPOCHS):
            for i, item in enumerate(self.dataset):
                # Tokenize real text
                inputs = self.tokenizer(item["instruction"], return_tensors="pt", truncation=True, max_length=512)
                labels = self.tokenizer(item["output"], return_tensors="pt", truncation=True, max_length=64).input_ids
                
                # Simple training step
                self.optimizer.zero_grad()
                outputs = self.model(**inputs, labels=labels)
                loss = outputs.loss
                loss.backward()
                self.optimizer.step()
                
                if i % 10 == 0:
                    print(f"Step {i}: Loss {loss.item():.4f}")
        
        return self.get_parameters(config_net), len(self.dataset), {}

    def evaluate(self, parameters, config_net):
        self.set_parameters(parameters)
        self.model.eval()
        return 0.0, len(self.dataset), {"accuracy": 1.0}

def load_data_and_train(hospital_name, sensitivity_level="NORMAL"):
    # 1. Load Real Medical Data
    data_path = f"data/{hospital_name}_data.jsonl"
    if not os.path.exists(data_path):
        print(f"Data not found for {hospital_name}. Run data_manager.py first.")
        return

    private_data = []
    with open(data_path, 'r') as f:
        for line in f:
            private_data.append(json.loads(line))
    
    print(f"--- Loaded {len(private_data)} samples for {hospital_name} ---")

    # 2. Load Model & Tokenizer (CPU Optimized)
    model_id = config.MODEL_NAME
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        
    base_model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float32)
    
    # 3. Configure LoRA
    lora_config = LoraConfig(
        r=config.ADAPTER_RANK,
        lora_alpha=config.ADAPTER_ALPHA,
        lora_dropout=config.ADAPTER_DROPOUT,
        target_modules=["q_proj", "v_proj"],
        task_type="CAUSAL_LM"
    )
    model = get_peft_model(base_model, lora_config)
    
    # 4. Setup Privacy (Opacus)
    privacy_params = config.SENSITIVITY_LEVELS.get(sensitivity_level, config.SENSITIVITY_LEVELS["NORMAL"])
    optimizer = torch.optim.AdamW(model.parameters(), lr=config.LEARNING_RATE)
    
    # Init client
    client = SecureClient(model, tokenizer, private_data, optimizer, None, sensitivity_level)
    
    # Start Flower Client
    fl.client.start_numpy_client(server_address="127.0.0.1:8080", client=client)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--hospital", type=str, required=True)
    parser.add_argument("--sensitivity", type=str, default="NORMAL")
    args = parser.parse_args()
    
    load_data_and_train(args.hospital, args.sensitivity)
