
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rcParams

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
plt.tight_layout()

# Number of point-lights
num_points = 15

# Initialize point-lights
points, = ax.plot([], [], 'wo', markersize=8)

# Parameters for walking motion
time_steps = 100
t = np.linspace(0, 2 * np.pi, time_steps)

# Define the motion for each point (simplified walking motion)
def get_point_positions(t_step):
    # Main body points (e.g., head, torso, hips)
    head_x = 0
    head_y = 1.0 + 0.05 * np.sin(t_step * 2)
    
    torso_x = 0
    torso_y = 0.5 + 0.03 * np.sin(t_step * 2)
    
    hip_x = 0
    hip_y = 0.0
    
    # Arm points (left and right)
    arm_swing = 0.5 * np.sin(t_step)
    left_shoulder_x = -0.2
    left_shoulder_y = 0.7 + 0.02 * np.sin(t_step * 2)
    left_elbow_x = -0.2 - 0.3 * np.sin(arm_swing)
    left_elbow_y = 0.4 + 0.1 * np.sin(arm_swing)
    left_hand_x = -0.2 - 0.6 * np.sin(arm_swing)
    left_hand_y = 0.1 + 0.1 * np.sin(arm_swing)
    
    right_shoulder_x = 0.2
    right_shoulder_y = 0.7 + 0.02 * np.sin(t_step * 2)
    right_elbow_x = 0.2 + 0.3 * np.sin(arm_swing)
    right_elbow_y = 0.4 + 0.1 * np.sin(arm_swing)
    right_hand_x = 0.2 + 0.6 * np.sin(arm_swing)
    right_hand_y = 0.1 + 0.1 * np.sin(arm_swing)
    
    # Leg points (left and right)
    leg_swing = 0.7 * np.sin(t_step + np.pi)
    left_hip_x = -0.1
    left_hip_y = 0.0
    left_knee_x = -0.1 - 0.2 * np.sin(leg_swing)
    left_knee_y = -0.5 + 0.1 * np.sin(leg_swing * 2)
    left_foot_x = -0.1 - 0.4 * np.sin(leg_swing)
    left_foot_y = -1.0 + 0.1 * np.sin(leg_swing * 2)
    
    right_hip_x = 0.1
    right_hip_y = 0.0
    right leg is opposite phase
    right_knee_x = 0.1 + 0.2 * np.sin(leg_swing)
    right_knee_y = -0.5 + 0.1 * np.sin(leg_swing * 2)
    right_foot_x = 0.1 + 0.4 * np.sin(leg_swing)
    right_foot_y = -1.0 + 0.1 * np.sin(leg_swing * 2)
    
    # Combine all points
    x = [
        head_x, torso_x, hip_x,
        left_shoulder_x, left_elbow_x, left_hand_x,
        right_shoulder_x, right_elbow_x, right_hand_x,
        left_hip_x, left_knee_x, left_foot_x,
        right_hip_x, right_knee_x, right_foot_x
    ]
    y = [
        head_y, torso_y, hip_y,
        left_shoulder_y, left_elbow_y, left_hand_y,
        right_shoulder_y, right_elbow_y, right_hand_y,
        left_hip_y, left_knee_y, left_foot_y,
        right_hip_y, right_knee_y, right_foot_y
    ]
    
    return x, y

# Animation update function
def update(frame):
    t_step = t[frame % time_steps]
    x, y = get_point_positions(t_step)
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=time_steps, interval=50, blit=True
)

plt.show()
