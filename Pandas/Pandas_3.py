# Select column

import pandas as pd

df = pd.read_csv('Example_data.csv', index_col=0)

names = df['Name']
print(names)

ages = df['Age']
print(ages)
