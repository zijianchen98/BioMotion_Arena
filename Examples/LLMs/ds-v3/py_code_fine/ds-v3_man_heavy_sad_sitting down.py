
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

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
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define keyframes for the sitting down motion
def get_position(t):
    # Time parameter t ranges from 0 to 1
    # Define positions for each point at time t
    
    # Head (1 point)
    head_x = 0
    head_y = 1.5 - 0.8 * t
    
    # Shoulders (2 points)
    shoulder_y = 1.3 - 0.7 * t
    left_shoulder_x = -0.3
    right_shoulder_x = 0.3
    
    # Elbows (2 points)
    elbow_y = 1.1 - 0.6 * t
    left_elbow_x = -0.4 + 0.1 * t
    right_elbow_x = 0.4 - 0.1 * t
    
    # Hands (2 points)
    hand_y = 0.9 - 0.8 * t
    left_hand_x = -0.5 + 0.1 * t
    right_hand_x = 0.5 - 0.1 * t
    
    # Torso (1 point)
    torso_x = 0
    torso_y = 0.9 - 0.6 * t
    
    # Hips (2 points)
    hip_y = 0.6 - 0.4 * t
    left_hip_x = -0.2
    right_hip_x = 0.2
    
    # Knees (2 points)
    knee_y = 0.3 - 0.3 * t
    left_knee_x = -0.25
    right_knee_x = 0.25
    
    # Feet (2 points)
    foot_y = 0.0
    left_foot_x = -0.3
    right_foot_x = 0.3
    
    # Additional point for the back (to show bending)
    back_x = 0
    back_y = 1.1 - 0.7 * t
    
    positions = [
        (head_x, head_y),  # head
        (left_shoulder_x, shoulder_y),  # left shoulder
        (right_shoulder_x, shoulder_y),  # right shoulder
        (left_elbow_x, elbow_y),  # left elbow
        (right_elbow_x, elbow_y),  # right elbow
        (left_hand_x, hand_y),  # left hand
        (right_hand_x, hand_y),  # right hand
        (torso_x, torso_y),  # torso
        (left_hip_x, hip_y),  # left hip
        (right_hip_x, hip_y),  # right hip
        (left_knee_x, knee_y),  # left knee
        (right_knee_x, knee_y),  # right knee
        (left_foot_x, foot_y),  # left foot
        (right_foot_x, foot_y),  # right foot
        (back_x, back_y)  # back point
    ]
    
    return positions

# Update function for animation
def update(frame):
    t = frame / 100  # Normalize frame to [0, 1]
    positions = get_position(t)
    for i, point in enumerate(points):
        point.center = positions[i]
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.tight_layout()
plt.show()
