import clean
import numpy as np
import pandas as pd
import tourney_agg

CONSIDERING = 10

df = clean.get_data()
ts = df['tournament id'].unique()
all_players = df['player'].unique()

t_df = tourney_agg.tourney_data()
t_df = t_df.add_prefix('t_')

sim_stats = {}
bad_data = []
insuf_data = []


def _analysis(player, p_df):
    temp_df = pd.concat([p_df, t_df], axis=1, join="inner")
    temp_df.dropna(subset=['1', '2'], inplace=True)

    if len(temp_df) < CONSIDERING:
        insuf_data.append(player)

    temp_df = temp_df.tail(CONSIDERING)

    temp_df['net_1'] = temp_df['1'] - temp_df['t_1']
    temp_df['net_2'] = temp_df['2'] - temp_df['t_2']
    temp_df['net_3'] = temp_df['3'] - temp_df['t_3']
    temp_df['net_4'] = temp_df['4'] - temp_df['t_4']

    _scres = temp_df[['net_1', 'net_2', 'net_3', 'net_4']].to_numpy().flatten()
    scores = _scres[np.logical_not(np.isnan(_scres))]

    mean = np.mean(scores)
    std = np.std(scores)

    sim_stats[player] = {'mean': mean,
                         'std': std}


def player_analysis():

    i = 0
    total = len(all_players)
    for player in all_players:
        p_df = pd.read_csv(f'data/players/{player}.csv', index_col=0)
        try:
            _analysis(player, p_df)
        except Exception as e:
            print(e)
            bad_data.append(player)

        i += 1
        print(f"Finished {player}'s' DF. {(i/total)*100}% complete")

    bad_names = set(bad_data + insuf_data)
    print(bad_names, len(bad_names))

    return sim_stats, bad_names
