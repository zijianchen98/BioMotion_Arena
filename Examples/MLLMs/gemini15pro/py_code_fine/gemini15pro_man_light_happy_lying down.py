
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the coordinates of the 15 point lights
# Coordinates are adjusted to roughly match the provided image
x = np.array([0, -20, 20, -30, 30, -15, 15, -5, 5, 0, -40, 40, -20, 20])
y = np.array([100, 70, 70, 40, 40, 40, 40, 40, 40, 10, -20, -20, -50, -50])

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-60, 60)  # Adjust x-axis limits
ax.set_ylim(-60, 120) # Adjust y-axis limits
ax.set_aspect('equal')
ax.set_facecolor('black') # Set background color
scat = ax.scatter(x, y, s=30, c='white') # Initialize scatter plot with larger white dots

# Animation update function
def animate(i):
    # Oscillate the points slightly to simulate movement
    x_offset = 5 * np.sin(i / 10)  # Slight horizontal oscillation
    y_offset = 2 * np.cos(i / 10)  # Slight vertical oscillation
    scat.set_offsets(np.c_[x + x_offset, y + y_offset ])
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50, blit=True) # Increased frames, adjusted interval

plt.show()

