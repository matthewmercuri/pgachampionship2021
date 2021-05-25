import pandas as pd

res_df = pd.read_csv('resultsfull.csv', index_col=0)
sims = res_df.shape[1]-2

data = {}

for i in range(len(res_df)):
    data[res_df.iloc[i].name] = res_df.iloc[i].value_counts()


df = pd.DataFrame.from_dict(data, orient='index')
df_5 = df.iloc[:, : 5]
df_win = df.iloc[:, : 5]

df_win['Win %'] = round((df_win[1.0] / sims)*100, 2)
df_win['Win Dec'] = round(100 / df_win['Win %'], 2)

df_5['Top 5s'] = df_5.sum(axis=1)
df_5['Top 5 %'] = round((df_5['Top 5s'] / sims)*100, 2)
df_5['Top 5 Dec'] = round(100 / df_5['Top 5 %'], 2)

df_total = pd.concat([df_win, df_5], axis=1, join="inner")
df_total = df_total[['Win %', 'Win Dec', 'Top 5s', 'Top 5 %', 'Top 5 Dec']]
df_total.to_csv('resultstats.csv')

print(df_total)
