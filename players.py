import clean
import numpy as np
import pandas as pd

df = clean.get_data()
ts = df['tournament id'].unique()
all_players = df['player'].unique()
avg_scores_df = pd.read_csv('data/avg_scores.csv', index_col=0)


def _participated(name, tourn_id):
    t_players = df[df['tournament id'] == tourn_id]['player'].unique()
    if name in t_players:
        return True
    else:
        return False


def _save_player_data(all_player_data):
    players = all_player_data.keys()

    i = 0
    total = len(players)
    for player in players:
        t_data = all_player_data[player]
        player_df = pd.DataFrame.from_dict(t_data, orient='index')
        player_df.to_csv(f'data/players/{player}.csv')

        i += 1
        print(f"Finished {player}'s' DF. {(i/total)*100}% complete")


def player_score_data():
    all_player_data = {}

    i = 0
    total = len(all_players)
    for player in all_players:
        player_data = {}
        for t in ts:
            participated = _participated(player, t)
            if participated is True:
                player_data[t] = {}
                t_df = df[df['tournament id'] == t]
                p_df = t_df[t_df['player'] == player]

                rounds = np.sort(p_df['round'].unique())
                for round in rounds:
                    r_df = p_df[p_df['round'] == round]
                    score = r_df['strokes'].sum()
                    player_data[t][round] = score

        all_player_data[player] = player_data
        i += 1
        print(f'Finished {player}. {(i/total)*100}% complete')

    _save_player_data(all_player_data)

    return all_player_data


player_score_data()
