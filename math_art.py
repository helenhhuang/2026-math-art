import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math

fig, ax = plt.subplots(figsize=(8, 8))

def trig_to_rgb(t):
    r = ((np.sin(t + 4*np.pi/3) + 1) / 2) * 0.9
    g = 0
    b = ((np.sin(t + 2*np.pi/3) + 1) / 2) * 0.9
    return (r, g, b)


# Part 1: Draw the pattern of circles
for value in range(1, 1000):
    # 1. Radius calculation
    radius = (1/150) + (1/10) * (np.sin((52*np.pi*value)/1000))**4
    
    # 2. Coordinates calculation
    common_factor = 1 - (1/2) * (np.cos((6*np.pi*value)/1000))**2
    # Ensure x and y remain single floats (scalars)
    x_pos = np.cos((5*np.pi*value)/1000) * common_factor
    y_pos = np.sin((16*np.pi*value)/1000) * common_factor
    
    # 3. Color calculation
    # Using 'value' as the phase creates a smooth transition across the drawing order
    rgb = trig_to_rgb(value * 0.05) 
    
    circle = patches.Circle((x_pos, y_pos), radius=radius, fill=False, color=rgb, linewidth=0.3)
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
plt.savefig("final.pdf")
plt.show()