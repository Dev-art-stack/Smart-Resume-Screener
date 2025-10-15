import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

print("Checking for available models...")

try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    print("\n--- Models available for 'generateContent' ---")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    print("-------------------------------------------\n")

except Exception as e:
    print(f"An error occurred: {e}")