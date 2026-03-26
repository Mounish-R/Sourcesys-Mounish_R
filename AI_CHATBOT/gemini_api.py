from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

def load_gemini():
    api_key = os.getenv("GEMINI_API_KEY")

    client = genai.Client(
        api_key=api_key
    )

    return client

def get_response(client, user_input):
    response = client.models.generate_content(
        model="gemini-2.5-flash",  
        contents=user_input
    )
    return response.text