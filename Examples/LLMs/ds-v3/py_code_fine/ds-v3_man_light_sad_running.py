
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
ax.axis('off')

# Initialize point lights
points = ax.scatter([], [], color='white', s=50)

# Define key points for a running motion (simplified)
def get_key_points(t):
    t is in [0, 1], representing the running cycle
    # Head (0)
    head_x = 0
    head_y = 1.5 + 0.1 * np.sin(2 * np.pi * t)
    
    # Shoulders (1, 2)
    shoulder_width = 0.5
    shoulder_y = 1.2 + 0.05 * np.sin(2 * np.pi * t)
    left_shoulder_x = -shoulder_width / 2
    right_shoulder_x = shoulder_width / 2
    
    # Elbows (3, 4)
    arm_swing = 0.4 * np.sin(2 * np.pi * t)
    left_elbow_x = -0.4 + 0.2 * np.sin(2 * np.pi * t)
    left_elbow_y = 1.0 + 0.1 * np.sin(2 * np.pi * t + np.pi/2)
    right_elbow_x = 0.4 - 0.2 * np.sin(2 * np.pi * t)
    right_elbow_y = 1.0 + 0.1 * np.sin(2 * np.pi * t + np.pi/2)
    
    # Hands (5, 6)
    left_hand_x = -0.6 + 0.3 * np.sin(2 * np.pi * t)
    left_hand_y = 0.7 + 0.1 * np.sin(2 * np.pi * t + np.pi/2)
    right_hand_x = 0.6 - 0.3 * np.sin(2 * np.pi * t)
    right_hand_y = 0.7 + 0.1 * np.sin(2 * np.pi * t + np.pi/2)
    
    # Hips (7, 8)
    hip_width = 0.4
    hip_y = 0.8 + 0.05 * np.sin(2 * np.pi * t + np.pi)
    left_hip_x = -hip_width / 2
    right_hip_x = hip_width / 2
    
    # Knees (9, 10)
    leg_swing = 0.6 * np.sin(2 * np.pi * t + np.pi)
    left_knee_x = -0.2 + 0.3 * np.sin(2 * np.pi * t + np.pi)
    left_knee_y = 0.4 + 0.2 * np.sin(2 * np.pi * t + np.pi)
    right_knee_x = 0.2 - 0.3 * np.sin(2 * np.pi * t + np.pi)
    right_knee_y = 0.4 + 0.2 * np.sin(2 * np.pi * t + np.pi)
    
    # Feet (11, 12)
    left_foot_x = -0.3 + 0.4 * np.sin(2 * np.pi * t + np.pi)
    left_foot_y = 0.1 + 0.1 * np.sin(2 * np.pi * t + np.pi)
    right_foot_x = 0.3 - 0.4 * np.sin(2 * np.pi * t + np.pi)
    right_foot_y = 0.1 + 0.1 * np.sin(2 * np.pi * t + np.pi)
    
    # Additional points for smoother motion (13, 14)
    mid_chest_x = 0
    mid_chest_y = 1.0 + 0.05 * np.sin(2 * np.pi * t)
    mid_pelvis_x = 0
    mid_pelvis_y = 0.7 + 0.05 * np.sin(2 * np.pi * t + np.pi)
    
    # Combine all points
    x = np.array([
        head_x, left_shoulder_x, right_shoulder_x, left_elbow_x, right_elbow_x,
        left_hand_x, right_hand_x, left_hip_x, right_hip_x, left_knee_x,
        right_knee_x, left_foot_x, right_foot_x, mid_chest_x, mid_pelvis_x
    ])
    y = np.array([
        head_y, shoulder_y, shoulder_y, left_elbow_y, right_elbow_y,
        left_hand_y, right_hand_y, hip_y, hip_y, left_knee_y,
        right_knee_y, left_foot_y, right_foot_y, mid_chest_y, mid_pelvis_y
    ])
    
    return x, y

# Animation update function
def update(frame):
    t = frame / num_frames
    x, y = get_key_points(t)
    points.set_offsets(np.column_stack((x, y)))
    return points,

# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, interval=1000/fps, blit=True
)

plt.tight_layout()
plt.show()
