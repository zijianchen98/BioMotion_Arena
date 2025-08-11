
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches
import math

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initialize point positions (x, y)
points = np.zeros((num_points, 2))
scatter = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Parameters for the walking motion
time_step = 0.1
total_frames = 100
radius = 1.0  # Radius of the turning path
turn_speed = 0.1  # Speed of turning

# Approximate joint positions relative to the body's center of mass
# These are rough estimates for a human figure
joint_offsets = {
    'head': (0, 1.2),
    'shoulder_left': (-0.3, 0.8),
    'shoulder_right': (0.3, 0.8),
    'elbow_left': (-0.5, 0.5),
    'elbow_right': (0.5, 0.5),
    'hand_left': (-0.7, 0.2),
    'hand_right': (0.7, 0.2),
    'hip_left': (-0.2, 0.0),
    'hip_right': (0.2, 0.0),
    'knee_left': (-0.3, -0.6),
    'knee_right': (0.3, -0.6),
    'ankle_left': (-0.2, -1.2),
    'ankle_right': (0.2, -1.2),
    'foot_left': (-0.3, -1.4),
    'foot_right': (0.3, -1.4)
}

# Order of joints for the points (for consistency)
joint_names = [
    'head',
    'shoulder_left', 'shoulder_right',
    'elbow_left', 'elbow_right',
    'hand_left', 'hand_right',
    'hip_left', 'hip_right',
    'knee_left', 'knee_right',
    'ankle_left', 'ankle_right',
    'foot_left', 'foot_right'
]

# Function to update the points for each frame
def update(frame):
    angle = frame * turn_speed
    # Center of mass moves in a circular path (turning around)
    com_x = radius * np.cos(angle)
    com_y = radius * np.sin(angle)
    
    # Body lean (sad, heavy posture: slight forward lean)
    lean_angle = -0.2  # slight forward lean
    
    # Update each point's position relative to the center of mass
    new_points = np.zeros((num_points, 2))
    for i, joint in enumerate(joint_names):
        x_offset, y_offset = joint_offsets[joint]
        # Apply body lean (rotate offsets around COM)
        rotated_x = x_offset * np.cos(lean_angle) - y_offset * np.sin(lean_angle)
        rotated_y = x_offset * np.sin(lean_angle) + y_offset * np.cos(lean_angle)
        new_points[i, 0] = com_x + rotated_x
        new_points[i, 1] = com_y + rotated_y
    
    scatter.set_offsets(new_points)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=np.linspace(0, 2*np.pi, total_frames),
    interval=50, blit=True
)

plt.tight_layout()
plt.show()
