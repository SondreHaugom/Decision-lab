from openai import OpenAI
from dotenv import load_dotenv
from model import models
import os

load_dotenv()
# hent API-nøkkelen
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=OPENAI_API_KEY)

openai_models = models()

response_id = None

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
                    model_to_use = openai_models[1]
                    print(f"Model that is used: {model_to_use} (confidence: {answer.confidence})")
                    print("---------------------------------------------------------------------")
                elif answer.choice == "Thorough":
                    model_to_use = openai_models[0]
                    print(f"Model that is used: {model_to_use} (confidence: {answer.confidence})")
                    print("---------------------------------------------------------------------")
                else:
                    print("No models available")

                chat_with_gpt(model_to_use, user_promt)
        except Exception as e:
            print(f"Error: {e} ")
    
    
    


def chat_with_gpt(model_to_use, user_promt):
    global response_id
    promt = user_promt
    model = model_to_use
        
    try:
        response = client.responses.create(
            model= model,
            input= promt,
            stream= True,
            previous_response_id= response_id,
        )
        for event in response:
            if event.type == "response.output_text.delta":
                print(event.delta, end="", flush=True)
            elif event.type == "response.completed":
                response_id = event.response.id
            elif event.type == "error":
                print(f"Error: {event.error.message}")
        print()
 
    except Exception as e:
        print(f"Error: {e} ")


decision()