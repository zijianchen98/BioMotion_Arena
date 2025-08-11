
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Left foot
    [1, 0],  # Right foot
    [2, 0],  # Left knee
    [3, 0],  # Right knee
    [4, 0],  # Left hip
    [5, 0],  # Right hip
    [6, 0],  # Left shoulder
    [7, 0],  # Right shoulder
    [8, 0],  # Left elbow
    [9, 0],  # Right elbow
    [10, 0], # Left wrist
    [11, 0], # Right wrist
    [12, 0], # Left hand
    [13, 0], # Right hand
    [14, 0]  # Head
]

# Define the number of frames
num_frames = 15

# Define the function to update the positions
def update(frame):
    global positions
    # Update the positions based on the jump action
    if frame == 0:
        positions[0][1] = -1  # Left foot
        positions[1][1] = -1  # Right foot
        positions[2][1] = -1  # Left knee
        positions[3][1] = -1  # Right knee
        positions[4][1] = -1  # Left hip
        positions[5][1] = -1  # Right hip
        positions[6][1] = -1  # Left shoulder
        positions[7][1] = -1  # Right shoulder
        positions[8][1] = -1  # Left elbow
        positions[9][1] = -1  # Right elbow
        positions[10][1] = -1  # Left wrist
        positions[11][1] = -1  # Right wrist
        positions[12][1] = -1  # Left hand
        positions[13][1] = -1  # Right hand
        positions[14][1] = -1  # Head
    elif frame == 1:
        positions[0][1] = 0  # Left foot
        positions[1][1] = 0  # Right foot
        positions[2][1] = 0  # Left knee
        positions[3][1] = 0  # Right knee
        positions[4][1] = 0  # Left hip
        positions[5][1] = 0  # Right hip
        positions[6][1] = 0  # Left shoulder
        positions[7][1] = 0  # Right shoulder
        positions[8][1] = 0  # Left elbow
        positions[9][1] = 0  # Right elbow
        positions[10][1] = 0  # Left wrist
        positions[11][1] = 0  # Right wrist
        positions[12][1] = 0  # Left hand
        positions[13][1] = 0  # Right hand
        positions[14][1] = 0  # Head
    else:
        positions[0][1] = 1  # Left foot
        positions[1][1] = 1  # Right foot
        positions[2][1] = 1  # Left knee
        positions[3][1] = 1  # Right knee
        positions[4][1] = 1  # Left hip
        positions[5][1] = 1  # Right hip
        positions[6][1] = 1  # Left shoulder
        positions[7][1] = 1  # Right shoulder
        positions[8][1] = 1  # Left elbow
        positions[9][1] = 1  # Right elbow
        positions[10][1] = 1  # Left wrist
        positions[11][1] = 1  # Right wrist
        positions[12][1] = 1  # Left hand
        positions[13][1] = 1  # Right hand
        positions[14][1] = 1  # Head

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 16)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis('off')

# Plot the points
points, = ax.plot([], [], 'o', markersize=10, color='white')

# Initialize the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=100)

# Display the animation
plt.show()
