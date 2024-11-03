from fetchNBA import playerStats
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

def statPrediction(firstName, lastName, opponentTeam):
    """
    Predicts player performance in the next game against a specified opponent team.
    
    Parameters:
    firstName (str): The first name of the player.
    lastName (str): The last name of the player.
    opponentTeam (str): The name of the opposing team.
    """

    # Retrieve the Google API key from environment variables and configure the Generative AI model with the API key
    geminiApiKey = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=geminiApiKey)

    model = genai.GenerativeModel("gemini-pro")

    # Create a prompt for the AI model based on the player's name and opponent, include statistics from previous 5 seasons for extra context
    prompt = f"How will {firstName} {lastName} perform in his next game against {opponentTeam} "

    #Genereate response from Gemini
    response = model.generate_content(prompt)
    print(response.text)

statPrediction("Lebron", "James", "OKC")