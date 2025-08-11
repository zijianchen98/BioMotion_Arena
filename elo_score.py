import pandas as pd
import math

# --- Configuration ---
INITIAL_ELO = 1500
K_FACTOR = 32
# change 'votes.csv' to your own file. The format is as follows.
"""
model_left, model_right, winner
xxxx,xxxx,left/right
"""
CSV_FILE_PATH = 'votes.csv'


def calculate_new_ratings(rating_a, rating_b, score_a, k_factor=32):

    expected_a = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))

    score_b = 1 - score_a
    expected_b = 1 - expected_a

    new_rating_a = rating_a + k_factor * (score_a - expected_a)
    new_rating_b = rating_b + k_factor * (score_b - expected_b)

    return new_rating_a, new_rating_b


def main():

    try:
        df = pd.read_csv(CSV_FILE_PATH)
    except FileNotFoundError:
        print(f"The file '{CSV_FILE_PATH}' was not found.")


    models_left = df['model_left'].unique()
    models_right = df['model_right'].unique()
    all_models = set(models_left) | set(models_right)

    elo_ratings = {model: INITIAL_ELO for model in all_models}

    for index, row in df.iterrows():
        model_a = row['model_left']
        model_b = row['model_right']
        winner = row['winner']

        current_elo_a = elo_ratings[model_a]
        current_elo_b = elo_ratings[model_b]

        if winner == 'left':
            score_a = 1.0  # model_a win
        elif winner == 'right':
            score_a = 0.0  # model_a lose
        else:  # "both_bad", "tie"
            score_a = 0.5  

    
        new_elo_a, new_elo_b = calculate_new_ratings(current_elo_a, current_elo_b, score_a, K_FACTOR)

       
        elo_ratings[model_a] = new_elo_a
        elo_ratings[model_b] = new_elo_b

    
    sorted_ratings = sorted(elo_ratings.items(), key=lambda item: item[1], reverse=True)

    print(f"--- Final Elo score (initial={INITIAL_ELO}, K={K_FACTOR}) ---")
    for model, rating in sorted_ratings:
        print(f"{model:<15} | Elo: {rating:.2f}")


if __name__ == "__main__":
    main()