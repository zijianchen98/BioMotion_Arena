
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
import math

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
ax.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define key points for a happy woman turning around
def get_key_points(frame):
    t = frame / total_frames * 2 * math.pi  # Normalized time for a full turn
    
    # Head (1 point)
    head_x = 0.5 * math.cos(t)
    head_y = 0.5 * math.sin(t) + 0.5
    
    # Shoulders (2 points)
    shoulder_width = 0.6
    left_shoulder_x = -shoulder_width/2 * math.cos(t) - 0.1 * math.sin(t)
    left_shoulder_y = shoulder_width/2 * math.sin(t) - 0.1 * math.cos(t)
    right_shoulder_x = shoulder_width/2 * math.cos(t) - 0.1 * math.sin(t)
    right_shoulder_y = -shoulder_width/2 * math.sin(t) - 0.1 * math.cos(t)
    
    # Elbows (2 points)
    elbow_angle = math.pi/3
    left_elbow_x = left_shoulder_x + 0.4 * math.cos(t + elbow_angle)
    left_elbow_y = left_shoulder_y + 0.4 * math.sin(t + elbow_angle)
    right_elbow_x = right_shoulder_x + 0.4 * math.cos(t - elbow_angle)
    right_elbow_y = right_shoulder_y + 0.4 * math.sin(t - elbow_angle)
    
    # Hands (2 points)
    left_hand_x = left_elbow_x + 0.3 * math.cos(t + elbow_angle + 0.2)
    left_hand_y = left_elbow_y + 0.3 * math.sin(t + elbow_angle + 0.2)
    right_hand_x = right_elbow_x + 0.3 * math.cos(t - elbow_angle - 0.2)
    right_hand_y = right_elbow_y + 0.3 * math.sin(t - elbow_angle - 0.2)
    
    # Torso (1 point - waist)
    waist_x = 0
    waist_y = -0.2
    
    # Hips (2 points)
    hip_width = 0.7
    left_hip_x = -hip_width/2 * math.cos(t) + 0.1 * math.sin(t)
    left_hip_y = -0.5 + hip_width/2 * math.sin(t) + 0.1 * math.cos(t)
    right_hip_x = hip_width/2 * math.cos(t) + 0.1 * math.sin(t)
    right_hip_y = -0.5 - hip_width/2 * math.sin(t) + 0.1 * math.cos(t)
    
    # Knees (2 points)
    knee_angle = math.pi/4
    left_knee_x = left_hip_x + 0.5 * math.cos(t + knee_angle)
    left_knee_y = left_hip_y - 0.5 * math.sin(t + knee_angle)
    right_knee_x = right_hip_x + 0.5 * math.cos(t - knee_angle)
    right_knee_y = right_hip_y - 0.5 * math.sin(t - knee_angle)
    
    # Feet (2 points)
    left_foot_x = left_knee_x + 0.4 * math.cos(t + knee_angle - 0.1)
    left_foot_y = left_knee_y - 0.4 * math.sin(t + knee_angle - 0.1)
    right_foot_x = right_knee_x + 0.4 * math.cos(t - knee_angle + 0.1)
    right_foot_y = right_knee_y - 0.4 * math.sin(t - knee_angle + 0.1)
    
    # Happy expression (1 point - mouth, represented as a smile)
    mouth_x = 0.5 * math.cos(t) + 0.1 * math.sin(t)
    mouth_y = 0.5 * math.sin(t) + 0.3
    
    return [
        (head_x, head_y),  # head
        (left_shoulder_x, left_shoulder_y),  # left shoulder
        (right_shoulder_x, right_shoulder_y),  # right shoulder
        (left_elbow_x, left_elbow_y),  # left elbow
        (right_elbow_x, right_elbow_y),  # right elbow
        (left_hand_x, left_hand_y),  # left hand
        (right_hand_x, right_hand_y),  # right hand
        (waist_x, waist_y),  # waist
        (left_hip_x, left_hip_y),  # left hip
        (right_hip_x, right_hip_y),  # right hip
        (left_knee_x, left_knee_y),  # left knee
        (right_knee_x, right_knee_y),  # right knee
        (left_foot_x, left_foot_y),  # left foot
        (right_foot_x, right_foot_y),  # right foot
        (mouth_x, mouth_y)  # mouth (smile)
    ]

# Update function for animation
def update(frame):
    key_points = get_key_points(frame)
    for i, point in enumerate(points):
        point.center = key_points[i]
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=total_frames, interval=1000/fps, blit=True)

plt.tight_layout()
plt.show()
