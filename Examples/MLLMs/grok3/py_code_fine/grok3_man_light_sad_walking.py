
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions for 15 point-lights (simplified human stick figure walking)
# Joints: head, shoulders, elbows, wrists, hips, knees, ankles
def initial_positions():
    return np.array([
        [0, 10],  # head
        [-2, 8], [2, 8],  # shoulders
        [-4, 6], [4, 6],  # elbows
        [-6, 4], [6, 4],  # wrists
        [0, 0], [-2, 0], [2, 0],  # hips
        [-3, -4], [1, -4],  # knees
        [-4, -8], [0, -8]  # ankles
    ])

# Update function for animation
def update(frame):
    # Simulate walking motion with biomechanical plausibility
    t = frame * 0.1  # Time parameter
    positions = initial_positions().copy()

    # Head bobbing slightly
    positions[0, 1] += np.sin(t) * 0.5

    # Shoulder and arm movement
    positions[1:5, 0] += np.sin(t) * 0.5  # Left arm forward, right arm back
    positions[1:5, 1] += np.sin(t + np.pi) * 0.5

    # Hip and leg movement (alternating legs)
    positions[5:9, 0] += np.sin(t) * 1.0  # Hips sway
    positions[9:11, 0] += np.cos(t) * 2.0  # Legs alternate
    positions[9:11, 1] += np.sin(t) * 1.5
    positions[11:, 0] += np.cos(t + np.pi) * 2.0  # Ankles follow
    positions[11:, 1] += np.sin(t + np.pi) * 1.5

    # Translate forward to simulate walking
    positions[:, 0] += t * 2

    scat.set_offsets(positions)
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-10, 20)
ax.set_ylim(-10, 10)
ax.axis('off')

# Create scatter plot for point-lights
scat = ax.scatter([], [], c='white', s=50)

# Create animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
