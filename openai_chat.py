from openai import OpenAI
from user_input import user_input
from model import models
from dotenv import load_dotenv
import os
load_dotenv()
# hent API-nøkkelen
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=OPENAI_API_KEY)












"""

def chat_with_gpt():
    while True:
        input = user_input()
        if user_input == "q".lower():
            print("Goodbye!")
            break
        try:
            response = client.responses.create(
                model= "gpt-6-luna",
                input= input,
            )
            print(response.choices[0].message.content)
        
        except Exception as e:
            print(f"Error: {e} ")


chat_with_gpt()
"""