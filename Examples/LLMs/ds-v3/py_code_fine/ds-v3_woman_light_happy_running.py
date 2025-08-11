
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches

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
points = ax.scatter([], [], color='white', s=50)

# Define keyframes for the running motion (simplified)
def get_keyframe(t):
    # Normalized time (0 to 1)
    phase = (t % num_frames) / num_frames
    
    # Body parts: head, shoulders, elbows, hands, hips, knees, feet
    # Using sinusoidal functions to simulate running motion
    head_x = 0
    head_y = 1.5 + 0.1 * np.sin(2 * np.pi * phase)
    
    # Shoulders
    shoulder_y = 1.2 + 0.05 * np.sin(2 * np.pi * phase)
    left_shoulder_x = -0.3 - 0.1 * np.sin(2 * np.pi * phase)
    right_shoulder_x = 0.3 + 0.1 * np.sin(2 * np.pi * phase)
    
    # Elbows
    left_elbow_x = left_shoulder_x - 0.2 - 0.1 * np.sin(2 * np.pi * (phase + 0.25))
    left_elbow_y = shoulder_y - 0.2 + 0.1 * np.sin(2 * np.pi * (phase + 0.25))
    right_elbow_x = right_shoulder_x + 0.2 + 0.1 * np.sin(2 * np.pi * (phase + 0.25))
    right_elbow_y = shoulder_y - 0.2 + 0.1 * np.sin(2 * np.pi * (phase + 0.25))
    
    # Hands
    left_hand_x = left_elbow_x - 0.2 - 0.1 * np.sin(2 * np.pi * (phase + 0.5))
    left_hand_y = left_elbow_y - 0.2 + 0.1 * np.sin(2 * np.pi * (phase + 0.5))
    right_hand_x = right_elbow_x + 0.2 + 0.1 * np.sin(2 * np.pi * (phase + 0.5))
    right_hand_y = right_elbow_y - 0.2 + 0.1 * np.sin(2 * np.pi * (phase + 0.5))
    
    # Hips
    hip_y = 0.8 + 0.05 * np.sin(2 * np.pi * phase)
    left_hip_x = -0.2 - 0.1 * np.sin(2 * np.pi * phase)
    right_hip_x = 0.2 + 0.1 * np.sin(2 * np.pi * phase)
    
    # Knees
    left_knee_x = left_hip_x - 0.1 - 0.2 * np.sin(2 * np.pi * (phase + 0.25))
    left_knee_y = hip_y - 0.3 + 0.2 * np.sin(2 * np.pi * (phase + 0.25))
    right_knee_x = right_hip_x + 0.1 + 0.2 * np.sin(2 * np.pi * (phase + 0.25))
    right_knee_y = hip_y - 0.3 + 0.2 * np.sin(2 * np.pi * (phase + 0.25))
    
    # Feet
    left_foot_x = left_knee_x - 0.1 - 0.2 * np.sin(2 * np.pi * (phase + 0.5))
    left_foot_y = left_knee_y - 0.3 + 0.2 * np.sin(2 * np.pi * (phase + 0.5))
    right_foot_x = right_knee_x + 0.1 + 0.2 * np.sin(2 * np.pi * (phase + 0.5))
    right_foot_y = right_knee_y - 0.3 + 0.2 * np.sin(2 * np.pi * (phase + 0.5))
    
    # Combine all points
    x = np.array([
        head_x,
        left_shoulder_x, right_shoulder_x,
        left_elbow_x, right_elbow_x,
        left_hand_x, right_hand_x,
        left_hip_x, right_hip_x,
        left_knee_x, right_knee_x,
        left_foot_x, right_foot_x,
        left_foot_x - 0.1, right_foot_x + 0.1  # Extra points for feet
    ])
    
    y = np.array([
        head_y,
        shoulder_y, shoulder_y,
        left_elbow_y, right_elbow_y,
        left_hand_y, right_hand_y,
        hip_y, hip_y,
        left_knee_y, right_knee_y,
        left_foot_y, right_foot_y,
        left_foot_y - 0.1, right_foot_y - 0.1  # Extra points for feet
    ])
    
    return x, y

# Animation update function
def update(frame):
    x, y = get_keyframe(frame)
    points.set_offsets(np.column_stack([x, y]))
    return points,

# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, interval=1000/fps, blit=True
)

plt.title('Biological Motion: Happy Woman Running', color='white')
plt.tight_layout()
plt.show()
