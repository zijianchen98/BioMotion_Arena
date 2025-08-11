
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Ellipse
import math

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points = [ax.plot([], [], 'o', color='white', markersize=8)[0] for _ in range(num_points)]

# Define key body points (approximate positions for a lying down person)
# These are in a coordinate system where the person is lying horizontally
body_points = {
    'head': (0, 0.5),
    'neck': (0, 0.3),
    'left_shoulder': (-0.2, 0.25),
    'right_shoulder': (0.2, 0.25),
    'left_elbow': (-0.3, 0.1),
    'right_elbow': (0.3, 0.1),
    'left_hand': (-0.4, -0.1),
    'right_hand': (0.4, -0.1),
    'torso': (0, 0.0),
    'left_hip': (-0.2, -0.2),
    'right_hip': (0.2, -0.2),
    'left_knee': (-0.2, -0.5),
    'right_knee': (0.2, -0.5),
    'left_ankle': (-0.2, -0.8),
    'right_ankle': (0.2, -0.8)
}

# Convert body points to a list in a specific order
point_order = [
    'head', 'neck', 'left_shoulder', 'right_shoulder',
    'left_elbow', 'right_elbow', 'left_hand', 'right_hand',
    'torso', 'left_hip', 'right_hip', 'left_knee',
    'right_knee', 'left_ankle', 'right_ankle'
]
initial_positions = np.array([body_points[name] for name in point_order])

# Breathing and slight movement parameters
def get_positions(t):
    # Time-dependent parameters
    breathing_amplitude = 0.05 * math.sin(t * 2 * math.pi / 5)  # Slow breathing
    leg_movement = 0.1 * math.sin(t * 2 * math.pi / 3)  # Slight leg movement
    
    # Modify initial positions
    positions = initial_positions.copy()
    
    # Breathing affects torso and shoulders
    positions[2:8, 1] += breathing_amplitude * 0.5  # Shoulders, elbows, hands
    positions[8, 1] += breathing_amplitude  # Torso
    
    # Slight leg movement
    positions[10:, 1] += leg_movement * 0.5  # Hips, knees, ankles
    
    # Random tiny jitter for realism
    jitter = np.random.normal(0, 0.01, (num_points, 2))
    positions += jitter
    
    return positions

# Animation update function
def update(frame):
    t = frame * 0.1  # Slow down the animation
    positions = get_positions(t)
    for i, point in enumerate(points):
        point.set_data(positions[i, 0], positions[i, 1])
    return points

# Create the animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.tight_layout()
plt.show()
