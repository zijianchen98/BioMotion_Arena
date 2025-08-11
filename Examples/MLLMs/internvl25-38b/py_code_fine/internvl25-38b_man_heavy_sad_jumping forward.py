
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Initialize positions for the sadman with heavy weight
positions = np.array([
    [0.0, 0.0],  # Head
    [-0.1, -0.1], [0.1, -0.1],  # Shoulders
    [-0.2, -0.3], [0.2, -0.3],  # Hips
    [-0.3, -0.5], [-0.15, -0.6], [-0.05, -0.65],  # Left Leg
    [0.3, -0.5], [0.15, -0.6], [0.05, -0.65],  # Right Leg
    [-0.15, -0.45], [-0.05, -0.55], [-0.02, -0.6],  # Left Arm
    [0.15, -0.45], [0.05, -0.55], [0.02, -0.6]  # Right Arm
])

# Function to update positions for jumping motion
def update_position(frame):
    t = 2 * np.pi * frame / 60
    amplitude = 0.2
    phase_offset = np.array([0, np.pi, np.pi, 0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
    
    # Vertical jump motion
    jump_motion = amplitude * np.sin(t + phase_offset)
    positions[:, 1] = -np.linspace(0.0, 0.6, 15) + jump_motion
    
    # Horizontal jump motion
    if frame < 30:
        positions[:, 0] += 0.002
    elif frame > 30:
        positions[:, 0] -= 0.002

    scatter.set_offsets(positions)

# Create figure and scatter points
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.6, 0.2)
ax.axis('off')
scatter = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

# Animation
ani = animation.FuncAnimation(fig, update_position, frames=60, interval=50, repeat=True)

plt.show()
