import os
from datasets import load_dataset
import pandas as pd
import json

def prepare_medical_data():
    print("--- DOWNLOADING REAL MEDICAL DATA (MTSamples) ---")
    
    # Load dataset from Hugging Face
    try:
        ds = load_dataset("tchebonenko/MedicalTranscriptions", split="train")
        df = pd.DataFrame(ds)
    except Exception as e:
        print(f"Error downloading dataset: {e}")
        return

    # Clean data (ensure specialty and transcription aren't null)
    df = df.dropna(subset=['medical_specialty', 'transcription'])
    
    # Let's pick 4 distinct specialties to simulate different hospitals
    hospitals = {
        "Hospital-East": [" Cardiovascular / Pulmonary", " Neurology"],
        "Hospital-West": [" Orthopedic", " Surgery"]
    }
    
    os.makedirs("data", exist_ok=True)
    
    for hospital_name, specialties in hospitals.items():
        # Filter for the specialties assigned to this hospital
        hospital_df = df[df['medical_specialty'].isin(specialties)]
        
        # Take a subset to keep it fast for PoC (e.g., 50 samples)
        hospital_df = hospital_df.sample(min(len(hospital_df), 50))
        
        # Format for LLM Categorization:
        # Prompt: "Determine the medical specialty of this transcript: [TRANSCRIPTION]"
        # Completion: "[SPECIALTY]"
        data_list = []
        for _, row in hospital_df.iterrows():
            sample = {
                "instruction": f"Determine the medical specialty of this transcript: {row['transcription'][:500]}...",
                "output": row['medical_specialty'].strip()
            }
            data_list.append(sample)
            
        file_path = f"data/{hospital_name}_data.jsonl"
        with open(file_path, 'w') as f:
            for entry in data_list:
                f.write(json.dumps(entry) + '\n')
                
        print(f"--- Saved {len(data_list)} samples for {hospital_name} to {file_path} ---")

if __name__ == "__main__":
    prepare_medical_data()
