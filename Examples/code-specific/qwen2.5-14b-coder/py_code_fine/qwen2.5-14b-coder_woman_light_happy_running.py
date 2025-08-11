
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
# These positions are based on a simplified model of a running woman
initial_positions = np.array([
    [0.1, 0.2], [0.2, 0.3], [0.3, 0.4], [0.4, 0.5], [0.5, 0.6],
    [0.6, 0.5], [0.7, 0.4], [0.8, 0.3], [0.9, 0.2], [0.8, 0.1],
    [0.7, 0.2], [0.6, 0.3], [0.5, 0.4], [0.4, 0.5], [0.3, 0.6]
])

# Define the movement pattern for each point light
# This is a simplified model of the running motion
def update(frame):
    # Calculate the new positions based on the frame number
    new_positions = initial_positions + np.array([0.01 * frame, 0])
    
    # Wrap around the positions to simulate running
    new_positions[:, 0] = np.mod(new_positions[:, 0], 1)
    
    # Update the scatter plot
    scat.set_offsets(new_positions)
    return scat,

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=100)

# Create the animation
ani = FuncAnimation(fig, update, frames=100, blit=True, repeat=True)

# Show the animation
plt.show()
