
import numpy as np
import matplotlib.pyplot as plt

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, -1],  # Left shoulder
    [-1, -1],  # Right shoulder
    [0, -2],  # Left hip
    [2, -2],  # Right hip
    [0, -3],  # Left knee
    [2, -3],  # Right knee
    [0, -4],  # Left ankle
    [2, -4]   # Right ankle
]

# Define the number of frames
num_frames = 10

# Define the time interval between frames
time_interval = 0.1

# Define the figure size
fig_size = (6, 6)

# Create the figure and axis
fig, ax = plt.subplots(figsize=fig_size)
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial position
for pos in positions:
    ax.plot(pos[0], pos[1], 'o', color='white')

# Animate the movement
for i in range(num_frames):
    # Update the positions of the points
    for j in range(len(positions)):
        positions[j][0] -= 0.1 * np.sin(2 * np.pi * i / num_frames)
        positions[j][1] += 0.1 * np.cos(2 * np.pi * i / num_frames)

    # Clear the previous frame
    ax.clear()

    # Plot the updated positions
    for pos in positions:
        ax.plot(pos[0], pos[1], 'o', color='white')

    # Show the current frame
    plt.pause(time_interval)

plt.show()
