import pandas as pd

# data acquired from https://www.advancedsportsanalytics.com/pga-raw-data

convert_dict = {'tournament id': int,
                'hole': int,
                'yards': int,
                'par': int,
                'strokes': int,
                'round': int,
                'player id': int,
                'player': str,
                'tournament name': str,
                'course': str,
                'season': int,
                'date': str}

hole_df = pd.read_csv('data/clean_hole.csv', index_col=0, low_memory=False)
hole_df = hole_df.astype(convert_dict, errors='ignore')


def get_data(hole_df=hole_df):
    return hole_df
