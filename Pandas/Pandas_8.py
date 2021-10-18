# Plot - histogram

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Example_data.csv', index_col=0)

df['Age'].plot.hist()
plt.show()

df['Age'].plot.hist(bins=4, edgecolor='black')
plt.show()