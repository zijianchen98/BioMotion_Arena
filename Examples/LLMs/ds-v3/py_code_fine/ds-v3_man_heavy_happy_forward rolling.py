
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
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define the motion of a forward rolling (somersault) motion
def get_point_positions(frame):
    t = frame / fps  # time in seconds
    
    # Key points for a somersault motion (simplified)
    # Head, shoulders, elbows, hands, hips, knees, feet
    # Using parametric equations for a rolling motion
    
    # Center of mass trajectory (rolling forward)
    roll_radius = 0.5
    com_x = roll_radius * (t * 2 * np.pi / duration - np.pi/2)
    com_y = -roll_radius * np.cos(t * 2 * np.pi / duration)
    
    # Limb positions relative to COM
    # Phase for limb movement
    phase = t * 2 * np.pi / duration
    
    # Head
    head_x = com_x
    head_y = com_y + 0.3 * np.sin(phase)
    
    # Shoulders
    shoulder_y = com_y - 0.1 * np.cos(phase)
    left_shoulder_x = com_x - 0.2
    right_shoulder_x = com_x + 0.2
    
    # Elbows
    elbow_phase = phase + np.pi/4
    left_elbow_x = left_shoulder_x - 0.15 * np.cos(elbow_phase)
    left_elbow_y = shoulder_y - 0.15 * np.sin(elbow_phase)
    right_elbow_x = right_shoulder_x + 0.15 * np.cos(elbow_phase)
    right_elbow_y = shoulder_y - 0.15 * np.sin(elbow_phase)
    
    # Hands
    hand_phase = phase + np.pi/2
    left_hand_x = left_elbow_x - 0.15 * np.cos(hand_phase)
    left_hand_y = left_elbow_y - 0.15 * np.sin(hand_phase)
    right_hand_x = right_elbow_x + 0.15 * np.cos(hand_phase)
    right_hand_y = right_elbow_y - 0.15 * np.sin(hand_phase)
    
    # Hips
    hip_y = com_y - 0.2 * np.cos(phase + np.pi)
    left_hip_x = com_x - 0.15
    right_hip_x = com_x + 0.15
    
    # Knees
    knee_phase = phase + np.pi * 0.75
    left_knee_x = left_hip_x - 0.2 * np.cos(knee_phase)
    left_knee_y = hip_y - 0.2 * np.sin(knee_phase)
    right_knee_x = right_hip_x + 0.2 * np.cos(knee_phase)
    right_knee_y = hip_y - 0.2 * np.sin(knee_phase)
    
    # Feet
    foot_phase = phase + np.pi
    left_foot_x = left_knee_x - 0.2 * np.cos(foot_phase)
    left_foot_y = left_knee_y - 0.2 * np.sin(foot_phase)
    right_foot_x = right_knee_x + 0.2 * np.cos(foot_phase)
    right_foot_y = right_knee_y - 0.2 * np.sin(foot_phase)
    
    # Additional points for more detail (e.g., torso, mid-limbs)
    torso_x = com_x
    torso_y = (shoulder_y + hip_y) / 2
    
    # Return all point positions
    return [
        (head_x, head_y),  # 0
        (left_shoulder_x, shoulder_y),  # 1
        (right_shoulder_x, shoulder_y),  # 2
        (left_elbow_x, left_elbow_y),  # 3
        (right_elbow_x, right_elbow_y),  # 4
        (left_hand_x, left_hand_y),  # 5
        (right_hand_x, right_hand_y),  # 6
        (torso_x, torso_y),  # 7
        (left_hip_x, hip_y),  # 8
        (right_hip_x, hip_y),  # 9
        (left_knee_x, left_knee_y),  # 10
        (right_knee_x, right_knee_y),  # 11
        (left_foot_x, left_foot_y),  # 12
        (right_foot_x, right_foot_y),  # 13
        (com_x, com_y)  # 14 (center of mass)
    ]

# Animation update function
def update(frame):
    positions = get_point_positions(frame)
    for i, point in enumerate(points):
        point.center = positions[i]
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=total_frames, interval=1000/fps, blit=True)

plt.tight_layout()
plt.show()
