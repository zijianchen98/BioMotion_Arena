
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions for 15 point-lights representing a lying down human
# Approximate joint positions for a simplified lying down posture
initial_positions = np.array([
    [0, 0],    # Head
    [0.5, 0.5], # Right shoulder
    [-0.5, 0.5], # Left shoulder
    [1, 1],    # Right elbow
    [-1, 1],   # Left elbow
    [1.5, 1.5], # Right wrist
    [-1.5, 1.5], # Left wrist
    [0, 2],    # Hip
    [0.5, 2.5], # Right knee
    [-0.5, 2.5], # Left knee
    [0.5, 3.5], # Right ankle
    [-0.5, 3.5], # Left ankle
    [0.2, 2.2], # Right hip joint
    [-0.2, 2.2], # Left hip joint
    [0, 0.2]    # Neck
]) * 10  # Scale up for visibility

# Breathing and slight natural movement simulation
def update(frame):
    # Small sinusoidal movement for breathing and natural shifts
    movement = np.sin(frame * 0.1) * 0.2
    positions = initial_positions.copy()
    # Simulate slight chest and hip movement
    positions[0] += [0, movement]  # Head
    positions[7] += [0, -movement]  # Hip
    positions[1:3] += [0, movement * 0.5]  # Shoulders
    positions[12:14] += [0, -movement * 0.5]  # Hip joints
    scatter.set_offsets(positions)
    return scatter,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-20, 20)
ax.set_ylim(-5, 40)
ax.axis('off')

# Create scatter plot for point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=100)

# Create animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

plt.show()
