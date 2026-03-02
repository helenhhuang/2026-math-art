import matplotlib.pyplot as plt
import numpy as np

for _ in range(10):
    x_pos = np.random.uniform(0, 10)
    for ymin in np.arange(-2, 2, 0.5):
        lw = 10-1.23 * (ymin + 2)
        plt.vlines(x_pos, ymin - 0.1, ymin + 0.5, linewidth=lw)

plt.xlim(-1, 11)
plt.show()