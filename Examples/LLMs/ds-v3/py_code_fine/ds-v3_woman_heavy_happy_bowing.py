
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Ellipse
import math

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points = [ax.plot([], [], 'o', color='white', markersize=8)[0] for _ in range(num_points)]

# Define the key points for the happy woman bowing
# The points are ordered as follows (approximate positions):
# 0: head
# 1-2: shoulders (left, right)
# 3-4: elbows (left, right)
# 5-6: hands (left, right)
# 7-8: hips (left, right)
# 9-10: knees (left, right)
# 11-12: feet (left, right)
# 13: torso midpoint
# 14: waist

# Initial positions (standing)
def initial_positions():
    pos = np.zeros((num_points, 2))
    # Head
    pos[0] = [0, 1.5]
    # Shoulders
    pos[1] = [-0.3, 1.3]  # left
    pos[2] = [0.3, 1.3]   # right
    # Elbows
    pos[3] = [-0.5, 1.1]  # left
    pos[4] = [0.5, 1.1]   # right
    # Hands
    pos[5] = [-0.6, 0.8]  # left
    pos[6] = [0.6, 0.8]   # right
    # Hips
    pos[7] = [-0.2, 0.7]  # left
    pos[8] = [0.2, 0.7]   # right
    # Knees
    pos[9] = [-0.2, 0.3]  # left
    pos[10] = [0.2, 0.3]  # right
    # Feet
    pos[11] = [-0.2, 0.0] # left
    pos[12] = [0.2, 0.0]  # right
    # Torso midpoint
    pos[13] = [0, 1.0]
    # Waist
    pos[14] = [0, 0.8]
    return pos

# Bowing motion parameters
def bowing_motion(t, total_frames=60):
    # t is the current frame (0 to total_frames-1)
    # Returns the positions of all points at frame t
    
    # Normalized time (0 to 1)
    progress = t / (total_frames - 1)
    
    # Get initial positions
    pos = initial_positions()
    
    # Bowing motion: the upper body leans forward
    # The head, shoulders, elbows, hands, torso, and waist move forward and down
    # The hips, knees, and feet remain mostly stationary
    
    # Angle of bowing (0 to 30 degrees)
    angle = 30 * np.sin(progress * np.pi)  # Smooth bow and return
    
    # Convert angle to radians
    theta = np.radians(angle)
    
    # Pivot point around the waist (point 14)
    pivot = pos[14].copy()
    
    # Points to rotate: head, shoulders, elbows, hands, torso midpoint
    rotate_indices = [0, 1, 2, 3, 4, 5, 6, 13]
    
    for i in rotate_indices:
        # Vector from pivot to point
        v = pos[i] - pivot
        # Rotation matrix
        rot = np.array([
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ])
        # Rotated vector
        v_rot = np.dot(rot, v)
        # New position
        pos[i] = pivot + v_rot
    
    # Slight movement in the arms to simulate a natural motion
    if progress <= 0.5:
        # Arms move forward during bow
        arm_progress = progress * 2
    else:
        # Arms move back during return
        arm_progress = (1 - progress) * 2
    
    # Adjust elbow and hand positions for a natural arm swing
    pos[3] = pos[1][0] - 0.2 * (1 + arm_progress), pos[1][1] - 0.2 * (1 + arm_progress)  # left elbow
    pos[4] = pos[2][0] + 0.2 * (1 + arm_progress), pos[2][1] - 0.2 * (1 + arm_progress)  # right elbow
    pos[5] = pos[3][0] - 0.1 * (1 + arm_progress), pos[3][1] - 0.3 * (1 + arm_progress)  # left hand
    pos[6] = pos[4][0] + 0.1 * (1 + arm_progress), pos[4][1] - 0.3 * (1 + arm_progress)  # right hand
    
    return pos

# Animation update function
def update(frame):
    pos = bowing_motion(frame, total_frames=60)
    for i, point in enumerate(points):
        point.set_data(pos[i, 0], pos[i, 1])
    return points

# Create the animation
ani = FuncAnimation(fig, update, frames=60, interval=50, blit=True)

plt.tight_layout()
plt.show()
