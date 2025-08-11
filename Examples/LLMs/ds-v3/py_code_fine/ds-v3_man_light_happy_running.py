
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches

# Parameters
num_points = 15
num_frames = 60
fps = 30

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Initialize point lights
points = ax.scatter([], [], color='white', s=50)

# Biomechanical parameters for running motion
def get_running_positions(t):
    # Time-dependent parameters
    phase = 2 * np.pi * t / num_frames
    
    # Body parts: head, shoulders, elbows, hands, hips, knees, feet
    # Using sinusoidal movements for simplicity (more complex models can be used)
    head_x = 0.0
    head_y = 1.5 + 0.1 * np.sin(phase * 2)
    
    # Shoulders
    shoulder_y = 1.2 + 0.05 * np.sin(phase * 2)
    left_shoulder_x = -0.2 - 0.1 * np.sin(phase)
    right_shoulder_x = 0.2 + 0.1 * np.sin(phase)
    
    # Elbows
    left_elbow_x = left_shoulder_x - 0.2 - 0.1 * np.sin(phase + np.pi/2)
    left_elbow_y = shoulder_y - 0.2 + 0.1 * np.sin(phase * 2)
    right_elbow_x = right_shoulder_x + 0.2 + 0.1 * np.sin(phase + np.pi/2)
    right_elbow_y = shoulder_y - 0.2 + 0.1 * np.sin(phase * 2)
    
    # Hands
    left_hand_x = left_elbow_x - 0.2 - 0.1 * np.sin(phase)
    left_hand_y = left_elbow_y - 0.2 + 0.1 * np.sin(phase * 2 + np.pi/4)
    right_hand_x = right_elbow_x + 0.2 + 0.1 * np.sin(phase)
    right_hand_y = right_elbow_y - 0.2 + 0.1 * np.sin(phase * 2 + np.pi/4)
    
    # Hips
    hip_y = 0.8 + 0.05 * np.sin(phase * 2)
    left_hip_x = -0.15 - 0.1 * np.sin(phase + np.pi)
    right_hip_x = 0.15 + 0.1 * np.sin(phase + np.pi)
    
    # Knees
    left_knee_x = left_hip_x - 0.1 - 0.2 * np.sin(phase + np.pi/2)
    left_knee_y = hip_y - 0.3 + 0.2 * np.sin(phase * 2)
    right_knee_x = right_hip_x + 0.1 + 0.2 * np.sin(phase + np.pi/2)
    right_knee_y = hip_y - 0.3 + 0.2 * np.sin(phase * 2)
    
    # Feet
    left_foot_x = left_knee_x - 0.1 - 0.3 * np.sin(phase)
    left_foot_y = left_knee_y - 0.3 + 0.3 * np.sin(phase * 2 + np.pi/2)
    right_foot_x = right_knee_x + 0.1 + 0.3 * np.sin(phase)
    right_foot_y = right_knee_y - 0.3 + 0.3 * np.sin(phase * 2 + np.pi/2)
    
    # Combine all points
    x = np.array([
        head_x,
        left_shoulder_x, right_shoulder_x,
        left_elbow_x, right_elbow_x,
        left_hand_x, right_hand_x,
        left_hip_x, right_hip_x,
        left_knee_x, right_knee_x,
        left_foot_x, right_foot_x,
        (left_shoulder_x + left_hip_x)/2,  # Additional point for torso
        (right_shoulder_x + right_hip_x)/2
    ])
    
    y = np.array([
        head_y,
        shoulder_y, shoulder_y,
        left_elbow_y, right_elbow_y,
        left_hand_y, right_hand_y,
        hip_y, hip_y,
        left_knee_y, right_knee_y,
        left_foot_y, right_foot_y,
        (shoulder_y + hip_y)/2,
        (shoulder_y + hip_y)/2
    ])
    
    return x, y

# Animation update function
def update(frame):
    x, y = get_running_positions(frame)
    points.set_offsets(np.column_stack([x, y]))
    return points,

# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, interval=1000/fps, blit=True
)

plt.tight_layout()
plt.show()
