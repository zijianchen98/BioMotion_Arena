
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rcParams

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_facecolor('black')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points, = ax.plot([], [], 'wo', markersize=8)

# Define keyframes for the lying down motion
def get_keyframe(t):
    # Time is normalized between 0 and 1 for the animation cycle
    # The motion will simulate a heavy woman lying down with slight breathing
    
    # Key joint positions (simplified for lying down pose)
    # Head, shoulders, elbows, hands, hips, knees, feet
    # The y-coordinates are adjusted to simulate lying down (lower y-values)
    
    # Breathing effect: slight vertical movement for the chest and shoulders
    breathing = 0.05 * np.sin(2 * np.pi * t)
    
    # Main body (lying horizontally)
    head_x = 0.0
    head_y = 0.8 + 0.01 * np.sin(2 * np.pi * t)
    
    shoulder_left_x = -0.3
    shoulder_left_y = 0.7 + breathing
    shoulder_right_x = 0.3
    shoulder_right_y = 0.7 + breathing
    
    elbow_left_x = -0.4
    elbow_left_y = 0.6
    elbow_right_x = 0.4
    elbow_right_y = 0.6
    
    hand_left_x = -0.5
    hand_left_y = 0.5
    hand_right_x = 0.5
    hand_right_y = 0.5
    
    hip_left_x = -0.2
    hip_left_y = 0.3
    hip_right_x = 0.2
    hip_right_y = 0.3
    
    knee_left_x = -0.25
    knee_left_y = 0.1
    knee_right_x = 0.25
    knee_right_y = 0.1
    
    foot_left_x = -0.3
    foot_left_y = -0.1
    foot_right_x = 0.3
    foot_right_y = -0.1
    
    # Additional points for the torso to make 15 points
    torso1_x = 0.0
    torso1_y = 0.6 + breathing
    torso2_x = 0.0
    torso2_y = 0.5
    torso3_x = 0.0
    torso3_y = 0.4
    
    # Combine all points
    x = np.array([
        head_x, 
        shoulder_left_x, shoulder_right_x,
        elbow_left_x, elbow_right_x,
        hand_left_x, hand_right_x,
        hip_left_x, hip_right_x,
        knee_left_x, knee_right_x,
        foot_left_x, foot_right_x,
        torso1_x, torso2_x, torso3_x
    ])
    
    y = np.array([
        head_y,
        shoulder_left_y, shoulder_right_y,
        elbow_left_y, elbow_right_y,
        hand_left_y, hand_right_y,
        hip_left_y, hip_right_y,
        knee_left_y, knee_right_y,
        foot_left_y, foot_right_y,
        torso1_y, torso2_y, torso3_y
    ])
    
    return x, y

# Animation update function
def update(frame):
    t = frame / 30  # 30 frames per cycle
    x, y = get_keyframe(t)
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=30, interval=50, blit=True
)

plt.tight_layout()
plt.show()
