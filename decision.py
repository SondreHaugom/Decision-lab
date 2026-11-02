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

        
    except FileNotFoundError as e:
        print(f"Feil ved lesing av bilde: {e}")


decision()
