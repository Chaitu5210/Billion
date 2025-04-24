import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

def GeneralizationAgent(input: str) -> str:
    response = model.generate_content(input)
    return response.text


if __name__ == "__main__":
    user_input = "What Is The Current Time"
    result = GeneralizationAgent(user_input)
    print(result)