
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
import math

# Parameters
num_points = 15
fps = 30
duration = 2  # seconds
total_frames = fps * duration

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define keyframes for the jumping motion
def get_keyframe(t):
    # Normalized time [0, 1]
    t_norm = t / total_frames
    
    # Jumping motion parameters
    jump_height = 1.5
    forward_distance = 1.0
    squat_depth = 0.2
    
    # Vertical motion: squat -> jump -> land -> recover
    if t_norm < 0.2:
        # Squatting down
        y_offset = -squat_depth * (t_norm / 0.2)
    elif t_norm < 0.5:
        # Jumping up
        phase = (t_norm - 0.2) / 0.3
        y_offset = -squat_depth + (jump_height + squat_depth) * (1 - (2 * phase - 1)**2)
    elif t_norm < 0.8:
        # Landing
        phase = (t_norm - 0.5) / 0.3
        y_offset = -squat_depth * phase
    else:
        # Recovering
        y_offset = -squat_depth * (1 - (t_norm - 0.8) / 0.2)
    
    # Forward motion
    x_offset = forward_distance * t_norm
    
    # Body parts positions relative to the center of mass
    # Head
    head_x = 0
    head_y = 0.6 + y_offset
    
    # Shoulders
    shoulder_y = 0.3 + y_offset
    left_shoulder_x = -0.2
    right_shoulder_x = 0.2
    
    # Elbows
    elbow_y = 0.2 + y_offset
    left_elbow_x = -0.3
    right_elbow_x = 0.3
    
    # Hands
    hand_swing = 0.3 * math.sin(2 * math.pi * t_norm * 2)
    left_hand_x = left_elbow_x - 0.2
    left_hand_y = elbow_y - 0.2 + hand_swing
    right_hand_x = right_elbow_x + 0.2
    right_hand_y = elbow_y - 0.2 - hand_swing
    
    # Hips
    hip_y = y_offset
    left_hip_x = -0.15
    right_hip_x = 0.15
    
    # Knees
    knee_bend = 0.2 * math.sin(2 * math.pi * t_norm * 2 + math.pi/2)
    left_knee_x = left_hip_x
    left_knee_y = hip_y - 0.3 - knee_bend
    right_knee_x = right_hip_x
    right_knee_y = hip_y - 0.3 - knee_bend
    
    # Feet
    left_foot_x = left_knee_x
    left_foot_y = left_knee_y - 0.3 + knee_bend
    right_foot_x = right_knee_x
    right_foot_y = right_knee_y - 0.3 + knee_bend
    
    # Combine all points with forward movement
    points_pos = [
        (head_x + x_offset, head_y),           # 0: head
        (left_shoulder_x + x_offset, shoulder_y),  # 1: left shoulder
        (right_shoulder_x + x_offset, shoulder_y), # 2: right shoulder
        (left_elbow_x + x_offset, elbow_y),    # 3: left elbow
        (right_elbow_x + x_offset, elbow_y),   # 4: right elbow
        (left_hand_x + x_offset, left_hand_y), # 5: left hand
        (right_hand_x + x_offset, right_hand_y), # 6: right hand
        (left_hip_x + x_offset, hip_y),        # 7: left hip
        (right_hip_x + x_offset, hip_y),       # 8: right hip
        (left_knee_x + x_offset, left_knee_y), # 9: left knee
        (right_knee_x + x_offset, right_knee_y), # 10: right knee
        (left_foot_x + x_offset, left_foot_y), # 11: left foot
        (right_foot_x + x_offset, right_foot_y), # 12: right foot
        (x_offset, hip_y),                     # 13: torso center
        (x_offset, (head_y + hip_y)/2)         # 14: neck
    ]
    
    return points_pos

# Animation update function
def update(frame):
    positions = get_keyframe(frame)
    for i, point in enumerate(points):
        point.center = positions[i]
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=total_frames, interval=1000/fps, blit=True)

plt.tight_layout()
plt.show()
