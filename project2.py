import pandas as pd
df = pd.read_csv(
    "E:/learning/py-ml-jadi/jadimlgit/regression-project/tehranhdata.csv")
new_df = df.dropna()
new_df.to_csv(
    "E:/learning/py-ml-jadi/jadimlgit/regression-project/tehranhdata2.csv")
# empty cell cleared and saved
