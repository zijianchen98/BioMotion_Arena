
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.collections import PathCollection

# Define the number of frames and points
num_frames = 30
num_points = 15

# Define the key points for a running motion (simplified)
# Points are ordered as: head, shoulders (2), elbows (2), hands (2), hips (2), knees (2), feet (2), torso (1)
# The coordinates are relative to the torso position and normalized

# Define the motion cycle for running
def get_point_positions(frame):
    t = frame / num_frames * 2 * np.pi  # Cycle over 2π
    
    # Torso position (central reference)
    torso_x = 0
    torso_y = 0
    
    # Head bobs slightly
    head_x = torso_x
    head_y = torso_y + 0.8 + 0.05 * np.sin(t * 2)
    
    # Shoulders move opposite to each other
    shoulder_l_x = torso_x - 0.3 * np.sin(t)
    shoulder_l_y = torso_y + 0.5
    shoulder_r_x = torso_x + 0.3 * np.sin(t)
    shoulder_r_y = torso_y + 0.5
    
    # Elbows move with the shoulders
    elbow_l_x = shoulder_l_x - 0.2 * np.sin(t + np.pi/2)
    elbow_l_y = shoulder_l_y - 0.2 * np.cos(t + np.pi/2)
    elbow_r_x = shoulder_r_x + 0.2 * np.sin(t + np.pi/2)
    elbow_r_y = shoulder_r_y - 0.2 * np.cos(t + np.pi/2)
    
    # Hands follow the elbows
    hand_l_x = elbow_l_x - 0.2 * np.sin(t)
    hand_l_y = elbow_l_y - 0.2 * np.cos(t)
    hand_r_x = elbow_r_x + 0.2 * np.sin(t)
    hand_r_y = elbow_r_y - 0.2 * np.cos(t)
    
    # Hips move opposite to shoulders
    hip_l_x = torso_x - 0.2 * np.sin(t + np.pi)
    hip_l_y = torso_y - 0.2
    hip_r_x = torso_x + 0.2 * np.sin(t + np.pi)
    hip_r_y = torso_y - 0.2
    
    # Knees move in running motion
    knee_l_x = hip_l_x - 0.2 * np.sin(t * 2 + np.pi/2)
    knee_l_y = hip_l_y - 0.4 + 0.1 * np.sin(t * 2)
    knee_r_x = hip_r_x + 0.2 * np.sin(t * 2 + np.pi/2)
    knee_r_y = hip_r_y - 0.4 + 0.1 * np.sin(t * 2)
    
    # Feet follow the knees
    foot_l_x = knee_l_x - 0.2 * np.sin(t * 2)
    foot_l_y = knee_l_y - 0.3 + 0.1 * np.sin(t * 2 + np.pi/2)
    foot_r_x = knee_r_x + 0.2 * np.sin(t * 2)
    foot_r_y = knee_r_y - 0.3 + 0.1 * np.sin(t * 2 + np.pi/2)
    
    # Combine all points
    points_x = [
        head_x,
        shoulder_l_x, shoulder_r_x,
        elbow_l_x, elbow_r_x,
        hand_l_x, hand_r_x,
        hip_l_x, hip_r_x,
        knee_l_x, knee_r_x,
        foot_l_x, foot_r_x,
        torso_x
    ]
    points_y = [
        head_y,
        shoulder_l_y, shoulder_r_y,
        elbow_l_y, elbow_r_y,
        hand_l_y, hand_r_y,
        hip_l_y, hip_r_y,
        knee_l_y, knee_r_y,
        foot_l_y, foot_r_y,
        torso_y
    ]
    
    return np.array([points_x, points_y]).T

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the point collection
scatter = ax.scatter([], [], color='white', s=100)

# Animation update function
def update(frame):
    pos = get_point_positions(frame)
    scatter.set_offsets(pos)
    return scatter,

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

plt.tight_layout()
plt.show()
