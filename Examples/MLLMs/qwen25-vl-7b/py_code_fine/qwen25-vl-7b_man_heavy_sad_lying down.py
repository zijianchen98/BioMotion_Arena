
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

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial position
for pos in positions:
    ax.plot(pos[0], pos[1], 'o', color='white')

# Animate the movement
for frame in range(num_frames):
    for i, pos in enumerate(positions):
        # Move each point slightly along a sine wave
        new_pos = [pos[0] + np.sin(frame * 0.1), pos[1] + np.cos(frame * 0.1)]
        positions[i] = new_pos
    ax.clear()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-5, 0)
    ax.plot([p[0] for p in positions], [p[1] for p in positions], 'o-', color='white')
    plt.pause(0.1)

plt.show()
