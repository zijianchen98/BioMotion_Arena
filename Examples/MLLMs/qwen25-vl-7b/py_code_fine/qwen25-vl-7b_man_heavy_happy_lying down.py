
import numpy as np
import matplotlib.pyplot as plt

# Define the positions of the points
positions = [
    [0, 0],  # Head
    [1, 0],  # Right shoulder
    [-1, 0],  # Left shoulder
    [2, -1],  # Right hip
    [-2, -1],  # Left hip
    [1, -2],  # Right knee
    [-1, -2],  # Left knee
    [0, -3],  # Right ankle
    [0, -4],  # Left ankle
]

# Define the number of frames
num_frames = 15

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-3, 3)
ax.set_ylim(-5, 1)
ax.axis('off')

# Plot the initial position
for pos in positions:
    ax.plot(pos[0], pos[1], 'o', color='white', markersize=10)

# Animate the points
def animate(i):
    # Update the positions of the points
    for j, pos in enumerate(positions):
        if i % 3 == 0:
            positions[j][0] += 0.1 * (-1)**j
        elif i % 3 == 1:
            positions[j][1] += 0.1 * (-1)**j
        else:
            positions[j][0] -= 0.1 * (-1)**j
            positions[j][1] -= 0.1 * (-1)**j

    # Clear the previous frame
    ax.clear()

    # Plot the updated positions
    for pos in positions:
        ax.plot(pos[0], pos[1], 'o', color='white', markersize=10)

# Create the animation
ani = FuncAnimation(fig, animate, frames=num_frames, interval=100, repeat=False)

# Save the animation as a GIF
ani.save('point_light_stimulus.gif', writer='imagemagick', fps=15)

plt.show()
