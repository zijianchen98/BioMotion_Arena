
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(i):
    # Update the position of the points
    x = np.sin(((i * 0.1) % (np.pi * 2)
    y = np.cos(((i * 0.1) % np.pi * 2))
    
    # Update the scatter plot
    sc.set_offsets(np.c_[x, y])
    return sc,

# Create the figure and axes
fig, ax = plt.subplots()

# Set the limits of the axes
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Create the scatter plot
sc = ax.scatter([], [])

# Set the background color to black
ax.set_facecolor('black')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=20)

# Show the plot
plt.show()
