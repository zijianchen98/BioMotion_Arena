
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, 0],  # Right shoulder
    [-1, 0],  # Left shoulder
    [2, 0],  # Right hip
    [-2, 0],  # Left hip
    [1, 1],  # Right elbow
    [-1, 1],  # Left elbow
    [2, -1],  # Right knee
    [-2, -1],  # Left knee
    [1.5, 0],  # Right hand
    [-1.5, 0],  # Left hand
    [1.5, -1],  # Right foot
    [-1.5, -1],  # Left foot
]

# Function to update the positions of the points
def update(frame):
    global positions
    # Simulate a sitting down motion
    for i in range(len(positions)):
        if i % 2 == 0:  # Even indices (shoulders, hips)
            positions[i][1] -= 0.05 * frame  # Lowering the body
        else:  # Odd indices (elbows, knees, hands, feet)
            positions[i][1] += 0.05 * frame  # Moving them slightly up
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.axis('off')

# Plot the initial positions
points, = ax.plot(*zip(*positions), 'o', color='white')

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
