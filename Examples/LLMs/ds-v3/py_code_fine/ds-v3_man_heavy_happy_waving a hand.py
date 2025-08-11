
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
import math

# Number of point-lights
num_points = 15

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize point-lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define the motion of a waving hand (simplified)
def update(frame):
    t = frame * 0.1  # Time parameter
    
    # Body and legs (relatively static)
    body_x = 0
    body_y = np.sin(t * 0.2) * 0.1  # Slight sway
    
    # Head
    head_x = body_x
    head_y = body_y + 0.6
    
    # Shoulders
    shoulder_left_x = body_x - 0.3
    shoulder_left_y = body_y + 0.4
    shoulder_right_x = body_x + 0.3
    shoulder_right_y = body_y + 0.4
    
    # Elbows
    elbow_left_x = shoulder_left_x - 0.2
    elbow_left_y = shoulder_left_y - 0.2
    # Right elbow moves with waving motion
    elbow_right_x = shoulder_right_x + 0.2 + 0.1 * np.sin(t * 2)
    elbow_right_y = shoulder_right_y - 0.2 + 0.1 * np.cos(t * 2)
    
    # Hands
    hand_left_x = elbow_left_x - 0.2
    hand_left_y = elbow_left_y - 0.2
    # Right hand waves more prominently
    hand_right_x = elbow_right_x + 0.2 + 0.3 * np.sin(t * 2)
    hand_right_y = elbow_right_y - 0.2 + 0.3 * np.cos(t * 2)
    
    # Hips
    hip_left_x = body_x - 0.2
    hip_left_y = body_y - 0.2
    hip_right_x = body_x + 0.2
    hip_right_y = body_y - 0.2
    
    # Knees
    knee_left_x = hip_left_x
    knee_left_y = hip_left_y - 0.4
    knee_right_x = hip_right_x
    knee_right_y = hip_right_y - 0.4
    
    # Feet
    foot_left_x = knee_left_x
    foot_left_y = knee_left_y - 0.4
    foot_right_x = knee_right_x
    foot_right_y = knee_right_y - 0.4
    
    # Assign positions to points
    positions = [
        (head_x, head_y),  # Head
        (shoulder_left_x, shoulder_left_y),  # Left shoulder
        (shoulder_right_x, shoulder_right_y),  # Right shoulder
        (elbow_left_x, elbow_left_y),  # Left elbow
        (elbow_right_x, elbow_right_y),  # Right elbow
        (hand_left_x, hand_left_y),  # Left hand
        (hand_right_x, hand_right_y),  # Right hand
        (body_x, body_y),  # Body center
        (hip_left_x, hip_left_y),  # Left hip
        (hip_right_x, hip_right_y),  # Right hip
        (knee_left_x, knee_left_y),  # Left knee
        (knee_right_x, knee_right_y),  # Right knee
        (foot_left_x, foot_left_y),  # Left foot
        (foot_right_x, foot_right_y),  # Right foot
        (body_x, body_y - 0.1)  # Additional point for heaviness (e.g., belly)
    ]
    
    for i in range(num_points):
        points[i].center = positions[i]
    
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=False)

plt.title("Point-Light Animation: Heavy Person Waving")
plt.show()
