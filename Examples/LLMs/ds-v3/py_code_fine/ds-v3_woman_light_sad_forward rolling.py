
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Ellipse
import math

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.set_aspect('equal')
ax.set_facecolor('black')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points = ax.scatter([], [], color='white', s=50)

# Define the key points for a human figure (simplified)
key_points = {
    'head': 0,
    'shoulder_left': 1,
    'shoulder_right': 2,
    'elbow_left': 3,
    'elbow_right': 4,
    'hand_left': 5,
    'hand_right': 6,
    'hip_left': 7,
    'hip_right': 8,
    'knee_left': 9,
    'knee_right': 10,
    'ankle_left': 11,
    'ankle_right': 12,
    'foot_left': 13,
    'foot_right': 14
}

# Initial positions (neutral standing pose)
def initial_positions():
    pos = np.zeros((num_points, 2))
    pos[0] = [0, 1.8]    # head
    pos[1] = [-0.3, 1.6] # shoulder_left
    pos[2] = [0.3, 1.6]  # shoulder_right
    pos[3] = [-0.5, 1.4] # elbow_left
    pos[4] = [0.5, 1.4]  # elbow_right
    pos[5] = [-0.7, 1.2] # hand_left
    pos[6] = [0.7, 1.2]  # hand_right
    pos[7] = [-0.2, 1.0] # hip_left
    pos[8] = [0.2, 1.0]  # hip_right
    pos[9] = [-0.2, 0.6] # knee_left
    pos[10] = [0.2, 0.6] # knee_right
    pos[11] = [-0.2, 0.2] # ankle_left
    pos[12] = [0.2, 0.2]  # ankle_right
    pos[13] = [-0.2, 0.0] # foot_left
    pos[14] = [0.2, 0.0]  # foot_right
    return pos

# Update function for animation
def update(frame):
    t = frame * 0.1
    pos = initial_positions()
    
    # Forward rolling motion (simplified)
    roll_angle = -t * 2  # Negative for forward roll
    
    # Rotate the upper body (head, shoulders, arms)
    for i in [0, 1, 2, 3, 4, 5, 6]:
        x, y = pos[i]
        # Rotate around a point near the hips
        cx, cy = 0, 1.0
        dx = x - cx
        dy = y - cy
        new_x = cx + dx * math.cos(roll_angle) - dy * math.sin(roll_angle)
        new_y = cy + dx * math.sin(roll_angle) + dy * math.cos(roll_angle)
        pos[i] = [new_x, new_y]
    
    # Rotate the lower body (hips, legs, feet)
    for i in [7, 8, 9, 10, 11, 12, 13, 14]:
        x, y = pos[i]
        # Rotate around a point near the hips
        cx, cy = 0, 1.0
        dx = x - cx
        dy = y - cy
        new_x = cx + dx * math.cos(roll_angle) - dy * math.sin(roll_angle)
        new_y = cy + dx * math.sin(roll_angle) + dy * math.cos(roll_angle)
        pos[i] = [new_x, new_y]
    
    # Add some vertical movement to simulate rolling
    for i in range(num_points):
        pos[i][1] -= 0.05 * t
    
    # Update scatter plot data
    points.set_offsets(pos)
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.tight_layout()
plt.show()
