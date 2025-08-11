
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

# Define the key points for the sad woman bowing
# Points order: head, neck, shoulders (2), elbows (2), hands (2), hips (2), knees (2), feet (2)
def get_positions(t):
    # Time parameter t ranges from 0 to 1 for the animation cycle
    
    # Head position - moves forward and slightly down
    head_x = 0.0
    head_y = 1.5 - 0.5 * math.sin(t * math.pi)
    
    # Neck position - follows head but less movement
    neck_x = 0.0
    neck_y = 1.3 - 0.3 * math.sin(t * math.pi)
    
    # Shoulders - move forward and slightly down
    shoulder_width = 0.5
    shoulder_y = 1.1 - 0.2 * math.sin(t * math.pi)
    left_shoulder_x = -shoulder_width
    right_shoulder_x = shoulder_width
    
    # Elbows - move forward and down with arms bending
    elbow_y = 0.9 - 0.4 * math.sin(t * math.pi)
    left_elbow_x = -0.4 - 0.1 * math.sin(t * math.pi)
    right_elbow_x = 0.4 + 0.1 * math.sin(t * math.pi)
    
    # Hands - move forward and down more
    hand_y = 0.7 - 0.6 * math.sin(t * math.pi)
    left_hand_x = -0.3 - 0.2 * math.sin(t * math.pi)
    right_hand_x = 0.3 + 0.2 * math.sin(t * math.pi)
    
    # Hips - slight movement forward
    hip_width = 0.4
    hip_y = 0.5 - 0.1 * math.sin(t * math.pi)
    left_hip_x = -hip_width
    right_hip_x = hip_width
    
    # Knees - bend forward
    knee_y = 0.2 - 0.3 * math.sin(t * math.pi)
    left_knee_x = -0.3
    right_knee_x = 0.3
    
    # Feet - stay on the ground but shift slightly
    foot_y = -0.2
    left_foot_x = -0.3 + 0.1 * math.sin(t * math.pi)
    right_foot_x = 0.3 - 0.1 * math.sin(t * math.pi)
    
    # Return all positions in order
    return [
        (head_x, head_y),          # 0: head
        (neck_x, neck_y),          # 1: neck
        (left_shoulder_x, shoulder_y),  # 2: left shoulder
        (right_shoulder_x, shoulder_y), # 3: right shoulder
        (left_elbow_x, elbow_y),   # 4: left elbow
        (right_elbow_x, elbow_y),  # 5: right elbow
        (left_hand_x, hand_y),     # 6: left hand
        (right_hand_x, hand_y),    # 7: right hand
        (left_hip_x, hip_y),       # 8: left hip
        (right_hip_x, hip_y),      # 9: right hip
        (left_knee_x, knee_y),     # 10: left knee
        (right_knee_x, knee_y),    # 11: right knee
        (left_foot_x, foot_y),     # 12: left foot
        (right_foot_x, foot_y),    # 13: right foot
        (0.0, hip_y - 0.1)         # 14: center of hips (additional point for better motion)
    ]

# Update function for animation
def update(frame):
    t = frame / 30  # 30 frames per cycle
    positions = get_positions(t)
    for i, point in enumerate(points):
        point.center = positions[i]
    return points

# Create the animation
ani = FuncAnimation(fig, update, frames=60, interval=50, blit=True)

plt.title('Biological Motion: Sad Woman Bowing', color='white')
plt.show()
