
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches

# Parameters
num_points = 15
num_frames = 60  # Number of frames in the animation
fps = 30  # Frames per second

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Points representing the walker (head, shoulders, elbows, hands, hips, knees, feet)
points = ax.plot([], [], 'wo', markersize=8)[0]

# Define the initial positions (relative to the body center)
def get_body_positions(t):
    # Body center moves forward (x) and slightly up and down (y)
    x_center = 0.5 * np.sin(2 * np.pi * t / num_frames)  # Sway side to side
    y_center = 0.1 * np.sin(4 * np.pi * t / num_frames)  # Up and down movement
    
    # Arm angles (left and right)
    left_arm_angle = np.pi/3 * np.sin(2 * np.pi * t / num_frames + np.pi/2)
    right_arm_angle = np.pi/3 * np.sin(2 * np.pi * t / num_frames - np.pi/2)
    
    # Leg angles (left and right)
    left_leg_angle = np.pi/4 * np.sin(2 * np.pi * t / num_frames)
    right_leg_angle = np.pi/4 * np.sin(2 * np.pi * t / num_frames + np.pi)
    
    # Head
    head_x = x_center
    head_y = y_center + 0.8
    
    # Shoulders
    left_shoulder_x = x_center - 0.2
    left_shoulder_y = y_center + 0.6
    right_shoulder_x = x_center + 0.2
    right_shoulder_y = y_center + 0.6
    
    # Elbows
    left_elbow_x = left_shoulder_x - 0.3 * np.cos(left_arm_angle)
    left_elbow_y = left_shoulder_y - 0.3 * np.sin(left_arm_angle)
    right_elbow_x = right_shoulder_x + 0.3 * np.cos(right_arm_angle)
    right_elbow_y = right_shoulder_y - 0.3 * np.sin(right_arm_angle)
    
    # Hands
    left_hand_x = left_elbow_x - 0.25 * np.cos(left_arm_angle + 0.2)
    left_hand_y = left_elbow_y - 0.25 * np.sin(left_arm_angle + 0.2)
    right_hand_x = right_elbow_x + 0.25 * np.cos(right_arm_angle - 0.2)
    right_hand_y = right_elbow_y - 0.25 * np.sin(right_arm_angle - 0.2)
    
    # Hips
    left_hip_x = x_center - 0.15
    left_hip_y = y_center
    right_hip_x = x_center + 0.15
    right_hip_y = y_center
    
    # Knees
    left_knee_x = left_hip_x - 0.2 * np.sin(left_leg_angle)
    left_knee_y = left_hip_y - 0.4 * np.cos(left_leg_angle)
    right_knee_x = right_hip_x + 0.2 * np.sin(right_leg_angle)
    right_knee_y = right_hip_y - 0.4 * np.cos(right_leg_angle)
    
    # Feet
    left_foot_x = left_knee_x - 0.2 * np.sin(left_leg_angle + 0.2)
    left_foot_y = left_knee_y - 0.3 * np.cos(left_leg_angle + 0.2)
    right_foot_x = right_knee_x + 0.2 * np.sin(right_leg_angle - 0.2)
    right_foot_y = right_knee_y - 0.3 * np.cos(right_leg_angle - 0.2)
    
    # Torso points (for more natural movement)
    torso1_x = x_center
    torso1_y = y_center + 0.4
    torso2_x = x_center
    torso2_y = y_center + 0.2
    
    # Combine all points
    x = np.array([
        head_x,
        left_shoulder_x, right_shoulder_x,
        left_elbow_x, right_elbow_x,
        left_hand_x, right_hand_x,
        torso1_x, torso2_x,
        left_hip_x, right_hip_x,
        left_knee_x, right_knee_x,
        left_foot_x, right_foot_x
    ])
    
    y = np.array([
        head_y,
        left_shoulder_y, right_shoulder_y,
        left_elbow_y, right_elbow_y,
        left_hand_y, right_hand_y,
        torso1_y, torso2_y,
        left_hip_y, right_hip_y,
        left_knee_y, right_knee_y,
        left_foot_y, right_foot_y
    ])
    
    return x, y

# Animation update function
def update(frame):
    t = frame % num_frames
    x, y = get_body_positions(t)
    points.set_data(x, y)
    return points,

# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, interval=1000/fps, blit=True
)

plt.tight_layout()
plt.show()
