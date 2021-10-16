# Filter rows by value

import pandas as pd

df = pd.read_csv('Example_data.csv', index_col=0)

above_19 = df[df['Age'] >= 20]
print(above_20)