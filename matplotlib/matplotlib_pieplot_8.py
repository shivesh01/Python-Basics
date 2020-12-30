import  matplotlib.pyplot as plt
import numpy as np

slices = [7, 2, 2, 13]
activities = ["sleeping", "eating", "working", "playing"]
cols = ['c', 'm', 'r', 'b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        # slice separate out
        explode=(0.1, 0.1, 0.1, 0.1),
        autopct='%1.1f%%')

plt.title('pie plot')
plt.show()
