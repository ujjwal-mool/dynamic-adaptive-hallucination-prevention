from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate(question, system_prompt=""):

    prompt = f"""
{system_prompt}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",      # or the Gemini model you're using successfully
        contents=prompt
    )

    return response.text