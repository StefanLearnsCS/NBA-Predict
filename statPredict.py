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

    # Call playerStats function to retrieve relevant player stats from previous 5 seasons.
    relevantStats = playerStats(firstName, lastName)

    # Create a prompt for the AI model based on the player's name and opponent, include statistics from previous 5 seasons for extra context
    prompt = f"""
        Based on {firstName} {lastName}'s performance in the upcoming game against {opponentTeam} over the last five seasons and their current form, predict the player's statistics for their 
        next game. Focus on the following categories: points, assists, rebounds, steals, blocks, and turnovers. Consider relevant factors such as age, 
        minutes played per game, field goal percentage, three-point percentage, free throw percentage, and the team's overall performance against the opponent.
        Also consider the players mentality, patterns, and motivations. Consider their rivals and what they want to prove to the fans.
        Provide the predicted values for each category clearly. Following are the player's stats from the previous 5 seasons:
    """ + str(relevantStats)

    #Genereate response from Gemini
    response = model.generate_content(prompt)
    
    return response.text