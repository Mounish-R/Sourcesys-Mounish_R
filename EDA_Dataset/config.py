import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load the environment variables from the .env file
load_dotenv()

# Initialize the Hugging Face Inference Client
# Make sure your .env has HUGGINGFACE_TOKEN
hf_token = os.getenv("HUGGINGFACE_TOKEN")
client = InferenceClient(token=hf_token)
