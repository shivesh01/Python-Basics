import  matplotlib.pyplot as plt
import numpy as np

days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

labels = ["sleeping", "eating", "working", "playing"]

fig, ax = plt.subplots()
ax.stackplot(days, sleeping, eating, working, playing, labels=labels)
ax.legend()

plt.xlabel('x')
plt.ylabel('y')
plt.title('stack plot')
plt.show()