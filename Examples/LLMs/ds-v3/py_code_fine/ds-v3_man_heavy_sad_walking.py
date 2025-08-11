
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches

# Parameters
num_points = 15
num_frames = 60  # Number of frames in the animation
fps = 30  # Frames per second

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize point positions (x, y) for 15 points
points = np.zeros((num_points, 2))
scatter = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Function to update point positions for each frame
def update(frame):
    t = frame * 2 * np.pi / num_frames  # Time parameter
    
    # Body motion parameters
    walk_speed = 0.1
    step_length = 0.5
    body_sway = 0.1
    arm_swing = 0.3
    leg_swing = 0.4
    head_bob = 0.05
    
    # Base positions (relative to body)
    # Head
    head_x = 0
    head_y = 1.5 + head_bob * np.sin(t * 2)
    
    # Shoulders
    shoulder_y = 1.2 + body_sway * np.sin(t)
    left_shoulder_x = -0.2
    right_shoulder_x = 0.2
    
    # Arms
    left_arm_angle = np.pi/4 + arm_swing * np.sin(t * 2)
    right_arm_angle = np.pi/4 + arm_swing * np.sin(t * 2 + np.pi)
    
    left_elbow_x = left_shoulder_x + 0.3 * np.cos(left_arm_angle)
    left_elbow_y = shoulder_y - 0.3 * np.sin(left_arm_angle)
    right_elbow_x = right_shoulder_x + 0.3 * np.cos(right_arm_angle)
    right_elbow_y = shoulder_y - 0.3 * np.sin(right_arm_angle)
    
    left_hand_x = left_elbow_x + 0.3 * np.cos(left_arm_angle - 0.2)
    left_hand_y = left_elbow_y - 0.3 * np.sin(left_arm_angle - 0.2)
    right_hand_x = right_elbow_x + 0.3 * np.cos(right_arm_angle - 0.2)
    right_hand_y = right_elbow_y - 0.3 * np.sin(right_arm_angle - 0.2)
    
    # Hips
    hip_y = 0.8 + body_sway * np.sin(t + np.pi)
    left_hip_x = -0.15
    right_hip_x = 0.15
    
    # Legs
    left_leg_angle = -np.pi/6 + leg_swing * np.sin(t * 2 + np.pi/2)
    right_leg_angle = -np.pi/6 + leg_swing * np.sin(t * 2 + 3*np.pi/2)
    
    left_knee_x = left_hip_x + 0.4 * np.sin(left_leg_angle)
    left_knee_y = hip_y - 0.4 * np.cos(left_leg_angle)
    right_knee_x = right_hip_x + 0.4 * np.sin(right_leg_angle)
    right_knee_y = hip_y - 0.4 * np.cos(right_leg_angle)
    
    left_foot_x = left_knee_x + 0.4 * np.sin(left_leg_angle - 0.2)
    left_foot_y = left_knee_y - 0.4 * np.cos(left_leg_angle - 0.2)
    right_foot_x = right_knee_x + 0.4 * np.sin(right_leg_angle - 0.2)
    right_foot_y = right_knee_y - 0.4 * np.cos(right_leg_angle - 0.2)
    
    # Torso points
    torso_mid_y = (shoulder_y + hip_y) / 2
    
    # Forward movement (walking)
    forward_offset = walk_speed * t
    
    # Assign positions to points (15 points)
    points = np.array([
        [head_x + forward_offset, head_y],            # 0: Head
        [left_shoulder_x + forward_offset, shoulder_y], # 1: Left shoulder
        [right_shoulder_x + forward_offset, shoulder_y], # 2: Right shoulder
        [left_elbow_x + forward_offset, left_elbow_y],  # 3: Left elbow
        [right_elbow_x + forward_offset, right_elbow_y], # 4: Right elbow
        [left_hand_x + forward_offset, left_hand_y],    # 5: Left hand
        [right_hand_x + forward_offset, right_hand_y],  # 6: Right hand
        [left_hip_x + forward_offset, hip_y],           # 7: Left hip
        [right_hip_x + forward_offset, hip_y],          # 8: Right hip
        [left_knee_x + forward_offset, left_knee_y],    # 9: Left knee
        [right_knee_x + forward_offset, right_knee_y],  # 10: Right knee
        [left_foot_x + forward_offset, left_foot_y],    # 11: Left foot
        [right_foot_x + forward_offset, right_foot_y],  # 12: Right foot
        [0 + forward_offset, torso_mid_y],              # 13: Torso middle
        [0 + forward_offset, (torso_mid_y + hip_y)/2]   # 14: Lower torso
    ])
    
    scatter.set_offsets(points)
    return scatter,

# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, interval=1000/fps, blit=True
)

plt.tight_layout()
plt.show()
