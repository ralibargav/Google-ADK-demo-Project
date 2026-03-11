import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL_NAME = "gemini-2.5-flash"


class ResearchAgent:

    def run(self, query):
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=query,
        )
        return response.text