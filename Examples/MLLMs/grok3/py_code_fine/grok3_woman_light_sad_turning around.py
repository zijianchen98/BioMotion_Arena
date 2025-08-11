
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of 15 point-lights for a human figure (simplified)
# These coordinates represent joints in a turning motion (e.g., head, shoulders, elbows, hips, knees, ankles)
initial_positions = np.array([
    [0, 10],  # Head
    [-1, 8],  # Left shoulder
    [-2, 6],  # Left elbow
    [-3, 4],  # Left wrist
    [1, 8],   # Right shoulder
    [2, 6],   # Right elbow
    [3, 4],   # Right wrist
    [-1, 5],  # Left hip
    [-2, 3],  # Left knee
    [-2, 1],  # Left ankle
    [1, 5],   # Right hip
    [2, 3],   # Right knee
    [2, 1],   # Right ankle
    [0, 7],   # Chest
    [0, 5]    # Pelvis
]) * 10  # Scale for visibility

# Parameters for turning motion
frames = 100
angle_increment = 360 / frames  # Full turn over 100 frames
positions = np.zeros((frames, 15, 2))

for i in range(frames):
    angle = np.radians(angle_increment * i)
    # Rotate around origin for turning motion
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    positions[i] = np.dot(initial_positions, rotation_matrix)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.axis('off')

# Create scatter plot for point-lights
scatter = ax.scatter([], [], c='white', s=100)

# Animation update function
def update(frame):
    scatter.set_offsets(positions[frame])
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=range(frames), interval=50, blit=True)

plt.show()
