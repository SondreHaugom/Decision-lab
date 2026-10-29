from openai import OpenAI
from user_input import user_input
from dotenv import load_dotenv
import os
load_dotenv()
# hent API-nøkkelen
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=OPENAI_API_KEY)


def chat_with_gpt():
    while True:
        user_input = user_input()
        if user_input.lower() == "q":
            print("Goodbye!")
            break
        try:
            response = client.responses.create(
                model
            )
        except Exception as e:
            print(f"Error: {e} ")