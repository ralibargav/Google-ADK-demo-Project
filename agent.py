import os
from dotenv import load_dotenv

# New Google Gen AI SDK (replaces deprecated google.generativeai)
from google import genai

from tools import calculator

load_dotenv()

# The client will pick up GEMINI_API_KEY from env, but we also pass it explicitly
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

MODEL_NAME = "gemini-2.5-flash"


def run_agent(user_query: str) -> str:
    if "calculate" in user_query:
        expression = user_query.replace("calculate", "")
        return str(calculator(expression))

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=user_query,
    )

    # For simple text prompts, .text is convenient
    return response.text


if __name__ == "__main__":
    while True:
        query = input("Ask Agent: ")

        if query.strip().lower() == "exit":
            break

        result = run_agent(query)
        print("Agent:", result)