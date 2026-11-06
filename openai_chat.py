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




def chat_with_gpt():
    while True:
        input = user_input()
        if input == "q".lower():
            print("Goodbye!")
            break
        try:
            response = client.responses.create(
                model= "chatgpt-4o-latest",
                input= input,
            )
            print(response.output_text)
        
        except Exception as e:
            print(f"Error: {e} ")




def decision():
    try:
        model = models()[0]

        decision = client.decisions.create(
            model=model,
            input= user_input(),
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
                print(f"Best model for this task is: {answer.choice}: {models()[1]} (confidence: {answer.confidence})")
                chat_with_gpt()
            elif answer.choice == "Thorough":
                print(f"Best model for this task is: {answer.choice}: {models()[0]} (confidence: {answer.confidence})")
                chat_with_gpt()
    
    except FileNotFoundError as e:
        print(f"Feil ved lesing av bilde: {e}")




