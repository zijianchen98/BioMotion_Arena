
import numpy as np
import matplotlib.pyplot as plt

# Define the positions of the points for the sadman forward rolling
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

# Define the number of frames in the animation
num_frames = 15

# Create a figure and axis
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
        positions[j][0] += (-1)**j * 0.1  # Forward rolling motion
        positions[j][1] += (-1)**(j+1) * 0.1  # Rolling motion
    
    # Clear the previous frame
    ax.clear()
    
    # Plot the updated positions of the points
    for pos in positions:
        ax.plot(pos[0], pos[1], 'o', color='white')
    
    # Show the current frame
    plt.pause(0.1)

plt.show()
