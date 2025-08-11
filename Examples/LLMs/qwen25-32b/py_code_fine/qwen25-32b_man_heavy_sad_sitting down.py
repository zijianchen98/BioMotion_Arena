
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights representing the sadman with heavy weight sitting down
initial_positions = np.array([
    [0.5, 1.0],  # Head
    [0.4, 0.8],  # Left shoulder
    [0.6, 0.8],  # Right shoulder
    [0.3, 0.6],  # Left elbow
    [0.7, 0.6],  # Right elbow
    [0.2, 0.4],  # Left hand
    [0.8, 0.4],  # Right hand
    [0.5, 0.7],  # Spine
    [0.4, 0.5],  # Left hip
    [0.6, 0.5],  # Right hip
    [0.3, 0.3],  # Left knee
    [0.7, 0.3],  # Right knee
    [0.2, 0.1],  # Left foot
    [0.8, 0.1],  # Right foot
    [0.5, 0.9]   # Center of mass
])

# Define the trajectory of each point-light over time
def update_position(frame, positions):
    # Simplified model for sitting down motion
    angle = np.pi / 12 * frame
    if frame <= 12:
        positions[:, 1] -= 0.05  # Moving down
        positions[8:14, 1] -= 0.1  # Lower body moves faster
    else:
        positions[:, 1] += 0.03  # Slight bounce after landing
    positions[0:7, 1] += np.sin(angle) * 0.05  # Upper body sway
    return positions

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

def animate(frame):
    updated_positions = update_position(frame, initial_positions.copy())
    scat.set_offsets(updated_positions)

ani = FuncAnimation(fig, animate, frames=24, interval=100, repeat=True)
plt.show()
