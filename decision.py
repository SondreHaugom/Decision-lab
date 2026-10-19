import base64
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
# hent API-nøkkelen
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=OPENAI_API_KEY)
image_base64 = base64.b64encode(Path("product.png").read_bytes()).decode("ascii")

def decision():
    try:
        decision = client.decisions.crreate(
            model = "gpt-6-luna",
            input = [
                {
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": "Inspect the product in this photo."},
                        {
                            "type": "input_image",
                            "image_url": f"data:image/png;base64,{image_base64}"
                        },
                    ],
                },
            ],

            question = [
                {
                    "type": "predicate",
                    "name": "visible_damage",
                    "instructions": (
                        "Does the product have visible damage, such as a crack, tear, or dent? "
                        "Ignore shadows and damage to the packaging."
                    ),
                }
            ],
        )
    except base64.b64decodeError:
        print("Feil ved base64 decoding. Prøv igjen")