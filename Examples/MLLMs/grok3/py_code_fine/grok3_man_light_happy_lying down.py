
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-3, 1)
ax.axis('off')

# Define initial positions for 15 point-lights (simplified human lying down pose)
# Head, shoulders, elbows, wrists, hips, knees, ankles, and torso points
initial_positions = np.array([
    [0, 0],      # Head
    [-0.5, -0.2], [-0.5, -0.4], [0.5, -0.2], [0.5, -0.4],  # Shoulders, elbows
    [-0.7, -0.6], [0.7, -0.6],  # Wrists
    [0, -0.8],   # Hips
    [-0.3, -1.2], [0.3, -1.2],  # Knees
    [-0.4, -1.8], [0.4, -1.8],  # Ankles
    [-0.2, -0.6], [0.2, -0.6], [0, -1]  # Torso points
])

# Breathing and slight arm/leg movement for realism
def update(frame):
    # Clear previous points
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-3, 1)
    ax.axis('off')

    # Small breathing motion (vertical shift)
    breath_amplitude = 0.05 * np.sin(frame * 0.1)
    # Slight arm and leg movement
    arm_amplitude = 0.05 * np.sin(frame * 0.15)
    leg_amplitude = 0.05 * np.sin(frame * 0.12)

    # Update positions with natural motion
    positions = initial_positions.copy()
    positions[0, 1] += breath_amplitude  # Head moves with breathing
    positions[1:5, 0] += arm_amplitude * np.array([-1, -1, 1, 1])  # Arm sway
    positions[8:12, 1] += leg_amplitude * np.array([-1, -1, 1, 1])  # Leg sway
    positions[5:7, 0] += arm_amplitude * np.array([-1, 1])  # Wrist sway
    positions[10:12, 1] += leg_amplitude * np.array([-1, 1])  # Ankle sway

    # Plot point-lights
    ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

    return ax

# Create animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=False)

plt.show()
