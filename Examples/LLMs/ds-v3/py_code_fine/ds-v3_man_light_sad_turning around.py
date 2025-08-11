
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
import math

# Parameters
num_points = 15
fps = 30
duration = 5  # seconds
total_frames = fps * duration

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define key points for the sad man (relative positions)
# Head, shoulders, elbows, hands, hips, knees, feet
key_points = np.array([
    [0, 1.5],    # head
    [-0.5, 1.2], # left shoulder
    [0.5, 1.2],  # right shoulder
    [-0.7, 0.8], # left elbow
    [0.7, 0.8],  # right elbow
    [-0.0, 0.9], # torso center
    [-0.9, 0.5], # left hand
    [0.9, 0.5],  # right hand
    [-0.4, 0.5], # left hip
    [0.4, 0.5],  # right hip
    [-0.5, 0.0], # left knee
    [0.5, 0.0],  # right knee
    [-0.5, -0.6],# left foot
    [0.5, -0.6], # right foot
    [0.0, -0.3]  # lower torso (for balance)
])

# Function to rotate points around the origin
def rotate_points(points, angle):
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    return np.dot(points, rotation_matrix)

# Add slight movement to simulate walking while turning
def add_walking_motion(points, frame, total_frames):
    walk_cycle = frame / total_frames * 2 * np.pi
    # Sway arms and legs slightly
    arm_sway = 0.1 * np.sin(walk_cycle * 2)
    leg_sway = 0.1 * np.sin(walk_cycle)
    
    # Left arm (points 3, 6)
    points[3, 0] = -0.7 + arm_sway
    points[6, 0] = -0.9 + arm_sway * 1.5
    
    # Right arm (points 4, 7)
    points[4, 0] = 0.7 - arm_sway
    points[7, 0] = 0.9 - arm_sway * 1.5
    
    # Left leg (points 10, 12)
    points[10, 1] = 0.0 + leg_sway * 0.5
    points[12, 1] = -0.6 + leg_sway
    
    # Right leg (points 11, 13)
    points[11, 1] = 0.0 - leg_sway * 0.5
    points[13, 1] = -0.6 - leg_sway
    
    return points

# Animation update function
def update(frame):
    # Calculate rotation angle (full rotation over animation)
    angle = 2 * np.pi * frame / total_frames
    
    # Get current key points with walking motion
    current_points = add_walking_motion(key_points.copy(), frame, total_frames)
    
    # Rotate points
    rotated_points = rotate_points(current_points, angle)
    
    # Update point positions
    for i, point in enumerate(points):
        point.center = rotated_points[i]
    
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=total_frames, interval=1000/fps, blit=True)

plt.tight_layout()
plt.show()
