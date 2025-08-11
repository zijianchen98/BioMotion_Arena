
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions for 15 point-lights (simplified human figure)
# Joints: head, shoulders, elbows, wrists, hips, knees, ankles, torso points
initial_positions = np.array([
    [0, 10],  # head
    [-2, 8], [-2, 6],  # left shoulder, elbow
    [2, 8], [2, 6],    # right shoulder, elbow
    [-1, 4], [-1, 2],  # left hip, knee
    [1, 4], [1, 2],    # right hip, knee
    [-1.5, 0],         # left ankle
    [1.5, 0],          # right ankle
    [0, 7], [0, 5],    # torso points
    [-0.5, 3], [0.5, 3] # additional weight effect
])

# Parameters for jumping motion
jump_height = 5
jump_duration = 50  # frames for one jump cycle
gravity = 0.1
heaviness_factor = 0.5  # slower movement due to heavy weight

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-2, 12)
ax.axis('off')

# Scatter plot for point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Animation function
def update(frame):
    t = frame % jump_duration
    if t < jump_duration / 2:
        # Ascending phase
        height = jump_height * np.sin(np.pi * t / (jump_duration / 2)) - heaviness_factor * t * gravity
    else:
        # Descending phase
        height = jump_height * np.sin(np.pi * (t - jump_duration / 2) / (jump_duration / 2)) - heaviness_factor * (t - jump_duration / 2) * gravity
    
    # Update positions with natural joint movement
    positions = initial_positions.copy()
    positions[:, 1] += height  # Vertical jump motion
    # Add slight bending for knees and elbows during jump
    if t < jump_duration / 2:
        bend = 0.5 * np.sin(np.pi * t / (jump_duration / 2))
    else:
        bend = 0.5 * np.sin(np.pi * (t - jump_duration / 2) / (jump_duration / 2))
    positions[3, 1] -= bend  # left elbow
    positions[5, 1] -= bend  # left knee
    positions[7, 1] -= bend  # right elbow
    positions[9, 1] -= bend  # right knee
    
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

plt.show()
