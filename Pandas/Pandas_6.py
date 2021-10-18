# Groupby - amount per occurence of value

import pandas as pd

df = pd.read_csv('Example_data.csv', index_col=0)

amout_per_age = df.groupby('Age').count()
print(amout_per_age)