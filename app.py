import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

print("AI Chatbot Started")
print("Type 'quit' to exit")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    print("\nBot:", response.choices[0].message.content)

except Exception as e:
    print("Error:", e)