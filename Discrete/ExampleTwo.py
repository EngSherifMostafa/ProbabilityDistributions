from scipy.stats import poisson
import numpy as np

# Function to calculate the average goals based on goals scored and matches played this season
def calculate_average_goals(goals_scored, matches_played):
    return goals_scored / matches_played if matches_played > 0 else 0

# Function to calculate the Poisson probability for a given lambda and number of goals
def poisson_probability(lmbda, k):
    return poisson.pmf(k, lmbda)

# Function to predict match outcomes and number of goals based on average goals this season
def predict_match_outcome(average_goals_scored_home, average_goals_scored_away, average_goals_conceded_home, average_goals_conceded_away):
    goals_range = np.arange(10)  # Adjust as needed

    # Calculate Poisson probabilities for different goal combinations
    prob_home_win = sum(poisson_probability(average_goals_scored_home, i) * poisson_probability(average_goals_conceded_away, j) for i in goals_range for j in goals_range if i > j)
    prob_away_win = sum(poisson_probability(average_goals_scored_away, i) * poisson_probability(average_goals_conceded_home, j) for i in goals_range for j in goals_range if i < j)
    prob_draw = sum(poisson_probability(average_goals_scored_home, i) * poisson_probability(average_goals_conceded_away, j) for i in goals_range for j in goals_range if i == j)

    # Print probabilities for match outcomes
    print("Probability of Home Win: {:.2%}".format(prob_home_win))
    print("Probability of Away Win: {:.2%}".format(prob_away_win))
    print("Probability of Draw: {:.2%}".format(prob_draw))

    # Determine the result
    if prob_home_win > prob_away_win and prob_home_win > prob_draw:
        print("Predicted Result: Home Win")
    elif prob_away_win > prob_home_win and prob_away_win > prob_draw:
        print("Predicted Result: Away Win")
    else:
        print("Predicted Result: Draw")

    # Predict number of goals
    predicted_goals_home = np.argmax([poisson_probability(average_goals_scored_home, k) for k in goals_range])
    predicted_goals_away = np.argmax([poisson_probability(average_goals_scored_away, k) for k in goals_range])

    print(f"Predicted Number of Goals for Home Team: {predicted_goals_home}")
    print(f"Predicted Number of Goals for Away Team: {predicted_goals_away}")

# Hypothetical data for illustration purposes
goals_scored_home_team_season = int (input("Enter goals scored home team season"))
goals_conceded_home_team_season = int (input("Enter goals conceded home team season"))
matches_played_home_team_season = int (input("Enter matches played this season for home team "))


goals_scored_away_team_season = int (input("Enter goals scored away team season"))
goals_conceded_away_team_season = int (input("Enter goals conceded away team season"))
matches_played_away_team_season = int (input("Enter matches played this season for away team "))


# Calculate average goals for the home and away teams
average_goals_scored_home_team = calculate_average_goals(goals_scored_home_team_season, matches_played_home_team_season)
average_goals_scored_away_team = calculate_average_goals(goals_scored_away_team_season, matches_played_away_team_season)

average_goals_conceded_home_team = calculate_average_goals(goals_conceded_home_team_season, matches_played_home_team_season)
average_goals_conceded_away_team = calculate_average_goals(goals_conceded_away_team_season, matches_played_away_team_season)

# Make predictions based on the average goals this season
predict_match_outcome(average_goals_scored_home_team, average_goals_scored_away_team, average_goals_conceded_home_team, average_goals_conceded_away_team)
