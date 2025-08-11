
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points = [ax.plot([], [], 'o', color='white', markersize=8)[0] for _ in range(num_points)]

# Parameters for the waving motion
time_steps = 100
amplitude = 0.5
frequency = 0.1
arm_length = 1.0
torso_height = 1.5

def update(frame):
    t = frame * 2 * np.pi / time_steps
    
    # Torso and head (stationary)
    torso_x = 0
    torso_y = 0
    head_x = 0
    head_y = torso_height
    
    # Left arm (stationary, hanging down)
    left_shoulder_x = -0.5
    left_shoulder_y = torso_height * 0.8
    left_elbow_x = -0.5
    left_elbow_y = torso_height * 0.4
    left_hand_x = -0.5
    left_hand_y = 0
    
    # Right arm (waving)
    right_shoulder_x = 0.5
    right_shoulder_y = torso_height * 0.8
    right_elbow_x = 0.5 + amplitude * np.sin(t) * 0.3
    right_elbow_y = torso_height * 0.6 + amplitude * np.sin(t) * 0.2
    right_hand_x = 0.5 + amplitude * np.sin(t + 0.5) * 0.7
    right_hand_y = torso_height * 0.3 + amplitude * np.sin(t + 0.5) * 0.5
    
    # Legs (stationary)
    left_hip_x = -0.3
    left_hip_y = 0
    left_knee_x = -0.3
    left_knee_y = -0.5
    left_foot_x = -0.3
    left_foot_y = -1.0
    
    right_hip_x = 0.3
    right_hip_y = 0
    right_knee_x = 0.3
    right_knee_y = -0.5
    right_foot_x = 0.3
    right_foot_y = -1.0
    
    # Combine all points
    point_positions = [
        (torso_x, torso_y),               # 0: torso
        (head_x, head_y),                 # 1: head
        (left_shoulder_x, left_shoulder_y),  # 2: left shoulder
        (left_elbow_x, left_elbow_y),     # 3: left elbow
        (left_hand_x, left_hand_y),       # 4: left hand
        (right_shoulder_x, right_shoulder_y),  # 5: right shoulder
        (right_elbow_x, right_elbow_y),   # 6: right elbow
        (right_hand_x, right_hand_y),     # 7: right hand
        (left_hip_x, left_hip_y),         # 8: left hip
        (left_knee_x, left_knee_y),       # 9: left knee
        (left_foot_x, left_foot_y),       # 10: left foot
        (right_hip_x, right_hip_y),       # 11: right hip
        (right_knee_x, right_knee_y),     # 12: right knee
        (right_foot_x, right_foot_y),     # 13: right foot
        (head_x + 0.1 * np.sin(t), head_y + 0.1)  # 14: extra point for head/face
    ]
    
    # Update point positions
    for i, point in enumerate(points):
        x, y = point_positions[i]
        point.set_data([x], [y])
    
    return points

# Create the animation
ani = FuncAnimation(fig, update, frames=time_steps, interval=50, blit=True)

plt.title('Happy Woman Waving Hand (Point-Light Display)', color='white')
plt.tight_layout()
plt.show()
