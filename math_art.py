import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, ax = plt.subplots(figsize=(6, 6))

# Part 1: Draw the pattern of circles
for value in range(1, 1000):
    # Radius varies sinusoidally
    r = (1/150) + (1/10) * (np.sin((52*np.pi*value)/1000))**4
    
    # Coordinates for the circle centers
    common_factor = 1 - (1/2) * (np.cos((6*np.pi*value)/1000))**2
    x = np.cos((5*np.pi*value)/1000) * np.cos(np.pi * 3) * common_factor
    y = np.sin((10/np.pi*value)/1000) * common_factor

    circle = patches.Circle((x, y), radius=r, fill=False, color=(0.1, 0.5, 0.8), linewidth=0.1)
    ax.add_patch(circle)

# Part 2: Draw the polar-style curve
k = 0.05
theta = np.linspace(0, 3 * np.pi, 500)
r_polar = k * np.cos(4*theta)

# Convert polar to Cartesian for the same axes
x_polar = r_polar * np.cos(theta)
y_polar = r_polar * np.sin(theta)
#ax.plot(x_polar, y_polar, color='red', alpha=0.5)

# Formatting
ax.set_yticks([])
ax.set_xticks([])
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
#plt.savefig("cool_circles.png")
plt.show()