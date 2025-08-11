
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
frames = 100
fps = 24
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initial positions of lights (simplified model of a lying person)
initial_positions = np.array([
    [-0.1, 0.8],  # Head
    [0, 0.7],     # Neck
    [0, 0.6],     # Upper Spine
    [0, 0.5],     # Lower Spine
    [-0.1, 0.4],  # Left Shoulder
    [-0.1, 0.3],  # Left Elbow
    [-0.1, 0.2],  # Left Wrist
    [0.1, 0.4],   # Right Shoulder
    [0.1, 0.3],   # Right Elbow
    [0.1, 0.2],   # Right Wrist
    [-0.1, 0.1],  # Left Hip
    [-0.1, 0],    # Left Knee
    [-0.1, -0.1], # Left Ankle
    [0.1, 0.1],   # Right Hip
    [0.1, 0],     # Right Knee
    [0.1, -0.1]   # Right Ankle
])

# Create scatter plot for the lights
lights = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=100, color='white')

def update(frame):
    t = frame / frames * 2 * np.pi
    # Simple sinusoidal movement to simulate breathing and slight movement
    positions = initial_positions.copy()
    positions[:, 1] += 0.01 * np.sin(t)
    positions[0, 1] += 0.02 * np.sin(2 * t)  # Head movement
    positions[2, 1] += 0.01 * np.cos(t)    # Upper spine movement
    positions[4:6, 1] -= 0.01 * np.cos(t)  # Left arm movement
    positions[7:9, 1] -= 0.01 * np.cos(t)  # Right arm movement
    positions[10:12, 1] -= 0.01 * np.cos(t) # Left leg movement
    positions[13:15, 1] -= 0.01 * np.cos(t) # Right leg movement
    lights.set_offsets(positions)
    return lights,

ani = FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)
plt.show()
