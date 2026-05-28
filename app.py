from openai import OpenAI

client = OpenAI(
    api_key="OPENAI_API_KEY"
)

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": "Explain AI in simple words"
        }
    ]
)

print(response.choices[0].message.content)