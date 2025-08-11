
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 30
dt = 1 / fps

# Initial positions of the lights (simplified model of a person sitting)
initial_positions = np.array([
    [0, 0],   # Head
    [-0.2, -0.5],  # Left Shoulder
    [0.2, -0.5],  # Right Shoulder
    [-0.4, -1],  # Left Elbow
    [0.4, -1],  # Right Elbow
    [-0.6, -1.5],  # Left Wrist
    [0.6, -1.5],  # Right Wrist
    [0, -1],  # Torso
    [-0.2, -2],  # Left Hip
    [0.2, -2],  # Right Hip
    [-0.4, -3],  # Left Knee
    [0.4, -3],  # Right Knee
    [-0.6, -4],  # Left Ankle
    [0.6, -4],  # Right Ankle
    [0, -2]  # Pelvis
])

# Function to update the position of the lights
def update(frame):
    t = frame * dt
    
    # Simple harmonic motion for sitting down
    head_y = -0.1 * np.sin(t)
    torso_y = -0.1 * np.sin(t)
    pelvis_y = -0.1 * np.sin(t)
    hip_y = -0.2 * np.sin(t) + 0.1
    knee_y = -0.3 * np.sin(t) + 0.2
    ankle_y = -0.4 * np.sin(t) + 0.3
    
    positions = initial_positions.copy()
    positions[0, 1] += head_y
    positions[8:, 1] += pelvis_y
    positions[[7, 14], 1] += torso_y
    positions[[9, 10], 1] += hip_y
    positions[[11, 12], 1] += knee_y
    positions[[13, 14], 1] += ankle_y
    
    sc.set_offsets(positions)
    return sc,

# Setup plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-5, 1)
ax.set_aspect('equal')
ax.axis('off')

sc = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=100, color='white')

# Animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

plt.show()
