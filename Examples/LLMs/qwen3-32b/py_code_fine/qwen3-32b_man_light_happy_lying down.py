
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Define the joints of the human figure (15 joints)
# Joints are represented as positions relative to the body center
joints = [
    [0.0, 0.0],        # Center of mass
    [0.0, 0.3],        # Head
    [-0.1, 0.1],       # Left shoulder
    [0.1, 0.1],        # Right shoulder
    [-0.2, -0.1],      # Left upper arm
    [0.2, -0.1],       # Right upper arm
    [-0.2, -0.3],      # Left lower arm
    [0.2, -0.3],       # Right lower arm
    [-0.1, -0.4],      # Left hip
    [0.1, -0.4],       # Right hip
    [-0.2, -0.6],      # Left upper leg
    [0.2, -0.6],       # Right upper leg
    [-0.2, -0.9],      # Left lower leg
    [0.2, -0.9],       # Right lower leg
    [0.0, -1.1],       # Feet (combined)
]

# Convert joints to numpy array
joints = np.array(joints)

# Create scatter points for the joints
points, = ax.plot([], [], 'o', color='white', markersize=8)

# Define the motion of the joints over time
# We'll simulate a lying down pose with some small oscillations to make it natural
def update(frame):
    # Base positions for lying down
    base_positions = np.array([
        [0.0, 0.0],
        [0.0, 0.3],
        [-0.1, 0.1],
        [0.1, 0.1],
        [-0.2, -0.1],
        [0.2, -0.1],
        [-0.2, -0.3],
        [0.2, -0.3],
        [-0.1, -0.4],
        [0.1, -0.4],
        [-0.2, -0.6],
        [0.2, -0.6],
        [-0.2, -0.9],
        [0.2, -0.9],
        [0.0, -1.1],
    ])

    # Add small oscillations to make the animation more natural
    oscillation = 0.01 * np.sin(2 * np.pi * (frame + np.arange(len(joints))) / 30)
    positions = base_positions + oscillation

    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=60, interval=1000//30, blit=True)

plt.show()
