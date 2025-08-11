
import numpy as np
import matplotlib.pyplot as plt

# Define the positions of the points for the sadman jumping up
positions = [
    [0, 0],  # Head
    [1, -1],  # Left shoulder
    [-1, -1],  # Right shoulder
    [0, -2],  # Left hip
    [2, -2],  # Right hip
    [0, -3],  # Left knee
    [2, -3],  # Right knee
    [0, -4],  # Left ankle
    [2, -4],  # Right ankle
]

# Number of frames in the animation
num_frames = 15

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')

# Plot the initial position
for pos in positions:
    ax.plot(pos[0], pos[1], 'o', color='white')

# Animate the jump
for i in range(num_frames):
    # Update the positions of the points
    for j in range(len(positions)):
        if j == 0:  # Head
            positions[j][1] += 0.1 * (-1)**i  # Jumping up
        elif j == 1 or j == 2:  # Shoulders
            positions[j][1] += 0.1 * (-1)**i  # Jumping up
        elif j == 3 or j == 4:  # Hips
            positions[j][1] += 0.1 * (-1)**i  # Jumping up
        elif j == 5 or j == 6:  # Knees
            positions[j][1] += 0.1 * (-1)**i  # Jumping up
        elif j == 7 or j == 8:  # Ankles
            positions[j][1] += 0.1 * (-1)**i  # Jumping up
    
    # Clear the previous plot
    ax.clear()
    
    # Plot the updated positions
    for pos in positions:
        ax.plot(pos[0], pos[1], 'o', color='white')
    
    # Show the current frame
    plt.pause(0.1)

plt.show()
