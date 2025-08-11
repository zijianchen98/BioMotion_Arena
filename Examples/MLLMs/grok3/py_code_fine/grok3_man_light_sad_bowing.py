
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of 15 point-lights for a bowing human figure
# Coordinates are approximate and represent key joints in a simplified human model
initial_positions = np.array([
    [0, 10],  # Head
    [0, 8],   # Neck
    [0, 6],   # Chest
    [0, 4],   # Hips
    [-1, 2],  # Left knee
    [-1, 0],  # Left ankle
    [1, 2],   # Right knee
    [1, 0],   # Right ankle
    [-2, 6],  # Left shoulder
    [-3, 4],  # Left elbow
    [-4, 2],  # Left wrist
    [2, 6],   # Right shoulder
    [3, 4],   # Right elbow
    [4, 2],   # Right wrist
    [0, 3]    # Pelvis
])

# Number of frames for the animation
frames = 60
positions = np.zeros((frames, 15, 2))

# Simulate bowing motion: head and upper body move downward, legs bend slightly
for i in range(frames):
    t = i / frames
    angle = np.pi * t / 2  # Bowing angle increases over time
    # Head and upper body movement
    positions[i, 0, 1] = initial_positions[0, 1] - 6 * t  # Head moves down
    positions[i, 1, 1] = initial_positions[1, 1] - 5 * t  # Neck follows
    positions[i, 2, 1] = initial_positions[2, 1] - 4 * t  # Chest follows
    positions[i, 4, 1] = initial_positions[4, 1] - 2 * t  # Left knee bends
    positions[i, 5, 1] = initial_positions[5, 1] - 1 * t  # Left ankle adjusts
    positions[i, 6, 1] = initial_positions[6, 1] - 2 * t  # Right knee bends
    positions[i, 7, 1] = initial_positions[7, 1] - 1 * t  # Right ankle adjusts
    # Arms move slightly inward
    positions[i, 8, 0] = initial_positions[8, 0] - 0.5 * t
    positions[i, 10, 0] = initial_positions[10, 0] - 0.5 * t
    positions[i, 11, 0] = initial_positions[11, 0] + 0.5 * t
    positions[i, 13, 0] = initial_positions[13, 0] + 0.5 * t
    # Copy initial positions for other points with adjustments
    for j in range(15):
        if j not in [0, 1, 2, 4, 5, 6, 7, 8, 10, 11, 13]:
            positions[i, j] = initial_positions[j]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-1, 11)
ax.set_xticks([])
ax.set_yticks([])
scatter = ax.scatter([], [], c='white', s=100)

# Animation update function
def update(frame):
    scatter.set_offsets(positions[frame])
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.show()
