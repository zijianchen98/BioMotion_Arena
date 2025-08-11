
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions for 15 point-lights (representing joints)
# Based on a simplified human model rolling forward
initial_positions = np.array([
    [0, 0],    # Head
    [0.5, 0.5], [0.5, -0.5],  # Shoulders
    [1, 1], [1, -1],  # Elbows
    [1.5, 1.5], [1.5, -1.5],  # Wrists
    [0, 1], [0, -1],  # Hips
    [0.5, 2], [0.5, -2],  # Knees
    [1, 2.5], [1, -2.5],  # Ankles
    [1.5, 3], [1.5, -3]   # Feet
]) * 0.1  # Scale down for visualization

# Number of frames for one complete roll cycle
n_frames = 100
t = np.linspace(0, 2 * np.pi, n_frames)

# Biomechanically plausible rolling motion (simplified sinusoidal movement)
def update(frame):
    angle = t[frame]
    # Rolling motion: rotate and translate points
    rotation = np.array([[np.cos(angle), -np.sin(angle)],
                         [np.sin(angle), np.cos(angle)]])
    translation = np.array([np.sin(angle) * 2, -np.abs(np.cos(angle)) * 2])
    positions = np.dot(initial_positions, rotation) + translation
    scatter.set_offsets(positions)
    return scatter,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 3)
ax.axis('off')

# Plot point-lights
scatter = ax.scatter([], [], c='white', s=50)

# Create animation
ani = FuncAnimation(fig, update, frames=n_frames, interval=50, blit=True)

plt.show()
