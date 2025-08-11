
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the point-lights
def init_positions():
    # Define the initial positions of the 15 point-lights
    # These positions are roughly corresponding to key joints of a human body
    positions = np.array([
        [0, 0],  # Center of mass
        [-0.1, 0.8],  # Left shoulder
        [0.1, 0.8],  # Right shoulder
        [-0.2, 0.6],  # Left elbow
        [0.2, 0.6],  # Right elbow
        [-0.3, 0.4],  # Left hand
        [0.3, 0.4],  # Right hand
        [-0.1, 0.4],  # Left hip
        [0.1, 0.4],  # Right hip
        [-0.2, 0.2],  # Left knee
        [0.2, 0.2],  # Right knee
        [-0.3, 0.0],  # Left foot
        [0.3, 0.0],  # Right foot
        [0, 1.0],  # Head
        [0, -0.2]  # Center of mass (lower)
    ])
    return positions

# Update the positions of the point-lights for each frame
def update_positions(frame):
    t = frame / 60.0  # Time in seconds
    amplitude = 0.1  # Amplitude of the jump
    frequency = 1.0  # Frequency of the jump
    vertical_offset = 0.1  # Vertical offset to simulate the heavy weight

    # Update the positions based on a sine wave to simulate jumping
    for i in range(len(positions)):
        if i == 0 or i == 14:  # Center of mass and lower center of mass
            positions[i][1] += amplitude * np.sin(2 * np.pi * frequency * t) + vertical_offset
        else:
            positions[i][1] += amplitude * np.sin(2 * np.pi * frequency * t) * 0.7 + vertical_offset

    # Update the horizontal position to simulate forward movement
    for i in range(len(positions)):
        positions[i][0] += 0.01 * t

    scat.set_offsets(positions)

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
ax.axis('off')

# Initialize the scatter plot for the point-lights
positions = init_positions()
scat = ax.scatter(positions[:, 0], positions[:, 1], s=50, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, update_positions, frames=600, interval=20, repeat=True)

# Display the animation
plt.show()
