from openai import OpenAI
from user_input import user_input
from model import models
from dotenv import load_dotenv
from decision import decision
import os
load_dotenv()
# hent API-nøkkelen
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=OPENAI_API_KEY)


def model_choice():
    choice = decision()
    model = ""
    if choice == "Fast":
        model = models()[1]
    elif choice == "Thorough":
        model = models()[0]
    return model 


def chat_with_gpt():
    while True:
        input = user_input()
        if input == "q".lower():
            print("Goodbye!")
            break
        try:
            response = client.responses.create(
                model= models()[0],
                input= input,
            )
            print(response.output_text)
        
        except Exception as e:
            print(f"Error: {e} ")


chat_with_gpt()

    