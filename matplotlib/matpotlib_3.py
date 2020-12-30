from matplotlib import pyplot as plt
from matplotlib import style

x1 = [5, 8, 10]
y1 = [12, 16, 6]

x2 = [6, 8, 11]
y2 = [6, 15, 7]

plt.plot(x1, y1, 'g', label='line 1', linewidth=5)
plt.plot(x2, y2, 'c',  label='line 2', linewidth=5)

plt.title("Info")
plt.ylabel("y- axis")
plt.xlabel("x - label")

plt.grid(True, color='k')
plt.legend()
plt.show()
