
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions for 15 point-lights (simplified human lying down pose)
# Joints: head, shoulders, elbows, wrists, hips, knees, ankles, torso points
initial_positions = np.array([
    [0, 0],    # head
    [-1, 0.5], # left shoulder
    [-2, 0.5], # left elbow
    [-3, 0.5], # left wrist
    [1, 0.5],  # right shoulder
    [2, 0.5],  # right elbow
    [3, 0.5],  # right wrist
    [0, 0],    # torso center
    [-0.5, -0.5], # left hip
    [-0.5, -1.5], # left knee
    [-0.5, -2.5], # left ankle
    [0.5, -0.5],  # right hip
    [0.5, -1.5],  # right knee
    [0.5, -2.5],  # right ankle
    [0, -0.2]     # lower torso
]) * 10  # Scale up for visibility

# Breathing and slight trembling motion (simplified for lying down)
def update(frame):
    t = frame * 0.1
    # Breathing motion (vertical oscillation)
    breath = 0.5 * np.sin(t)
    # Slight trembling (random small movements)
    tremble = 0.1 * np.random.randn(15, 2)
    # New positions with natural motion
    new_positions = initial_positions.copy()
    new_positions[:, 1] += breath + tremble[:, 1]  # Vertical motion for breathing and tremble
    scat.set_offsets(new_positions)
    return scat,

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-40, 40)
ax.set_ylim(-30, 30)
ax.axis('off')

# Scatter plot for point-lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=100)

# Create animation
ani = FuncAnimation(fig, update, frames=range(200), interval=50, blit=True)

plt.show()
