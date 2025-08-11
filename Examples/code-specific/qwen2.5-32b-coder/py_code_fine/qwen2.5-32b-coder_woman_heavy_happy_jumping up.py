
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
frames = 100
fps = 30
dt = 1 / fps
g = 9.81  # acceleration due to gravity

# Initial positions and velocities
np.random.seed(42)
positions = np.zeros((num_lights, 2))
velocities = np.zeros((num_lights, 2))

# Define joints and their initial positions
joints = {
    'head': (0, 1),
    'neck': (0, 0.7),
    'shoulder_left': (-0.3, 0.7),
    'elbow_left': (-0.6, 0.4),
    'hand_left': (-0.9, 0.3),
    'shoulder_right': (0.3, 0.7),
    'elbow_right': (0.6, 0.4),
    'hand_right': (0.9, 0.3),
    'hip': (0, -0.1),
    'knee_left': (-0.3, -0.4),
    'foot_left': (-0.3, -0.8),
    'knee_right': (0.3, -0.4),
    'foot_right': (0.3, -0.8),
}

# Convert joint positions to list
positions[:len(joints)] = list(joints.values())

# Function to update positions
def update(frame):
    global positions, velocities

    # Simple physics for jumping motion
    if frame < frames // 2:
        velocities[:, 1] -= g * dt
    else:
        velocities[:, 1] += g * dt

    positions += velocities * dt

    # Reset position after landing
    if positions[-1, 1] < -1:
        positions[:, 1] = np.array(list(joints.values()))[:, 1]
        velocities[:, 1] = np.random.uniform(3, 5, num_lights)

    scatter.set_offsets(positions)
    return scatter,

# Setup plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')
scatter = ax.scatter(positions[:, 0], positions[:, 1], s=100, color='white')

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

plt.show()
