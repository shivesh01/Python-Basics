# Read csv file

import pandas as pd

df = pd.read_csv('Example_data.csv', index_col=0)

print(df)