
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Parameters
num_points = 15
num_frames = 60  # Number of frames for the animation
fps = 30  # Frames per second

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define keyframe positions for a jumping motion
def get_keyframe(frame, total_frames):
    t = frame / total_frames * 2 * np.pi  # Normalized time
    
    # Jumping motion parameters
    jump_height = 1.5
    forward_distance = 1.0
    body_sway = 0.2 * np.sin(t * 2)  # Sway side to side
    
    # Vertical position (jumping)
    y = jump_height * np.sin(t)
    
    # Forward movement
    x_center = forward_distance * (t / (2 * np.pi)) - forward_distance / 2
    
    # Points representing a simplified human figure (head, shoulders, arms, hips, legs, feet)
    # These are relative to the center (x_center, y)
    points_pos = [
        (0 + x_center + body_sway, 0.5 + y),  # Head
        (-0.2 + x_center + body_sway, 0.3 + y),  # Left shoulder
        (0.2 + x_center + body_sway, 0.3 + y),  # Right shoulder
        (-0.4 + x_center + body_sway, 0.2 + y),  # Left elbow
        (0.4 + x_center + body_sway, 0.2 + y),  # Right elbow
        (-0.5 + x_center + body_sway, 0.0 + y),  # Left hand
        (0.5 + x_center + body_sway, 0.0 + y),  # Right hand
        (-0.2 + x_center + body_sway, -0.2 + y),  # Left hip
        (0.2 + x_center + body_sway, -0.2 + y),  # Right hip
        (-0.2 + x_center + body_sway, -0.6 + y),  # Left knee
        (0.2 + x_center + body_sway, -0.6 + y),  # Right knee
        (-0.2 + x_center + body_sway, -1.0 + y),  # Left foot
        (0.2 + x_center + body_sway, -1.0 + y),  # Right foot
        (0 + x_center + body_sway, -0.4 + y),  # Torso midpoint
        (0 + x_center + body_sway, 0.1 + y)   # Neck
    ]
    
    # Animate arm and leg movement during jump
    arm_swing = 0.3 * np.sin(t * 2)
    leg_swing = 0.4 * np.sin(t * 2 + np.pi)  # Legs move opposite to arms
    
    # Adjust arm and leg positions
    points_pos[3] = (-0.4 + x_center + body_sway + arm_swing, 0.2 + y)  # Left elbow
    points_pos[4] = (0.4 + x_center + body_sway - arm_swing, 0.2 + y)  # Right elbow
    points_pos[5] = (-0.5 + x_center + body_sway + arm_swing, 0.0 + y)  # Left hand
    points_pos[6] = (0.5 + x_center + body_sway - arm_swing, 0.0 + y)  # Right hand
    points_pos[9] = (-0.2 + x_center + body_sway + leg_swing, -0.6 + y)  # Left knee
    points_pos[10] = (0.2 + x_center + body_sway - leg_swing, -0.6 + y)  # Right knee
    points_pos[11] = (-0.2 + x_center + body_sway + leg_swing, -1.0 + y)  # Left foot
    points_pos[12] = (0.2 + x_center + body_sway - leg_swing, -1.0 + y)  # Right foot
    
    return points_pos

# Update function for animation
def update(frame):
    positions = get_keyframe(frame, num_frames)
    for i, point in enumerate(points):
        point.center = positions[i]
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=1000/fps, blit=True)

plt.tight_layout()
plt.show()
