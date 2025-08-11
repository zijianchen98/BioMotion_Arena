
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Set up the figure and axis
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, aspect='equal')
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-1.5, 2.5)
ax.set_xticks([])
ax.set_yticks([])

# Base positions of 15 body points in 3D
base_positions = np.array([
    [0.0, 2.0, 0.3],    # Head
    [0.0, 1.7, 0.2],    # Neck
    [-0.6, 1.5, -0.1],  # Left shoulder
    [0.6, 1.5, -0.1],   # Right shoulder
    [-0.8, 1.2, -0.2],  # Left elbow
    [0.8, 1.2, -0.2],   # Right elbow
    [-1.0, 0.8, -0.3],  # Left hand
    [1.0, 0.8, -0.3],   # Right hand
    [0.0, 1.3, 0.0],    # Torso
    [-0.4, 0.9, -0.1],  # Left hip
    [0.4, 0.9, -0.1],   # Right hip
    [-0.4, 0.4, -0.1],  # Left knee
    [0.4, 0.4, -0.1],   # Right knee
    [-0.4, 0.0, 0.1],   # Left foot
    [0.4, 0.0, 0.1]     # Right foot
])

# Parameters for the animation
total_time = 5.0
step_time = total_time / 2
camera_distance = 6.0
amplitude_lift = 0.4
amplitude_arm = 0.3
amplitude_bounce = 0.2

# Initialize the points for the plot
points, = ax.plot([], [], 'wo', markersize=10)

def update(frame):
    t = frame * 0.05
    rotation_angle = 2 * math.pi * t / total_time
    gait_phase = 2 * math.pi * t / step_time
    bounce_offset = amplitude_bounce * math.sin(2 * math.pi * t / total_time - math.pi/2)
    
    current_positions = base_positions.copy()
    
    # Add vertical lift to feet
    current_positions[13, 1] += amplitude_lift * (1 + math.cos(gait_phase + math.pi)) / 2
    current_positions[14, 1] += amplitude_lift * (1 + math.cos(gait_phase)) / 2
    
    # Add arm swinging motion
    current_positions[6, 0] += amplitude_arm * math.sin(gait_phase + math.pi)
    current_positions[7, 0] += amplitude_arm * math.sin(gait_phase)
    current_positions[6, 2] += amplitude_arm * math.cos(gait_phase)
    current_positions[7, 2] += amplitude_arm * math.cos(gait_phase + math.pi)
    
    # Add body bounce
    current_positions[:, 1] += bounce_offset
    
    # Rotation matrix for turning motion
    rotation_matrix = np.array([
        [math.cos(rotation_angle), 0, -math.sin(rotation_angle)],
        [0, 1, 0],
        [math.sin(rotation_angle), 0, math.cos(rotation_angle)]
    ])
    
    rotated_positions = np.zeros_like(current_positions)
    for i in range(15):
        rotated_positions[i] = np.dot(rotation_matrix, current_positions[i])
    
    # Project 3D points to 2D using perspective
    screen_x = []
    screen_y = []
    for i in range(15):
        x, y, z = rotated_positions[i]
        factor = camera_distance / (camera_distance + z)
        screen_x.append(x * factor)
        screen_y.append(y * factor)
    
    points.set_data(screen_x, screen_y)
    return points,

ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()
