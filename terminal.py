
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

while True:
    user_input = input("Enter your message (or 'quit' to exit): ")
    if user_input.lower() == 'quit':
        break
    
    response = model.generate_content(user_input)
    print("\nResponse:", response.text)
    print("\n" + "="*50 + "\n")
