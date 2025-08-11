
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Define initial positions for 15 point-lights (simplified human lying down)
# Joints: head, shoulders, elbows, wrists, hips, knees, ankles, torso points
initial_positions = np.array([
    [0, 0],    # head
    [-1, 0.5], # left shoulder
    [-2, 0.5], # left elbow
    [-3, 0.5], # left wrist
    [1, 0.5],  # right shoulder
    [2, 0.5],  # right elbow
    [3, 0.5],  # right wrist
    [0, 0],    # torso top
    [0, -0.5], # torso middle
    [0, -1],   # torso bottom
    [-0.5, -1],# left hip
    [-0.5, -2],# left knee
    [-0.5, -3],# left ankle
    [0.5, -1], # right hip
    [0.5, -2], # right knee
    [0.5, -3]  # right ankle
]) * 10  # Scale for visibility

# Breathing and slight limb movement for realism
def update(frame):
    positions = initial_positions.copy()
    # Simulate breathing (vertical torso movement)
    breath_amplitude = 0.5 * np.sin(frame * 0.1)
    positions[7:10, 1] += breath_amplitude  # Torso points
    # Slight limb oscillation
    for i in [2, 3, 6, 11, 12, 15]:  # Elbows, wrists, knees, ankles
        positions[i, 0] += 0.2 * np.sin(frame * 0.15 + i)
        positions[i, 1] += 0.2 * np.cos(frame * 0.15 + i)
    scat.set_offsets(positions)
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-40, 40)
ax.set_ylim(-40, 40)
ax.axis('off')

# Create scatter plot for point-lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Create animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

plt.show()
