import pandas as pd
df = pd.read_csv('tehranhdata.csv')
new_df = df.dropna()
