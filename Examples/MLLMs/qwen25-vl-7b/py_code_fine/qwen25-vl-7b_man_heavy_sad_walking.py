
import numpy as np
import matplotlib.pyplot as plt

# Define the positions of the points for the sadman walking
positions = [
    [0, 0],  # Head
    [1, -1], # Left shoulder
    [2, -1], # Right shoulder
    [3, -1], # Left hip
    [4, -1], # Right hip
    [5, -1], # Left knee
    [6, -1], # Right knee
    [7, -1], # Left ankle
    [8, -1], # Right ankle
]

# Define the number of frames in the animation
num_frames = 10

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 9)
ax.set_ylim(-2, 2)
ax.axis('off')

# Plot the initial position of the points
for pos in positions:
    ax.plot(pos[0], pos[1], 'o', color='white')

# Function to update the positions of the points
def update(frame):
    for i, pos in enumerate(positions):
        if frame % 2 == 0:
            positions[i][0] += 0.1 * (-1 if i % 2 == 0 else 1)
        else:
            positions[i][0] -= 0.1 * (-1 if i % 2 == 0 else 1)
        positions[i][1] += 0.1 * (-1 if i % 2 == 0 else 1)
    for pos in positions:
        ax.plot(pos[0], pos[1], 'o', color='white')
    return ax,

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=100, blit=True)

plt.show()
