
import numpy as np
import matplotlib.pyplot as plt

# Define the positions of the points for the happywoman jumping forward
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
    [14, 0]  # Face
]

# Define the number of frames in the animation
num_frames = 15

# Create a figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(-1, 15)
ax.set_ylim(-1, 1)
ax.axis('off')

# Plot the initial position of the points
for pos in positions:
    ax.plot(pos[0], pos[1], 'o', color='white')

# Function to update the positions of the points
def update(frame):
    for i, pos in enumerate(positions):
        if frame % 3 == 0:
            pos[0] += 0.1  # Forward motion
        elif frame % 3 == 1:
            pos[0] -= 0.1  # Backward motion
        else:
            pos[0] += 0.1  # Forward motion
        pos[1] += 0.1  # Upward motion
    return [ax.plot(pos[0], pos[1], 'o', color='white') for pos in positions]

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=100)

plt.show()
