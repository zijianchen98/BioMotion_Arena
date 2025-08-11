
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, 0],  # Left shoulder
    [-1, 0], # Right shoulder
    [0, -1], # Left hip
    [0, 1],  # Right hip
    [0, 2],  # Left knee
    [0, 3],  # Right knee
    [0, 4],  # Left ankle
    [0, 5],  # Right ankle
]

# Define the number of frames
num_frames = 15

# Define the function to update the positions of the points
def update(frame):
    global positions
    # Wave the hand
    if frame % 2 == 0:
        positions[6][1] += 0.1  # Left knee up
        positions[7][1] -= 0.1  # Right knee down
    else:
        positions[6][1] -= 0.1  # Left knee down
        positions[7][1] += 0.1  # Right knee up
    
    # Ensure the points stay within the frame
    for i in range(len(positions)):
        positions[i][0] = max(-1, min(1, positions[i][0]))
        positions[i][1] = max(-1, min(5, positions[i][1]))

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 5.5)
ax.axis('off')

# Plot the points
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Initialize the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=100, blit=True)

plt.show()
