# Plot - pie plot

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Example_data.csv', index_col=0)

df['Name'].value_counts().plot.pie()
plt.show()