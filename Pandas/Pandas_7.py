# Groupby - mean per occurence of value

import pandas as pd

df = pd.read_csv('Example_data.csv', index_col=0)

avg_age_per_name = df.groupby('Name').mean()
print(avg_age_per_name)