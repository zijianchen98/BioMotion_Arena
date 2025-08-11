
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Hand
    [1, 0],  # Wrist
    [2, 0],  # Elbow
    [3, 0],  # Shoulder
    [4, 0],  # Hip
    [5, 0],  # Knee
    [6, 0],  # Ankle
    [7, 0],  # Foot
    [8, 0],  # Hand
    [9, 0],  # Wrist
    [10, 0],  # Elbow
    [11, 0],  # Shoulder
    [12, 0],  # Hip
    [13, 0],  # Knee
    [14, 0]   # Ankle
]

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 15)
ax.set_ylim(-1, 1)
ax.axis('off')

# Plot the initial positions
points, = ax.plot([], [], 'o', color='white')

def init():
    points.set_data([], [])
    return points,

def animate(i):
    # Update the positions of the points
    points.set_data(positions[i % len(positions)])
    return points,

# Create the animation
ani = FuncAnimation(fig, animate, frames=range(len(positions)), init_func=init, blit=True)

# Save the animation
ani.save('point_light_stimulus.mp4', writer='ffmpeg', fps=10)

plt.show()
