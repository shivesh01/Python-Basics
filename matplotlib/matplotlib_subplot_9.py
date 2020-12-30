import matplotlib.pyplot as plt
import numpy as np


# working with multiple plot
def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


t1 = np.arange(0, 5, 0.1)
t2 = np.arange(0, 5, 0.02)

# subplot(available graph, aligning horzontially /vertically, first graph)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2))

plt.subplot(212)
plt.plot(t2, np.cos(2 * np.pi * t2))
plt.show()
