import base64
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
# hent API-nøkkelen
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=OPENAI_API_KEY)

def decicions(promt):
    try:
        promt("You: ")

        if promt == "q":
            print("Goodbye!")
            exit()

    except ValueError:
        print("Feil ved innputt. Prøv igjen.")    