import clean
import numpy as np
import pandas as pd

# Calculate the average score for each round

df = clean.get_data()
ts = df['tournament id'].unique()
all_players = df['player'].unique()


def get_tourney_avg_scores():
    tournament_avg_scores = {}
    for t in ts:
        t_df = df[df['tournament id'] == t]
        rounds = np.sort(t_df['round'].unique())

        players = t_df['player'].unique()

        tournament_avg_scores[t] = {}
        for round in rounds:
            round_df = t_df[t_df['round'] == round]

            player_scores = []
            for player in players:
                player_r_df = round_df[round_df['player'] == player]
                player_score = player_r_df['strokes'].sum()

                if player_score != 0:
                    player_scores.append(player_score)

            round_avg = np.mean(np.array(player_scores))
            tournament_avg_scores[t][round] = round_avg

    return tournament_avg_scores


def avg_scores_df():
    data = get_tourney_avg_scores()
    df = pd.DataFrame.from_dict(data, orient='index')
    df.to_csv('data/avg_scores.csv')
    print(df)
    return df


avg_scores_df()
