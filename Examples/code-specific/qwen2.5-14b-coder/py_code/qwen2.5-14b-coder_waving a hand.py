
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points
num_points = 15

# Define the initial positions of the points
initial_positions = np.array([
    [0.2, 0.5], [0.3, 0.5], [0.4, 0.5], [0.5, 0.5], [0.6, 0.5],
    [0.7, 0.5], [0.8, 0.5], [0.9, 0.5], [1.0, 0.5], [0.5, 0.4],
    [0.5, 0.3], [0.5, 0.2], [0.5, 0.1], [0.5, 0.6], [0.5, 0.7]
])

# Define the target positions for the waving motion
target_positions = np.array([
    [0.2, 0.5], [0.3, 0.5], [0.4, 0.5], [0.5, 0.5], [0.6, 0.5],
    [0.7, 0.5], [0.8, 0.5], [0.9, 0.5], [1.0, 0.5], [0.5, 0.4],
    [0.5, 0.3], [0.5, 0.2], [0.5, 0.1], [0.5, 0.6], [0.5, 0.7]
])

# Define the wave motion
def wave_motion(t):
    x = np.linspace(0, 1, num_points)
    y = np.sin(2 * np.pi * (x - t)) * 0.1 + 0.5
    return np.column_stack((x, y))

# Define the update function for the animation
def update(frame):
    positions = wave_motion(frame / 100.0)
    sc.set_offsets(positions)
    return sc,

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Create the scatter plot
sc = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=100)

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), blit=True, repeat=False)

# Show the animation
plt.show()
