
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points for the happyman running
positions = [
    [0.5, 0.5],  # Head
    [0.4, 0.6],  # Left shoulder
    [0.6, 0.6],  # Right shoulder
    [0.3, 0.7],  # Left elbow
    [0.7, 0.7],  # Right elbow
    [0.2, 0.8],  # Left hand
    [0.8, 0.8],  # Right hand
    [0.4, 0.9],  # Left hip
    [0.6, 0.9],  # Right hip
    [0.3, 1.0],  # Left knee
    [0.7, 1.0],  # Right knee
    [0.4, 1.1],  # Left ankle
    [0.6, 1.1]   # Right ankle
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Smoothly interpolate between frames
    positions = np.interp(frame, [0, 15], positions)
    return positions,

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Plot the initial position of the points
points, = ax.plot(*zip(*positions), 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(16), interval=50, blit=True)

# Show the animation
plt.show()
