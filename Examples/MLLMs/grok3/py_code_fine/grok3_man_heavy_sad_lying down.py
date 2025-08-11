
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions of 15 point-lights (simplified human lying down pose)
# Joints: head, shoulders, elbows, wrists, hips, knees, ankles
initial_positions = np.array([
    [0, 0],    # head
    [-1, 0.5], # left shoulder
    [-2, 0.5], # left elbow
    [-3, 0.5], # left wrist
    [1, 0.5],  # right shoulder
    [2, 0.5],  # right elbow
    [3, 0.5],  # right wrist
    [0, -0.5], # spine
    [-0.5, -1],# left hip
    [-0.5, -2],# left knee
    [-0.5, -3],# left ankle
    [0.5, -1], # right hip
    [0.5, -2], # right knee
    [0.5, -3], # right ankle
    [0, -0.5]  # pelvis (repeated for stability)
]) * 10  # Scale up for visibility

# Breathing and slight trembling motion (simulating heavy weight and sadness)
def update(frame):
    t = frame * 0.1
    # Small sinusoidal motion for breathing
    breath = 0.2 * np.sin(t)
    # Slight trembling (random noise for realism)
    tremble = 0.05 * np.random.randn(15, 2)
    
    # Update positions with breathing and trembling
    new_positions = initial_positions.copy()
    new_positions[:, 1] += breath + tremble[:, 1]  # Vertical motion for breathing
    new_positions[:, 0] += tremble[:, 0]           # Horizontal trembling
    
    scatter.set_offsets(new_positions)
    return scatter,

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-40, 40)
ax.set_ylim(-40, 40)
ax.axis('off')

# Create scatter plot for point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=100)

# Create animation
ani = FuncAnimation(fig, update, frames=range(200), interval=50, blit=True)

plt.show()
