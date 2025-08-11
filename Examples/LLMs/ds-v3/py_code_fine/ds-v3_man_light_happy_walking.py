
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches

# Parameters
num_points = 15
num_frames = 60
fps = 30

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Initialize point lights
points = ax.scatter([], [], color='white', s=50)

# Define the walking motion
def walking_motion(t):
    # Key points for a walking motion (simplified)
    # Head, shoulders, elbows, hands, hips, knees, feet
    # Positions are relative to the body's center (x, y)
    
    # Time-dependent parameters
    stride_length = 1.5
    leg_swing = 0.5 * np.sin(2 * np.pi * t)
    arm_swing = 0.3 * np.sin(2 * np.pi * t + np.pi)
    body_bob = 0.1 * np.sin(4 * np.pi * t)
    
    # Body position
    x_pos = t * stride_length / num_frames * 2
    
    # Points: head, shoulders, elbows, hands, hips, knees, feet
    points_x = np.zeros(num_points)
    points_y = np.zeros(num_points)
    
    # Head (0)
    points_x[0] = x_pos
    points_y[0] = 1.6 + body_bob
    
    # Shoulders (1, 2)
    points_x = 0.3
    points_y_shoulder = 1.3 + body_bob
    points_x[1] = x_pos - points_x  # Left shoulder
    points_y[1] = points_y_shoulder
    points_x[2] = x_pos + points_x  # Right shoulder
    points_y[2] = points_y_shoulder
    
    # Elbows (3, 4)
    elbow_offset = 0.2
    points_x[3] = x_pos - points_x + elbow_offset * np.cos(arm_swing)  # Left elbow
    points_y[3] = points_y_shoulder - 0.2 + elbow_offset * np.sin(arm_swing)
    points_x[4] = x_pos + points_x - elbow_offset * np.cos(arm_swing)  # Right elbow
    points_y[4] = points_y_shoulder - 0.2 - elbow_offset * np.sin(arm_swing)
    
    # Hands (5, 6)
    hand_offset = 0.3
    points_x[5] = x_pos - points_x + hand_offset * np.cos(arm_swing + 0.2)  # Left hand
    points_y[5] = points_y_shoulder - 0.4 + hand_offset * np.sin(arm_swing + 0.2)
    points_x[6] = x_pos + points_x - hand_offset * np.cos(arm_swing + 0.2)  # Right hand
    points_y[6] = points_y_shoulder - 0.4 - hand_offset * np.sin(arm_swing + 0.2)
    
    # Hips (7, 8)
    hip_x = 0.2
    points_y_hip = 0.8 + body_bob
    points_x[7] = x_pos - hip_x  # Left hip
    points_y[7] = points_y_hip
    points_x[8] = x_pos + hip_x  # Right hip
    points_y[8] = points_y_hip
    
    # Knees (9, 10)
    knee_offset = 0.3
    points_x[9] = x_pos - hip_x  # Left knee
    points_y[9] = points_y_hip - knee_offset + 0.1 * leg_swing
    points_x[10] = x_pos + hip_x  # Right knee
    points_y[10] = points_y_hip - knee_offset - 0.1 * leg_swing
    
    # Feet (11, 12)
    foot_offset = 0.2
    points_x[11] = x_pos - hip_x + foot_offset * np.sin(leg_swing)  # Left foot
    points_y[11] = points_y_hip - knee_offset - 0.2 + 0.1 * np.cos(leg_swing)
    points_x[12] = x_pos + hip_x - foot_offset * np.sin(leg_swing)  # Right foot
    points_y[12] = points_y_hip - knee_offset - 0.2 - 0.1 * np.cos(leg_swing)
    
    # Additional points for more detail (e.g., torso, mid-leg)
    # Torso midpoint (13)
    points_x[13] = x_pos
    points_y[13] = 1.05 + body_bob
    
    # Mid-leg points (14)
    points_x[14] = x_pos
    points_y[14] = 0.4 + body_bob
    
    return points_x, points_y

# Animation update function
def update(frame):
    t = frame / num_frames * 2  # Two strides
    x, y = walking_motion(t)
    points.set_offsets(np.column_stack((x, y)))
    return points,

# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, interval=1000/fps, blit=True
)

plt.tight_layout()
plt.show()
