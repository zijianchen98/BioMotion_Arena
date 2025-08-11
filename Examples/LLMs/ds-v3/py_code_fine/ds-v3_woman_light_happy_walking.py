
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Parameters
num_points = 15
num_frames = 60  # Number of frames in the animation
fps = 30  # Frames per second

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define walking motion parameters
def get_walking_positions(frame):
    t = frame / num_frames * 2 * np.pi  # Time parameter
    
    # Body motion parameters
    body_x = 0.5 * np.sin(t * 2)  # Sway side to side
    body_y = 0.1 * np.sin(t)  # Slight up and down
    
    # Head
    head_x = body_x
    head_y = body_y + 1.2
    
    # Shoulders
    shoulder_y = body_y + 0.8
    left_shoulder_x = body_x - 0.3 - 0.1 * np.sin(t * 2)
    right_shoulder_x = body_x + 0.3 + 0.1 * np.sin(t * 2)
    
    # Elbows
    left_elbow_x = left_shoulder_x - 0.2 * np.sin(t * 2 + np.pi/4)
    left_elbow_y = shoulder_y - 0.2 * np.cos(t * 2 + np.pi/4)
    right_elbow_x = right_shoulder_x + 0.2 * np.sin(t * 2 + np.pi/4)
    right_elbow_y = shoulder_y - 0.2 * np.cos(t * 2 + np.pi/4)
    
    # Hands
    left_hand_x = left_elbow_x - 0.2 * np.sin(t * 2 + np.pi/2)
    left_hand_y = left_elbow_y - 0.2 * np.cos(t * 2 + np.pi/2)
    right_hand_x = right_elbow_x + 0.2 * np.sin(t * 2 + np.pi/2)
    right_hand_y = right_elbow_y - 0.2 * np.cos(t * 2 + np.pi/2)
    
    # Hips
    hip_y = body_y + 0.3
    left_hip_x = body_x - 0.2 - 0.05 * np.sin(t * 2)
    right_hip_x = body_x + 0.2 + 0.05 * np.sin(t * 2)
    
    # Knees
    left_knee_x = left_hip_x - 0.1 * np.sin(t * 2 + np.pi)
    left_knee_y = hip_y - 0.3 * np.cos(t * 2 + np.pi)
    right_knee_x = right_hip_x + 0.1 * np.sin(t * 2 + np.pi)
    right_knee_y = hip_y - 0.3 * np.cos(t * 2 + np.pi)
    
    # Feet
    left_foot_x = left_knee_x - 0.2 * np.sin(t * 2 + 3*np.pi/4)
    left_foot_y = left_knee_y - 0.2 * np.cos(t * 2 + 3*np.pi/4)
    right_foot_x = right_knee_x + 0.2 * np.sin(t * 2 + 3*np.pi/4)
    right_foot_y = right_knee_y - 0.2 * np.cos(t * 2 + 3*np.pi/4)
    
    # Return positions in order: head, shoulders, elbows, hands, hips, knees, feet
    return np.array([
        [head_x, head_y],  # Head
        [left_shoulder_x, shoulder_y],  # Left shoulder
        [right_shoulder_x, shoulder_y],  # Right shoulder
        [left_elbow_x, left_elbow_y],  # Left elbow
        [right_elbow_x, right_elbow_y],  # Right elbow
        [left_hand_x, left_hand_y],  # Left hand
        [right_hand_x, right_hand_y],  # Right hand
        [left_hip_x, hip_y],  # Left hip
        [right_hip_x, hip_y],  # Right hip
        [left_knee_x, left_knee_y],  # Left knee
        [right_knee_x, right_knee_y],  # Right knee
        [left_foot_x, left_foot_y],  # Left foot
        [right_foot_x, right_foot_y],  # Right foot
        [body_x, body_y],  # Center of body (optional)
        [body_x, body_y + 0.5]  # Mid torso (optional)
    ])

# Update function
def update(frame):
    positions = get_walking_positions(frame)
    for i, point in enumerate(points):
        point.center = positions[i]
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=1000/fps, blit=True)

plt.tight_layout()
plt.show()
