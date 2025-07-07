from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini 1.5 Flash model
model = genai.GenerativeModel("gemini-1.5-flash")

# Chat loop
user_input = input("Enter: ")
while user_input.lower() != "exit":
    response = model.generate_content([user_input])
    print(f"\nAI: {response.text}")
    user_input = input("Enter: ")
