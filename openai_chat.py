from openai import OpenAI
from user_input import user_input
from dotenv import load_dotenv
#from decision import decision
import os
load_dotenv()
# hent API-nøkkelen
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=OPENAI_API_KEY)


def model_choice():
    models = [
        "gpt-6-luna",
        "gpt-5.4-mini-2026-03-17"
    ]

    return models


model_to_use = ""

def decision():
    while True:
        try:
            user_promt = input("You: ")
            if user_promt == "q":
                print("Goodbye!")
                break
            decision = client.decisions.create(
                model="gpt-6-luna",
                input= user_promt,
                questions = [
                    {
                        "type": "choice",
                        "name": "model_choice",
                        "instructions": "Which AI models should be used for this task?",
                        "choices": [
                            {"value": "Fast", "description": "Quick responses."},
                            {"value": "Thorough", "description": "Detailed analysis."}
                        ],
                    },
                ],
            )
            answer = decision.answers[0]
            if answer.type == "refusal":
                print(f"Refused: {answer.name}")

            elif answer.type == "choice":
                if answer.choice == "Fast":
                    model_to_use = model_choice()[1]
                    print(f"Model that is used: {model_to_use} (confidence: {answer.confidence})")
                elif answer.choice == "Thorough":
                    model_to_use = model_choice()[0]
                    print(f"Model that is used: {model_to_use} (confidence: {answer.confidence})")
                else:
                    print("No models available")

        except Exception as e:
            print(f"Error: {e} ")
    
    return model_to_use and user_promt


decision()

"""


def chat_with_gpt():
    user_promt
    if user_promt == "q".lower():
        print("Goodbye!")
        
    try:
        response = client.responses.create(
            model= model_to_use,
            input= user_promt,
        )
        print(response.output_text)

     
    except Exception as e:
        print(f"Error: {e} ")



decision()

"""