
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
initial_positions = np.array([
    [0.1, 0.2], [0.2, 0.3], [0.3, 0.4], [0.4, 0.5], [0.5, 0.6],
    [0.6, 0.5], [0.7, 0.4], [0.8, 0.3], [0.9, 0.2], [0.8, 0.1],
    [0.7, 0.2], [0.6, 0.3], [0.5, 0.4], [0.4, 0.5], [0.3, 0.6]
])

# Define the movement pattern for the running action
def running_motion(t):
    x = 0.1 * np.sin(2 * np.pi * t) + 0.5
    y = 0.1 * np.cos(2 * np.pi * t) + 0.5
    return x, y

# Create a figure and axis for the animation
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Create scatter plot for the point lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=10)

# Update function for the animation
def update(frame):
    t = frame / 100.0
    x, y = running_motion(t)
    positions = np.array([x, y])
    scatter.set_offsets(positions.T)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
