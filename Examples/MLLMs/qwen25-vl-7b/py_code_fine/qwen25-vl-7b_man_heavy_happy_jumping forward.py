
import numpy as np
import matplotlib.pyplot as plt

# Define the positions of the points for the happyman jumping forward
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
    [10, 0], # Left hand
    [11, 0], # Right hand
    [12, 0], # Head
    [13, 0], # Neck
    [14, 0]  # Body
]

# Define the number of frames in the animation
num_frames = 15

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial position of the points
for pos in positions:
    ax.plot(pos[0], pos[1], 'o', color='white')

# Animate the points
for i in range(num_frames):
    # Update the positions of the points
    for j in range(len(positions)):
        positions[j][0] += 0.1 * (-1 if j % 2 == 0 else 1)
        positions[j][1] += 0.1 * (-1 if j % 2 == 0 else 1)

    # Clear the previous plot
    ax.clear()

    # Plot the updated positions of the points
    for pos in positions:
        ax.plot(pos[0], pos[1], 'o', color='white')

    # Show the current frame
    plt.pause(0.1)

plt.show()
