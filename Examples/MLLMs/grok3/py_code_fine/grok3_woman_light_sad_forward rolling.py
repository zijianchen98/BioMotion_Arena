
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of 15 point-lights for a sad woman forward rolling
# Approximate joint positions (x, y) in a normalized coordinate system (-1 to 1)
initial_positions = np.array([
    [0.0, 0.8],  # Head
    [0.1, 0.6],  # Right shoulder
    [-0.1, 0.6], # Left shoulder
    [0.2, 0.4],  # Right elbow
    [-0.2, 0.4], # Left elbow
    [0.3, 0.2],  # Right wrist
    [-0.3, 0.2], # Left wrist
    [0.1, 0.0],  # Right hip
    [-0.1, 0.0], # Left hip
    [0.2, -0.2], # Right knee
    [-0.2, -0.2],# Left knee
    [0.3, -0.4], # Right ankle
    [-0.3, -0.4],# Left ankle
    [0.0, -0.6], # Pelvis
    [0.0, 0.7]   # Chest
])

# Number of frames for the animation
frames = 100
positions = np.zeros((frames, 15, 2))

# Simulate forward rolling motion (simplified biomechanical model)
for i in range(frames):
    t = i / frames * 2 * np.pi  # One complete roll
    angle = t
    # Rotate and translate points to simulate rolling
    for j in range(15):
        x, y = initial_positions[j]
        # Rotate around the center (pelvis initially at origin)
        new_x = x * np.cos(angle) - y * np.sin(angle)
        new_y = x * np.sin(angle) + y * np.cos(angle)
        # Translate and adjust for rolling motion
        positions[i, j, 0] = new_x + np.sin(t) * 0.5
        positions[i, j, 1] = new_y + np.cos(t) * 0.5 - 0.1 * np.sin(t)  # Slight vertical oscillation

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot
scatter = ax.scatter([], [], c='white', s=50)

# Animation update function
def update(frame):
    scatter.set_offsets(positions[frame])
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

# Display the animation
plt.show()
