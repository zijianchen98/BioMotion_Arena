
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
import math

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-5, 5)
ax.set_ylim(-2, 8)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points = [Circle((0, 0), 0.1, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define the key points of the body (approximate positions for a human figure)
def get_body_positions(t):
    # Time parameter t is in radians (0 to 2π for one full cycle)
    # Define the motion for each point
    
    # Head (sinusoidal vertical movement)
    head_x = 0
    head_y = 3.5 + 0.3 * math.sin(t * 2)
    
    # Shoulders (slight movement)
    shoulder_left_x = -0.5 - 0.1 * math.sin(t)
    shoulder_left_y = 3.0 + 0.2 * math.sin(t * 2)
    shoulder_right_x = 0.5 + 0.1 * math.sin(t)
    shoulder_right_y = 3.0 + 0.2 * math.sin(t * 2)
    
    # Elbows (more pronounced movement)
    elbow_left_x = -0.8 - 0.2 * math.sin(t * 2)
    elbow_left_y = 2.5 + 0.4 * math.sin(t * 2 + 0.5)
    elbow_right_x = 0.8 + 0.2 * math.sin(t * 2)
    elbow_right_y = 2.5 + 0.4 * math.sin(t * 2 + 0.5)
    
    # Hands (follow elbows with more movement)
    hand_left_x = -1.0 - 0.3 * math.sin(t * 2 + 0.3)
    hand_left_y = 2.0 + 0.6 * math.sin(t * 2 + 0.7)
    hand_right_x = 1.0 + 0.3 * math.sin(t * 2 + 0.3)
    hand_right_y = 2.0 + 0.6 * math.sin(t * 2 + 0.7)
    
    # Torso (slight movement)
    torso_x = 0
    torso_y = 2.0 + 0.1 * math.sin(t * 2)
    
    # Hips (more movement for jumping)
    hip_left_x = -0.4 - 0.1 * math.sin(t)
    hip_left_y = 1.5 + 0.5 * math.sin(t * 2)
    hip_right_x = 0.4 + 0.1 * math.sin(t)
    hip_right_y = 1.5 + 0.5 * math.sin(t * 2)
    
    # Knees (pronounced movement)
    knee_left_x = -0.5 - 0.2 * math.sin(t * 2 + 0.2)
    knee_left_y = 0.8 + 0.7 * math.sin(t * 2 + 0.4)
    knee_right_x = 0.5 + 0.2 * math.sin(t * 2 + 0.2)
    knee_right_y = 0.8 + 0.7 * math.sin(t * 2 + 0.4)
    
    # Feet (most movement)
    foot_left_x = -0.6 - 0.3 * math.sin(t * 2 + 0.5)
    foot_left_y = 0.2 + 0.9 * math.sin(t * 2 + 0.8)
    foot_right_x = 0.6 + 0.3 * math.sin(t * 2 + 0.5)
    foot_right_y = 0.2 + 0.9 * math.sin(t * 2 + 0.8)
    
    # Forward movement (simulate jumping forward)
    forward_offset = 0.5 * (1 - math.cos(t))  # Moves forward over time
    
    # Apply forward movement to all points
    positions = np.array([
        [head_x + forward_offset, head_y],               # 0: head
        [shoulder_left_x + forward_offset, shoulder_left_y],  # 1: left shoulder
        [shoulder_right_x + forward_offset, shoulder_right_y], # 2: right shoulder
        [elbow_left_x + forward_offset, elbow_left_y],    # 3: left elbow
        [elbow_right_x + forward_offset, elbow_right_y],  # 4: right elbow
        [hand_left_x + forward_offset, hand_left_y],      # 5: left hand
        [hand_right_x + forward_offset, hand_right_y],    # 6: right hand
        [torso_x + forward_offset, torso_y],              # 7: torso
        [hip_left_x + forward_offset, hip_left_y],        # 8: left hip
        [hip_right_x + forward_offset, hip_right_y],      # 9: right hip
        [knee_left_x + forward_offset, knee_left_y],      # 10: left knee
        [knee_right_x + forward_offset, knee_right_y],    # 11: right knee
        [foot_left_x + forward_offset, foot_left_y],      # 12: left foot
        [foot_right_x + forward_offset, foot_right_y],    # 13: right foot
        [torso_x + forward_offset, torso_y + 0.3]         # 14: mid-torso (extra point)
    ])
    
    return positions

# Update function for animation
def update(frame):
    t = frame * 0.1  # Controls the speed of the animation
    positions = get_body_positions(t)
    for i, point in enumerate(points):
        point.center = positions[i]
    return points

# Create the animation
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.title('Point-Light Jumping Animation', color='white')
plt.show()
