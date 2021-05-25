import pandas as pd

df = pd.read_csv('resultsfull.csv', index_col=0, low_memory=False)
print(df['TOTAL_Avg_Rank'])
