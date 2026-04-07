import os
import pandas as pd
from config import client
from prompts import get_eda_prompt

def generate_eda_report(file_path: str) -> str:
    df = pd.read_csv(file_path)
    sample_data = df.head(15).to_csv(index=False)
    
    prompt = get_eda_prompt(sample_data)
    
    response = client.chat_completion(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800,
        temperature=0.2
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    if not os.getenv("HUGGINGFACE_TOKEN"):
        raise EnvironmentError("HUGGINGFACE_TOKEN environment variable is not set.")

    dataset_path = os.path.join(os.path.dirname(__file__), "mobiles1.csv")
    output_path = os.path.join(os.path.dirname(__file__), "eda_report.md")

    try:
        print("Generating professional EDA report. This may take a moment...")
        report = generate_eda_report(dataset_path)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)
            
        print(f"Report successfully saved to {output_path}")
        
    except FileNotFoundError:
        print(f"Dataset not found at: {dataset_path}")
    except Exception as e:
        print(f"Report generation failed: {e}")
