
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
# These positions are based on a simplified model of a waving hand
initial_positions = np.array([
    [0.1, 0.2], [0.2, 0.3], [0.3, 0.4], [0.4, 0.5], [0.5, 0.6],
    [0.5, 0.5], [0.4, 0.4], [0.3, 0.3], [0.2, 0.2], [0.1, 0.1],
    [0.2, 0.1], [0.3, 0.1], [0.4, 0.1], [0.5, 0.1], [0.6, 0.1]
])

# Define the function to update the positions of the point lights
def update(frame):
    # Calculate the new positions based on the current frame
    t = frame / 100.0
    new_positions = initial_positions.copy()
    new_positions[:, 0] += 0.1 * np.sin(2 * np.pi * (t + new_positions[:, 1]))
    new_positions[:, 1] += 0.05 * np.cos(2 * np.pi * (t + new_positions[:, 0]))
    
    # Update the scatter plot with the new positions
    scatter.set_offsets(new_positions)
    return scatter,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Create the scatter plot with the initial positions
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=100)

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

# Show the animation
plt.show()
