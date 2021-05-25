import clean
import pandas as pd

df = clean.get_data()
ts = df['tournament id'].unique()


def tourney_meta():
    t_meta = {}

    for t in ts:
        t_meta[t] = {}

        t_df = df[df['tournament id'] == t]
        name = t_df['tournament name'].iloc[0]

        season = t_df['season'].iloc[0]
        dates = t_df['date'].iloc[0]

        t_meta[t]['name'] = name
        t_meta[t]['season'] = season
        t_meta[t]['date'] = dates

    t_meta_df = pd.DataFrame.from_dict(t_meta, orient='index')

    return t_meta_df


def tourney_data():
    t_df = pd.read_csv('data/avg_scores.csv', index_col=0)

    t_meta_df = tourney_meta()
    t_df = pd.concat([t_df, t_meta_df], axis=1, join="inner")

    return t_df
