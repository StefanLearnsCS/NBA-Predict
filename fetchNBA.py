import requests

def playerStats(firstName, lastName):
    #NBA Stats API by swagger, http://b8c40s8.143.198.70.30.sslip.io/index.html
    base_url = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/name/"

    url = f"{base_url}{firstName}%20{lastName}"
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Define relevant statistics for prediction
        relevant_stats = []

        # Extract only relevant statistics for the most recent 5 seasons
        for player_stats in data:
            filtered_stats = {
                "season": player_stats.get("season"),
                "age": player_stats.get("age"),  # Age can affect performance
                "games": player_stats.get("games"),  # Total games played in the season
                "gamesStarted": player_stats.get("gamesStarted"),  # Games started, indicating a player's role
                "minutesAverage": player_stats.get("minutesPg") / player_stats.get("games"),  # Minutes per game, a key factor in performance
                "fieldGoals": player_stats.get("fieldGoals"),  # Field goals made
                "fieldAttempts": player_stats.get("fieldAttempts"),  # Field goal attempts
                "threeFg": player_stats.get("threeFg"),  # Three-point field goals made
                "twoFg": player_stats.get("twoFg"),  # Two-point field goals made
                "ft": player_stats.get("ft"),  # Free throws made
                "total_rb": player_stats.get("totalRb"),  # Total rebounds
                "assists": player_stats.get("assists"),  # Total assists
                "steals": player_stats.get("steals"),  # Steals, indicating defensive capability
                "blocks": player_stats.get("blocks"),  # Blocks, indicating defensive capability
                "turnovers": player_stats.get("turnovers"),  # Turnovers, negatively impacting overall performance
                "personalFouls": player_stats.get("personalFouls"),  # Personal fouls, can limit playtime
                "pointsPerGame": player_stats.get("points") / player_stats.get("games"),  # Total points scored
                "team": player_stats.get("team")  # Team affiliation
            }

            relevant_stats.append(filtered_stats)
        
        # Sort by season and get the 5 most recent seasons
        relevant_stats.sort(key=lambda x: x["season"], reverse=True)
        recent_stats = relevant_stats[:5]

        print("Relevant Player Statistics for the 5 Most Recent Seasons: \n")
        for season in recent_stats:
            print(season)
            print()
    else:
        print(f"Failed to retrieve data: {response.status_code} - {response.text}")