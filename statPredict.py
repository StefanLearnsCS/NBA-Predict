from fetchNBA import playerStats
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

def statPrediction(firstName, lastName, opponentTeam):
    geminiApiKey = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=geminiApiKey)

    model = genai.GenerativeModel("gemini-pro")

    prompt = f"How will {firstName} {lastName} perform in his next game against {opponentTeam} "
    response = model.generate_content(prompt)
    print(response.text)

statPrediction("Lebron", "James", "OKC")