
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
import math

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define the key points for the sad man bowing
# Points are ordered as: head, neck, shoulders (left and right), elbows, wrists, hips (left and right), knees, ankles
def get_positions(t):
    # Time parameter t is in [0, 2pi]
    # Head bobs down and up
    head_y = 1.5 - 0.5 * (1 + math.sin(t))
    
    # Neck follows head but less movement
    neck_y = 1.3 - 0.3 * (1 + math.sin(t))
    
    # Shoulders move slightly forward and back
    shoulder_left_x = -0.3 - 0.1 * math.sin(t)
    shoulder_right_x = 0.3 + 0.1 * math.sin(t)
    shoulder_y = 1.2 - 0.2 * (1 + math.sin(t))
    
    # Elbows move as if holding heavy weight
    elbow_left_x = -0.4 - 0.1 * math.sin(t)
    elbow_right_x = 0.4 + 0.1 * math.sin(t)
    elbow_y = 0.9 - 0.3 * (1 + math.sin(t))
    
    # Wrists move more, as if arms are hanging
    wrist_left_x = -0.5 - 0.2 * math.sin(t)
    wrist_right_x = 0.5 + 0.2 * math.sin(t)
    wrist_y = 0.5 - 0.4 * (1 + math.sin(t))
    
    # Hips move slightly
    hip_left_x = -0.2 - 0.05 * math.sin(t)
    hip_right_x = 0.2 + 0.05 * math.sin(t)
    hip_y = 0.7 - 0.1 * (1 + math.sin(t))
    
    # Knees bend as if bowing
    knee_left_x = -0.2
    knee_right_x = 0.2
    knee_y = 0.3 - 0.3 * (1 + math.sin(t))
    
    # Ankles move less
    ankle_left_x = -0.2
    ankle_right_x = 0.2
    ankle_y = 0.1 - 0.1 * (1 + math.sin(t))
    
    # Toes (for completeness)
    toe_left_x = -0.3
    toe_right_x = 0.3
    toe_y = 0.0
    
    # Return all positions in order
    return [
        (0.0, head_y),  # head
        (0.0, neck_y),  # neck
        (shoulder_left_x, shoulder_y),  # left shoulder
        (shoulder_right_x, shoulder_y),  # right shoulder
        (elbow_left_x, elbow_y),  # left elbow
        (elbow_right_x, elbow_y),  # right elbow
        (wrist_left_x, wrist_y),  # left wrist
        (wrist_right_x, wrist_y),  # right wrist
        (hip_left_x, hip_y),  # left hip
        (hip_right_x, hip_y),  # right hip
        (knee_left_x, knee_y),  # left knee
        (knee_right_x, knee_y),  # right knee
        (ankle_left_x, ankle_y),  # left ankle
        (ankle_right_x, ankle_y),  # right ankle
        (0.0, toe_y)  # center toe (for balance)
    ]

# Update function for animation
def update(frame):
    t = frame * 0.1  # Slow down the animation
    positions = get_positions(t)
    for i, point in enumerate(points):
        point.center = positions[i]
    return points

# Create the animation
ani = FuncAnimation(fig, update, frames=63, interval=50, blit=True)

plt.tight_layout()
plt.show()
