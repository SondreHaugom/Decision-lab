from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
from user_input import user_input
from model import models
import os
load_dotenv()
# hent API-nøkkelen
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=OPENAI_API_KEY)



def user_promt():
    promts = user_input()

    return promts


def model_type():
    try:
        fast = models()[1]
        thorough = models()[0]
        return fast and thorough
    
    except ValueError:
        print("No models found")



def decision():
    try:
        model = models()[0]

        decision = client.decisions.create(
            model=model,
            input= user_promt(),
            questions= [
                {
                    "type": "choice",
                    "name": "model_choice",
                    "instructions": "Which AI models should be used for this task?",
                    "choices": [
                        {"value": "Fast", "description": "Quick responses."},
                        {"value": "Thorough", "description": "Detailed analysis."},
                    ],
                },
            ],
        )
        answer = decision.answers[0]
        if answer.type == "refusal":
            print(f"Refused: {answer.name}")
        elif answer.type == "choice":
            print(f"model_choice: {answer.choice} (confidence: {answer.confidence})")

    except FileNotFoundError as e:
        print(f"Feil ved lesing av bilde: {e}")


decision()
