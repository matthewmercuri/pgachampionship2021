import clean

df = clean.get_data()

players = df['player'].unique()

print(df.head())
print(players)
print(df[df['player'] == players[0]])
print(df[df['player'] == 'Rory McIlroy'])
