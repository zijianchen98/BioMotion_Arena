
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, -1],  # Right shoulder
    [-1, -1],  # Left shoulder
    [2, -2],  # Right hip
    [-2, -2],  # Left hip
    [1, -3],  # Right knee
    [-1, -3],  # Left knee
    [1.5, -4],  # Right ankle
    [-1.5, -4]  # Left ankle
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Simulate a smooth movement towards a bowing position
    for i in range(len(positions)):
        if i % 2 == 0:
            # Head and shoulders move upwards
            positions[i][1] += 0.1 * np.sin(frame / 10)
        else:
            # Hips, knees, and ankles move downwards
            positions[i][1] -= 0.1 * np.sin(frame / 10)
    
    # Ensure positions stay within bounds
    for i in range(len(positions)):
        positions[i][1] = max(-5, min(0, positions[i][1]))

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-5, 0)
ax.axis('off')

# Plot the points
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Initialize the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, init_func=lambda: None)

plt.show()
