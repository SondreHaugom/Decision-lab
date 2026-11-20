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


model_to_use = model_choice()[0]




def chat_with_gpt():
    while True:
        user_promt = user_input()
        if user_promt == "q".lower():
            print("Goodbye!")
            break
        try:
            response = client.responses.create(
                model= model_to_use,
                input= user_promt,
            )
            print(response.output_text)

     
        except Exception as e:
            print(f"Error: {e} ")


chat_with_gpt()


"""
def decision():
    try:

        decision = client.decisions.create(
            model= "gpt-6-luna",
            input= user_promt,
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
            if answer.choice == "Fast":
                print(f"Best model for this task is: {answer.choice}: {model_choice()[1]} (confidence: {answer.confidence})")
                model_to_use = model_choice()[1]
                #print(f"Model that is used: {model_to_use} and user input: {user_promt}")
                chat_with_gpt(model_to_use)
            elif answer.choice == "Thorough":
                print(f"Best model for this task is: {answer.choice}: {model_choice()[0]} (confidence: {answer.confidence})")
                model_to_use = model_choice()[0]
                print(f"Model that is used: {model_to_use} and user input: {user_promt}")
                #chat_with_gpt(model_to_use)
            else:
                print(f"Invalid choice: {answer.choice}")
    
    except FileNotFoundError as e:
        print(f"Feil ved lesing av bilde: {e}")


#decision()


"""