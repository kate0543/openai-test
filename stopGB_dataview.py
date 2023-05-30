import pandas as pd
df=pd.read_table('../StopsGB.tsv')
print(df.columns)
row=df.head(1)
for value in row.values:
    print(value)