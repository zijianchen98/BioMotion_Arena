
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Parameters
num_points = 15
num_frames = 60  # Number of frames in the animation
fps = 30  # Frames per second

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.1, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define key positions for the points (simplified jumping motion)
# Points are ordered as: head, shoulders, elbows, hands, hips, knees, feet
def get_positions(frame):
    t = frame / num_frames
    jump_height = 1.5 * np.sin(np.pi * t)  # Sinusoidal jump motion
    
    # Base positions (relative to center)
    base_positions = np.array([
        [0.0, 1.8],    # head
        [-0.5, 1.5],   # left shoulder
        [0.5, 1.5],    # right shoulder
        [-0.7, 1.2],   # left elbow
        [0.7, 1.2],    # right elbow
        [-0.9, 0.9],   # left hand
        [0.9, 0.9],    # right hand
        [-0.4, 1.0],   # left hip
        [0.4, 1.0],    # right hip
        [-0.4, 0.4],   # left knee
        [0.4, 0.4],    # right knee
        [-0.4, 0.0],   # left foot
        [0.4, 0.0],    # right foot
        [0.0, 1.2],    # torso midpoint
        [0.0, 0.7]     # waist
    ])
    
    # Apply jump height
    positions = base_positions.copy()
    positions[:, 1] += jump_height
    
    # Add some arm and leg movement during the jump
    arm_swing = 0.3 * np.sin(2 * np.pi * t)
    leg_bend = 0.2 * np.sin(2 * np.pi * t)
    
    # Modify arm positions
    positions[2, 0] += 0.1 * arm_swing  # right shoulder
    positions[3, 0] -= 0.2 * arm_swing  # left elbow
    positions[4, 0] += 0.2 * arm_swing  # right elbow
    positions[5, 0] -= 0.3 * arm_swing  # left hand
    positions[6, 0] += 0.3 * arm_swing  # right hand
    
    # Modify leg positions
    positions[9, 1] -= 0.2 * leg_bend   # left knee
    positions[10, 1] -= 0.2 * leg_bend  # right knee
    positions[11, 1] -= 0.1 * leg_bend  # left foot
    positions[12, 1] -= 0.1 * leg_bend  # right foot
    
    return positions

# Update function for animation
def update(frame):
    positions = get_positions(frame)
    for i, point in enumerate(points):
        point.center = positions[i]
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=1000/fps, blit=True)

plt.tight_layout()
plt.show()
