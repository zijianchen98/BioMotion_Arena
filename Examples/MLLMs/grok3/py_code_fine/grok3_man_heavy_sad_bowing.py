
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define 15 point-light positions for a bowing sadman (approximated joints)
# Initial positions (upright posture)
joints = np.array([
    [0, 0],    # pelvis
    [0, 0.1],  # lower spine
    [0, 0.2],  # upper spine
    [0, 0.3],  # neck
    [0, 0.4],  # head
    [-0.1, 0], # left hip
    [-0.2, -0.2], # left knee
    [-0.1, -0.4], # left ankle
    [0.1, 0],  # right hip
    [0.2, -0.2],  # right knee
    [0.1, -0.4],  # right ankle
    [-0.1, 0.2],  # left shoulder
    [-0.2, 0.1],  # left elbow
    [-0.3, 0],   # left wrist
    [0.1, 0.2]   # right shoulder
])

# Scatter plot for point-lights
scatter = ax.scatter(joints[:, 0], joints[:, 1], c='white', s=50)

# Animation function
def update(frame):
    # Simulate bowing motion (forward bend with slight sway)
    angle = np.deg2rad(30 * (1 - np.cos(np.pi * frame / 100)))  # Smooth bowing over 100 frames
    rot_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    # Apply rotation to upper body (spine, neck, head, shoulders, arms)
    upper_body_indices = [1, 2, 3, 4, 11, 12, 13, 14]
    upper_body = joints[upper_body_indices] - joints[0]  # Relative to pelvis
    upper_body = (rot_matrix @ upper_body.T).T + joints[0]
    joints[upper_body_indices] = upper_body
    
    # Adjust legs slightly for balance (simple forward shift)
    leg_indices = [5, 6, 7, 8, 9, 10]
    joints[leg_indices] += [0, -0.1 * np.sin(angle)]
    
    # Update scatter points
    scatter.set_offsets(joints)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
