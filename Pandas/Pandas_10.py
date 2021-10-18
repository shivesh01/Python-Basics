# Plot - scatter plot

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Example_data.csv', index_col=0)

df.plot.scatter(x='Name', y='Age')
plt.show()