
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import patches

# Parameters
num_points = 15
num_frames = 60  # Number of frames in the animation
fps = 30  # Frames per second

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize point lights
points = ax.scatter([], [], color='white', s=50)

# Define the walking motion trajectory for 15 points (simplified model)
def get_walking_positions(t):
    # Head
    head_x = 0.1 * np.sin(2 * np.pi * t)
    head_y = 1.8 + 0.05 * np.sin(4 * np.pi * t)
    
    # Shoulders
    shoulder_left_x = -0.2 + 0.1 * np.sin(2 * np.pi * t + np.pi/4)
    shoulder_left_y = 1.6 + 0.03 * np.sin(4 * np.pi * t)
    shoulder_right_x = 0.2 + 0.1 * np.sin(2 * np.pi * t + np.pi/4)
    shoulder_right_y = 1.6 + 0.03 * np.sin(4 * np.pi * t)
    
    # Elbows
    elbow_left_x = -0.3 + 0.15 * np.sin(2 * np.pi * t + np.pi/2)
    elbow_left_y = 1.4 + 0.05 * np.sin(4 * np.pi * t + np.pi/2)
    elbow_right_x = 0.3 + 0.15 * np.sin(2 * np.pi * t + np.pi/2)
    elbow_right_y = 1.4 + 0.05 * np.sin(4 * np.pi * t + np.pi/2)
    
    # Hands
    hand_left_x = -0.4 + 0.2 * np.sin(2 * np.pi * t + 3*np.pi/4)
    hand_left_y = 1.2 + 0.1 * np.sin(4 * np.pi * t + np.pi/2)
    hand_right_x = 0.4 + 0.2 * np.sin(2 * np.pi * t + 3*np.pi/4)
    hand_right_y = 1.2 + 0.1 * np.sin(4 * np.pi * t + np.pi/2)
    
    # Hips
    hip_left_x = -0.15 + 0.1 * np.sin(2 * np.pi * t)
    hip_left_y = 1.0 + 0.02 * np.sin(4 * np.pi * t + np.pi)
    hip_right_x = 0.15 + 0.1 * np.sin(2 * np.pi * t)
    hip_right_y = 1.0 + 0.02 * np.sin(4 * np.pi * t + np.pi)
    
    # Knees
    knee_left_x = -0.2 + 0.15 * np.sin(2 * np.pi * t + np.pi)
    knee_left_y = 0.6 + 0.1 * np.sin(4 * np.pi * t + np.pi)
    knee_right_x = 0.2 + 0.15 * np.sin(2 * np.pi * t + np.pi)
    knee_right_y = 0.6 + 0.1 * np.sin(4 * np.pi * t + np.pi)
    
    # Feet
    foot_left_x = -0.25 + 0.2 * np.sin(2 * np.pi * t + 5*np.pi/4)
    foot_left_y = 0.2 + 0.15 * np.sin(4 * np.pi * t + np.pi)
    foot_right_x = 0.25 + 0.2 * np.sin(2 * np.pi * t + 5*np.pi/4)
    foot_right_y = 0.2 + 0.15 * np.sin(4 * np.pi * t + np.pi)
    
    # Torso (midpoint between shoulders and hips)
    torso_x = 0.0
    torso_y = 1.3 + 0.02 * np.sin(4 * np.pi * t)
    
    # Assemble all points
    x = np.array([
        head_x, 
        shoulder_left_x, shoulder_right_x,
        elbow_left_x, elbow_right_x,
        hand_left_x, hand_right_x,
        hip_left_x, hip_right_x,
        knee_left_x, knee_right_x,
        foot_left_x, foot_right_x,
        torso_x
    ])
    
    y = np.array([
        head_y,
        shoulder_left_y, shoulder_right_y,
        elbow_left_y, elbow_right_y,
        hand_left_y, hand_right_y,
        hip_left_y, hip_right_y,
        knee_left_y, knee_right_y,
        foot_left_y, foot_right_y,
        torso_y
    ])
    
    return x, y

# Animation update function
def update(frame):
    t = frame / num_frames
    x, y = get_walking_positions(t)
    points.set_offsets(np.column_stack((x, y)))
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=1000/fps, blit=True)

plt.tight_layout()
plt.show()
