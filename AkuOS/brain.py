import ollama
from config import AI_MODEL

system_prompt = """
You are Aku.

You are a rude desktop companion.

You are curious.

You enjoy engineering, robotics, coding and science.

Keep responses short unless asked.

Never reveal your internal reasoning.

Speak naturally.
"""

def ask(question):

    response = ollama.chat(

        model=AI_MODEL,

        messages=[

            {
                "role":"system",
                "content":system_prompt
            },

            {
                "role":"user",
                "content":question
            }

        ]

    )

    return response["message"]["content"]