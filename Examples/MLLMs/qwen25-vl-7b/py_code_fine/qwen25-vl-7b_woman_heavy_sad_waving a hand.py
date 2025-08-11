
import numpy as np
import matplotlib.pyplot as plt

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, 0],  # Left shoulder
    [-1, 0], # Right shoulder
    [0, -1], # Left hip
    [0, -2], # Right hip
    [0, -3], # Left knee
    [0, -4], # Right knee
    [0, -5], # Left ankle
    [0, -6], # Right ankle
    [0, -7], # Left hand
    [0, -8], # Right hand
]

# Define the number of frames
num_frames = 15

# Define the time interval between frames
time_interval = 0.1

# Define the figure size
fig_size = (5, 5)

# Create the figure and axis
fig, ax = plt.subplots(figsize=fig_size)
ax.set_xlim(-2, 2)
ax.set_ylim(-9, 0)
ax.axis('off')

# Plot the initial position of the points
for pos in positions:
    ax.plot(pos[0], pos[1], 'o', color='white')

# Animate the points
def animate(i):
    # Update the positions of the points
    for j in range(len(positions)):
        positions[j][1] += 0.1 * (-1 if i % 2 == 0 else 1)
    
    # Plot the updated positions
    for pos in positions:
        ax.plot(pos[0], pos[1], 'o', color='white')
    
    # Update the frame number
    ax.text(0.5, -9.5, f'Frame {i}', ha='center', va='top', fontsize=12)

# Create the animation
ani = FuncAnimation(fig, animate, frames=num_frames, interval=time_interval*1000, repeat=False)

# Show the animation
plt.show()
