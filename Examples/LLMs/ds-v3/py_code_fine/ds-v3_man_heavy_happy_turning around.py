
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches

# Parameters
num_points = 15
fps = 30
duration = 5  # seconds
total_frames = fps * duration

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Initialize point lights
points = ax.scatter([], [], color='white', s=50)

# Define the motion of a turning person with heavy weight
def update(frame):
    t = frame / fps
    angle = 2 * np.pi * t / duration  # Full rotation over duration
    
    # Body parts positions (simplified model)
    # Head
    head_x = 0.5 * np.cos(angle)
    head_y = 0.5 * np.sin(angle)
    
    # Shoulders (wider due to heavy weight)
    shoulder_width = 0.6
    left_shoulder_x = head_x - shoulder_width * np.sin(angle)
    left_shoulder_y = head_y + shoulder_width * np.cos(angle)
    right_shoulder_x = head_x + shoulder_width * np.sin(angle)
    right_shoulder_y = head_y - shoulder_width * np.cos(angle)
    
    # Elbows (bent due to heavy weight)
    elbow_radius = 0.4
    left_elbow_x = left_shoulder_x - elbow_radius * np.sin(angle + np.pi/4)
    left_elbow_y = left_shoulder_y + elbow_radius * np.cos(angle + np.pi/4)
    right_elbow_x = right_shoulder_x - elbow_radius * np.sin(angle - np.pi/4)
    right_elbow_y = right_shoulder_y + elbow_radius * np.cos(angle - np.pi/4)
    
    # Hands (holding weight)
    hand_radius = 0.3
    left_hand_x = left_elbow_x - hand_radius * np.sin(angle + np.pi/3)
    left_hand_y = left_elbow_y + hand_radius * np.cos(angle + np.pi/3)
    right_hand_x = right_elbow_x - hand_radius * np.sin(angle - np.pi/3)
    right_hand_y = right_elbow_y + hand_radius * np.cos(angle - np.pi/3)
    
    # Torso (leaning slightly due to weight)
    torso_x = 0
    torso_y = -0.2
    
    # Hips
    hip_width = 0.5
    left_hip_x = torso_x - hip_width * np.sin(angle)
    left_hip_y = torso_y + hip_width * np.cos(angle)
    right_hip_x = torso_x + hip_width * np.sin(angle)
    right_hip_y = torso_y - hip_width * np.cos(angle)
    
    # Knees
    knee_radius = 0.6
    left_knee_x = left_hip_x - knee_radius * np.sin(angle + np.pi/6)
    left_knee_y = left_hip_y + knee_radius * np.cos(angle + np.pi/6)
    right_knee_x = right_hip_x - knee_radius * np.sin(angle - np.pi/6)
    right_knee_y = right_hip_y + knee_radius * np.cos(angle - np.pi/6)
    
    # Feet
    foot_radius = 0.4
    left_foot_x = left_knee_x - foot_radius * np.sin(angle + np.pi/4)
    left_foot_y = left_knee_y + foot_radius * np.cos(angle + np.pi/4)
    right_foot_x = right_knee_x - foot_radius * np.sin(angle - np.pi/4)
    right_foot_y = right_knee_y + foot_radius * np.cos(angle - np.pi/4)
    
    # Combine all points
    x = np.array([
        head_x, 
        left_shoulder_x, right_shoulder_x,
        left_elbow_x, right_elbow_x,
        left_hand_x, right_hand_x,
        torso_x,
        left_hip_x, right_hip_x,
        left_knee_x, right_knee_x,
        left_foot_x, right_foot_x
    ])
    
    y = np.array([
        head_y,
        left_shoulder_y, right_shoulder_y,
        left_elbow_y, right_elbow_y,
        left_hand_y, right_hand_y,
        torso_y,
        left_hip_y, right_hip_y,
        left_knee_y, right_knee_y,
        left_foot_y, right_foot_y
    ])
    
    # Add some noise to simulate natural movement
    if frame % 10 < 5:
        x += np.random.normal(0, 0.02, num_points-1)
        y += np.random.normal(0, 0.02, num_points-1)
    
    # Add a central point for balance (15th point)
    balance_x = torso_x - 0.1 * np.sin(angle)
    balance_y = torso_y - 0.3 + 0.1 * np.cos(angle)
    x = np.append(x, balance_x)
    y = np.append(y, balance_y)
    
    points.set_offsets(np.column_stack((x, y)))
    return points,

# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=total_frames, interval=1000/fps, blit=True
)

plt.tight_layout()
plt.show()
