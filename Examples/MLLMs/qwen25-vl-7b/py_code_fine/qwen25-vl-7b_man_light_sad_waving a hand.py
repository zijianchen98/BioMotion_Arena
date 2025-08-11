
import numpy as np
import matplotlib.pyplot as plt

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, 0],  # Right shoulder
    [-1, 0], # Left shoulder
    [2, 1],  # Right elbow
    [0, 1],  # Right wrist
    [2, -1], # Right hip
    [0, -1], # Left hip
    [1, -2], # Right knee
    [-1, -2],# Left knee
    [2, -3], # Right ankle
    [0, -3], # Left ankle
    [1, -4], # Right hand
    [-1, -4] # Left hand
]

# Define the number of frames
num_frames = 100

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial position
ax.plot(*zip(*positions), 'o', color='white')

# Animate the points
for i in range(num_frames):
    # Update the positions of the points
    positions[0][1] -= 0.01  # Head moves down
    positions[1][1] += 0.01  # Right shoulder moves up
    positions[2][1] += 0.01  # Left shoulder moves up
    positions[3][1] -= 0.01  # Right elbow moves down
    positions[4][1] -= 0.01  # Right wrist moves down
    positions[5][1] += 0.01  # Right hip moves up
    positions[6][1] += 0.01  # Left hip moves up
    positions[7][1] -= 0.01  # Right knee moves down
    positions[8][1] -= 0.01  # Left knee moves down
    positions[9][1] -= 0.01  # Right ankle moves down
    positions[10][1] -= 0.01  # Left ankle moves down
    positions[11][1] -= 0.01  # Right hand moves down
    positions[12][1] -= 0.01  # Left hand moves down
    
    # Plot the updated positions
    ax.clear()
    ax.plot(*zip(*positions), 'o', color='white')
    fig.canvas.draw()

plt.show()
