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






def decision():
    try:
        model = models()
   
        decision = client.decisions.create(
            model = "gpt-6-luna",
            input = [
                {
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": user_promt()},
                        {
                            "type": "input_image",
                            "image_url": f"data:image/png;base64,{model}"
                        },
                    ],
                },
            ],

            questions = [
                {
                    "type": "predicate",
                    "name": "models",
                    "instructions": (
                        "if the promt is lage use models[0] and if the promt i smal use models[1]"
                    ),
                }
            ],
        )

        answer = decision.answers[0]
        if answer.type == "refusal":
            print(f"Refused: {answer.name}")
        elif answer.type == "predicate":
            print(f"Right model for this task: {answer.probability}")
    
    except FileNotFoundError as e:
        print(f"Feil ved lesing av bilde: {e}")


decision()
