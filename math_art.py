import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

#Start with a single line
#plt.vlines(0, -2, 2, linewidth = 10)
    
#break line into smaller segments
for ymin in np.arange(-2, 2, 0.5):
    lw = 10-1.23 * (ymin + 2)
    plt.vlines(0, ymin, ymin + 0.5, linewidth=lw)

plt.show()