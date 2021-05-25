import analysis
import numpy as np
import pandas as pd

SIMS = 100000

sim_stats, bad_names = analysis.player_analysis()

df = pd.DataFrame.from_dict(sim_stats, orient='index')
df.sort_values(['mean'], inplace=True)
df.dropna(inplace=True)

parts_file = open("data/parts.txt", "r")
participant_list = [line.strip() for line in parts_file.readlines()]

player_data_list = df.index.tolist()
no_data = []

players = []
for player in participant_list:
    if player in player_data_list:
        players.append(player)
    else:
        no_data.append(player)


def mc_sim():
    _res_dfs = []
    for i in range(SIMS):
        scores = {}
        for player in players:
            p_df = df[df.index == player]
            mu = p_df['mean'].iloc[0]
            sigma = p_df['std'].iloc[0]
            p_scores = np.random.normal(mu, sigma, size=4)

            scores[player] = p_scores

        _res_df = pd.DataFrame.from_dict(scores, orient='index')
        _res_df['total'] = _res_df.sum(axis=1)
        _res_df.sort_values(by='total', inplace=True)
        _res_df['Rank'] = _res_df['total'].rank()
        _res_dfs.append(_res_df['Rank'])
        # print(_res_df)

    res_df = pd.concat(_res_dfs, axis=1, join="inner")
    res_df['TOTAL_Rank'] = res_df.sum(axis=1) / SIMS
    res_df['TOTAL_Avg_Rank'] = res_df['TOTAL_Rank'].rank()
    res_df.sort_values(by='TOTAL_Avg_Rank', inplace=True)
    # res_df['TOTAL_Avg_Rank'].to_csv('results4.csv')
    res_df.to_csv('resultsfull.csv')
    print(res_df)


mc_sim()
