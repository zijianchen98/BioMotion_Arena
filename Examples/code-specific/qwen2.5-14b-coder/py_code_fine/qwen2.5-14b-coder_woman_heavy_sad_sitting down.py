
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
# These positions are based on a simplified model of a sitting woman with a heavy weight
initial_positions = np.array([
    [0.1, 0.5], [0.2, 0.5], [0.3, 0.5], [0.4, 0.5], [0.5, 0.5],
    [0.6, 0.5], [0.7, 0.5], [0.8, 0.5], [0.9, 0.5],
    [0.5, 0.6], [0.5, 0.7], [0.5, 0.8],
    [0.5, 0.9], [0.5, 1.0]
])

# Define the movement function
def update(frame):
    # Calculate the new positions based on the frame number
    # This is a simple example of how the points might move
    # In a real animation, this would be more complex and based on biomechanical principles
    t = frame / 100.0
    new_positions = initial_positions.copy()
    new_positions[:, 0] += 0.05 * np.sin(2 * np.pi * t)
    new_positions[10:, 1] -= 0.05 * np.cos(2 * np.pi * t)
    
    # Update the scatter plot
    scatter.set_offsets(new_positions)
    return scatter,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Create the scatter plot
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=100)

# Create the animation
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Show the animation
plt.show()
