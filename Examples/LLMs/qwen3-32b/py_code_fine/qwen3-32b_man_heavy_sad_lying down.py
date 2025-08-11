
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

# Define the joint positions of a human body (15 joints)
# These are relative positions for a human lying down with a heavy, sad posture
# Coordinates are in (x, y) format, with (0, 0) at the center of the body
joint_names = [
    'left_ankle', 'left_knee', 'left_hip',
    'right_ankle', 'right_knee', 'right_hip',
    'spine_base', 'spine_mid', 'spine_shoulder',
    'left_shoulder', 'left_elbow', 'left_wrist',
    'right_shoulder', 'right_elbow', 'right_wrist'
]

# Initial joint positions (lying down with heavy posture)
# y-axis is vertical, x-axis is horizontal
# Coordinates are in arbitrary units; we will scale them later
initial_positions = np.array([
    [-0.4, -0.8], [-0.4, -0.4], [-0.4, 0.0],  # left leg
    [0.4, -0.8], [0.4, -0.4], [0.4, 0.0],     # right leg
    [0.0, 0.0], [0.0, 0.4], [0.0, 0.8],       # spine
    [-0.3, 1.0], [-0.3, 0.7], [-0.3, 0.4],    # left arm
    [0.3, 1.0], [0.3, 0.7], [0.3, 0.4]        # right arm
])

# Normalize to unit scale
initial_positions = initial_positions / 1.5

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create the point-light dots
dots = [plt.scatter(x, y, c='white', s=100) for x, y in initial_positions]

# Define the number of frames and time between frames
num_frames = 60
interval = 100  # milliseconds

# Define the motion over time
def update(frame):
    t = frame / num_frames * 2 * np.pi  # time in [0, 2pi]
    
    # Apply a slow, heavy motion to simulate sadness and lying down
    # We will add small, slow oscillations to joints to simulate breathing and slight sagging
    motion_factor = 0.02 * (1 - math.cos(t * 0.5))  # slow sine wave for sagging
    
    # Move joints with a sad, heavy posture
    for i, (x, y) in enumerate(initial_positions):
        if joint_names[i] in ['left_hip', 'right_hip', 'spine_base', 'spine_mid', 'spine_shoulder']:
            # Sagging motion for lower body and spine
            y += motion_factor * 0.5
        elif joint_names[i] in ['left_shoulder', 'left_elbow', 'left_wrist', 'right_shoulder', 'right_elbow', 'right_wrist']:
            # Slight droop in arms
            y -= motion_factor * 0.3
        elif joint_names[i] in ['left_knee', 'right_knee']:
            # Slight bending of knees
            y += motion_factor * 0.2
        elif joint_names[i] in ['left_ankle', 'right_ankle']:
            # Slight sinking of feet
            y -= motion_factor * 0.1

        dots[i].set_offsets([x, y])

    return dots

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=interval, blit=True)

# Display the animation
plt.show()
