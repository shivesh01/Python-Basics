# Useful built-in methods and attributes

import pandas as pd

df = pd.read_csv('Example_data.csv', index_col=0)

columns = df.columns
print(columns)

types = df.dtypes
print(types)

describe = df.describe()
print(describe)