import pandas as pd

# data acquired from https://www.advancedsportsanalytics.com/pga-raw-data

hole_df = pd.read_csv('data/hole.csv')
# t_df = pd.read_csv('data/tourney.csv')

hole_good_cols = ['tournament id', 'hole', 'yards', 'par', 'strokes', 'round',
                  'player id', 'player', 'tournament name', 'course', 'season',
                  'date']
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

# t_good_cols = ['player', 'tournament id', 'player id', 'tournament name',
#                'season', 'course', 'date']

hole_df = hole_df[hole_good_cols].astype(convert_dict, errors='ignore')
print(hole_df.head())
print(len(hole_df))
print(hole_df[hole_df['player'] == 'Danny Lee'])
hole_df.to_csv('data/clean_hole.csv')
