
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rcParams

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points, = ax.plot([], [], 'wo', markersize=8)

# Parameters for the turning motion
frames_per_cycle = 100
total_frames = 200  # Two full turns

# Define the positions of the point-lights relative to the body
# These are approximate positions for a human figure (head, shoulders, elbows, hands, hips, knees, feet)
# Coordinates are in a local frame that will be rotated
body_points = np.array([
    [0, 1.5],    # head
    [-0.5, 1.2], [0.5, 1.2],  # shoulders
    [-0.7, 0.8], [0.7, 0.8],  # elbows
    [-0.9, 0.4], [0.9, 0.4],  # hands
    [-0.4, 0.5], [0.4, 0.5],  # hips
    [-0.4, 0.0], [0.4, 0.0],  # knees
    [-0.4, -0.5], [0.4, -0.5],  # ankles
    [-0.3, -1.0], [0.3, -1.0]   # feet
])

# Add slight movement to limbs to make it more natural
def get_body_position(frame):
    # Rotate the body
    angle = 2 * np.pi * (frame % frames_per_cycle) / frames_per_cycle
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    # Rotate the body points
    rotated_points = np.dot(body_points, rotation_matrix)
    
    # Add some arm and leg movement
    arm_swing = 0.2 * np.sin(2 * np.pi * frame / (frames_per_cycle / 2))
    leg_swing = 0.1 * np.sin(2 * np.pi * frame / (frames_per_cycle / 2) + np.pi)
    
    # Modify arm and leg positions
    modified_points = rotated_points.copy()
    # Left arm (points 3, 5)
    modified_points[3, 0] += 0.1 * arm_swing
    modified_points[5, 0] += 0.2 * arm_swing
    # Right arm (points 4, 6)
    modified_points[4, 0] -= 0.1 * arm_swing
    modified_points[6, 0] -= 0.2 * arm_swing
    # Left leg (points 9, 11, 13)
    modified_points[9, 0] += 0.1 * leg_swing
    modified_points[11, 0] += 0.1 * leg_swing
    modified_points[13, 0] += 0.1 * leg_swing
    # Right leg (points 10, 12, 14)
    modified_points[10, 0] -= 0.1 * leg_swing
    modified_points[12, 0] -= 0.1 * leg_swing
    modified_points[14, 0] -= 0.1 * leg_swing
    
    return modified_points

# Animation update function
def update(frame):
    current_points = get_body_position(frame)
    points.set_data(current_points[:, 0], current_points[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=total_frames, interval=50, blit=True
)

plt.tight_layout()
plt.show()
