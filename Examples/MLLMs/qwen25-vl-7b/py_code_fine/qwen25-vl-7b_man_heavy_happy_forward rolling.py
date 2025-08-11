
import numpy as np
import matplotlib.pyplot as plt

# Define the positions of the points for the happyman with heavy weight forward rolling
positions = [
    [0, 0],  # Head
    [1, -1], # Left shoulder
    [2, -1], # Right shoulder
    [3, -1], # Left elbow
    [4, -1], # Right elbow
    [5, -1], # Left wrist
    [6, -1], # Right wrist
    [7, -1], # Left hand
    [8, -1], # Right hand
    [9, -1], # Left knee
    [10, -1],# Right knee
    [11, -1],# Left ankle
    [12, -1],# Right ankle
    [13, -1],# Left foot
    [14, -1] # Right foot
]

# Define the number of frames in the animation
num_frames = 15

# Create a figure and axis object
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Plot the initial position of the points
for pos in positions:
    ax.plot(pos[0], pos[1], 'o', color='white')

# Animate the points
for i in range(num_frames):
    # Update the positions of the points
    for j in range(len(positions)):
        positions[j][0] += (-1 if i % 2 == 0 else 1)
        positions[j][1] += (-1 if i % 3 == 0 else 1)

    # Clear the previous plot
    ax.clear()

    # Plot the updated positions of the points
    for pos in positions:
        ax.plot(pos[0], pos[1], 'o', color='white')

    # Set the limits of the plot
    ax.set_xlim(-2, 16)
    ax.set_ylim(-2, 16)

    # Show the plot
    plt.pause(0.1)

plt.show()
