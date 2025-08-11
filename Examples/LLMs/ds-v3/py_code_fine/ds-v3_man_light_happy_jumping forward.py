
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches

# Parameters
num_points = 15
num_frames = 60
fps = 30

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.set_aspect('equal')
ax.axis('off')

# Initialize point lights
points = ax.scatter([], [], color='white', s=50)

# Define keyframes for the jumping motion
def get_keyframe(t):
    # Normalized time [0, 1]
    t_norm = t / num_frames
    
    # Jumping motion parameters
    jump_height = 1.5
    forward_distance = 1.0
    body_lean = 0.2 * np.sin(2 * np.pi * t_norm)
    
    # Vertical position (parabolic jump)
    if t_norm < 0.5:
        y_pos = jump_height * 4 * t_norm * (1 - t_norm * 2)
    else:
        y_pos = jump_height * 4 * (1 - t_norm) * (2 * t_norm - 1)
    
    # Forward movement
    x_pos = forward_distance * t_norm
    
    # Body parts positions (simplified model)
    head_x = x_pos + body_lean
    head_y = 1.7 + y_pos
    
    shoulder_x = x_pos + body_lean
    shoulder_y = 1.4 + y_pos
    
    hip_x = x_pos - body_lean
    hip_y = 1.0 + y_pos
    
    # Left arm (sinusoidal movement)
    left_arm_angle = np.pi/3 * np.sin(2 * np.pi * t_norm)
    left_elbow_x = shoulder_x - 0.3 * np.cos(left_arm_angle)
    left_elbow_y = shoulder_y - 0.3 * np.sin(left_arm_angle)
    left_hand_x = left_elbow_x - 0.25 * np.cos(left_arm_angle + np.pi/6)
    left_hand_y = left_elbow_y - 0.25 * np.sin(left_arm_angle + np.pi/6)
    
    # Right arm (opposite phase)
    right_arm_angle = np.pi/3 * np.sin(2 * np.pi * t_norm + np.pi)
    right_elbow_x = shoulder_x + 0.3 * np.cos(right_arm_angle)
    right_elbow_y = shoulder_y - 0.3 * np.sin(right_arm_angle)
    right_hand_x = right_elbow_x + 0.25 * np.cos(right_arm_angle + np.pi/6)
    right_hand_y = right_elbow_y - 0.25 * np.sin(right_arm_angle + np.pi/6)
    
    # Legs (alternating movement)
    left_leg_angle = np.pi/4 * np.sin(2 * np.pi * t_norm + np.pi/2)
    left_knee_x = hip_x - 0.3 * np.cos(left_leg_angle)
    left_knee_y = hip_y - 0.3 * np.sin(left_leg_angle)
    left_foot_x = left_knee_x - 0.4 * np.cos(left_leg_angle - np.pi/6)
    left_foot_y = left_knee_y - 0.4 * np.sin(left_leg_angle - np.pi/6)
    
    right_leg_angle = np.pi/4 * np.sin(2 * np.pi * t_norm - np.pi/2)
    right_knee_x = hip_x + 0.3 * np.cos(right_leg_angle)
    right_knee_y = hip_y - 0.3 * np.sin(right_leg_angle)
    right_foot_x = right_knee_x + 0.4 * np.cos(right_leg_angle - np.pi/6)
    right_foot_y = right_knee_y - 0.4 * np.sin(right_leg_angle - np.pi/6)
    
    # Combine all points
    point_positions = np.array([
        [head_x, head_y],            # head
        [shoulder_x, shoulder_y],    # shoulder
        [hip_x, hip_y],              # hip
        
        # Left arm
        [left_elbow_x, left_elbow_y],
        [left_hand_x, left_hand_y],
        
        # Right arm
        [right_elbow_x, right_elbow_y],
        [right_hand_x, right_hand_y],
        
        # Left leg
        [left_knee_x, left_knee_y],
        [left_foot_x, left_foot_y],
        
        # Right leg
        [right_knee_x, right_knee_y],
        [right_foot_x, right_foot_y],
        
        # Additional points for more detail
        [shoulder_x - 0.1, shoulder_y + 0.1],  # left shoulder detail
        [shoulder_x + 0.1, shoulder_y + 0.1],  # right shoulder detail
        [hip_x - 0.1, hip_y - 0.1],            # left hip detail
        [hip_x + 0.1, hip_y - 0.1]             # right hip detail
    ])
    
    return point_positions

# Animation update function
def update(frame):
    pos = get_keyframe(frame)
    points.set_offsets(pos)
    return points,

# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, interval=1000/fps, blit=True
)

plt.tight_layout()
plt.show()
