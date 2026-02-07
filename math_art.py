import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, ax = plt.subplots()

for value in range(1, 1000):
    r = (1/150) + (1/10) * (np.sin((52*np.pi*value)/1000))**4

    x = np.cos((8*np.pi*value)/1000) * (
        1 - (1/2) * (np.cos((67*np.pi*value)/1000))**2
    )

    y = np.sin((8*np.pi*value)/1000) * (
        1 - (1/2) * (np.cos((67*np.pi*value)/1000))**2
    )

    circle = patches.Circle((x, y),
                            radius = r,
                            fill = False,
                            edgecolor = 'blue',
                            linewidth = 0.1
                        )
    
    ax.add_patch(circle)
    
ax.set_aspect('equal', adjustable = 'box')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
plt.show()

    
    
