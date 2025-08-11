
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2, 2)
ax.axis('off')

# Define 15 joint positions for a human figure (simplified for forward rolling)
# Initial positions (approximate for a rolling posture)
joint_positions = np.array([
    [0, 0],    # Head
    [0.3, -0.2], [0.3, -0.5], [0.3, -0.8],  # Right arm
    [-0.3, -0.2], [-0.3, -0.5], [-0.3, -0.8],  # Left arm
    [0.2, -1], [0, -1.2], [-0.2, -1],  # Torso
    [0.4, -1.5], [0.2, -1.7],  # Right leg
    [-0.4, -1.5], [-0.2, -1.7]  # Left leg
])

# Scatter plot for point lights
scatter = ax.scatter(joint_positions[:, 0], joint_positions[:, 1], c='white', s=50)

# Animation function
def update(frame):
    # Simulate forward rolling motion (simplified sinusoidal movement)
    angle = np.pi * frame / 50  # Rolling cycle over 50 frames
    roll_radius = 0.5
    center_y = -1 + roll_radius * np.sin(angle)
    center_x = roll_radius * np.cos(angle)

    # Update joint positions based on rolling motion
    new_positions = joint_positions.copy()
    for i in range(len(new_positions)):
        new_positions[i, 0] += center_x
        new_positions[i, 1] += center_y + 0.1 * np.sin(angle + i * 0.4)  # Add slight oscillation for natural motion

    scatter.set_offsets(new_positions)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
