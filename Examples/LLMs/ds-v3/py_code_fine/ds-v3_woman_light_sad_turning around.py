
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points, = ax.plot([], [], 'wo', markersize=8)

# Define the motion parameters
frames_per_cycle = 60  # Number of frames for a full turn
total_frames = frames_per_cycle * 2  # Total frames for the animation

# Define the point-light positions relative to the body
# These are approximate positions for a human figure turning around
def get_body_points(phase):
    # Phase varies from 0 to 2*pi for a full turn
    # Body is turning in place, so the points will rotate around the vertical axis
    
    # Main body points (x, y is up, x is left-right)
    body_points = np.array([
        [0.0, 1.2],    # Head
        [0.0, 0.9],    # Neck
        [0.0, 0.7],    # Shoulder center
        [-0.2, 0.6],   # Left shoulder
        [0.2, 0.6],    # Right shoulder
        [-0.2, 0.3],   # Left elbow
        [0.2, 0.3],    # Right elbow
        [-0.2, 0.0],   # Left hand
        [0.2, 0.0],    # Right hand
        [0.0, 0.5],    # Torso top
        [0.0, 0.0],    # Torso bottom
        [-0.15, -0.2], # Left knee
        [0.15, -0.2],  # Right knee
        [-0.15, -0.5], # Left foot
        [0.15, -0.5]   # Right foot
    ])
    
    # Add slight movement to simulate walking/turning
    # The figure is turning, so the x-coordinates will change based on phase
    # The y-coordinates may have slight bobbing
    rotated_points = body_points.copy()
    
    # Rotate points around the y-axis (simulate turning)
    rotation_matrix = np.array([
        [np.cos(phase), -np.sin(phase)],
        [np.sin(phase), np.cos(phase)]
    ])
    
    for i in range(len(rotated_points)):
        rotated_points[i, :2] = np.dot(rotation_matrix, rotated_points[i, :2])
    
    # Add slight vertical bobbing for the head and shoulders (sad, slow movement)
    bobbing = 0.05 * np.sin(2 * phase)
    rotated_points[0, 1] += bobbing  # Head
    rotated_points[1, 1] += bobbing * 0.8  # Neck
    rotated_points[2, 1] += bobbing * 0.6  # Shoulders
    
    # Arms movement (sad, slow swinging)
    arm_swing = 0.1 * np.sin(phase)
    rotated_points[3:9:2, 0] += arm_swing * 0.5  # Left arm
    rotated_points[4:9:2, 0] -= arm_swing * 0.5  # Right arm
    
    return rotated_points

# Animation update function
def update(frame):
    phase = 2 * np.pi * frame / frames_per_cycle
    current_points = get_body_points(phase)
    points.set_data(current_points[:, 0], current_points[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=total_frames, interval=50, blit=True
)

plt.tight_layout()
plt.show()
