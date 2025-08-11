
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
import math

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define the key points of the body (approximate positions for a human figure)
# These are relative to the center of the body and will be rotated
body_points = {
    'head': (0, 0.8),
    'neck': (0, 0.5),
    'left_shoulder': (-0.3, 0.4),
    'right_shoulder': (0.3, 0.4),
    'left_elbow': (-0.5, 0.2),
    'right_elbow': (0.5, 0.2),
    'left_hand': (-0.6, 0.0),
    'right_hand': (0.6, 0.0),
    'torso': (0, 0.0),
    'left_hip': (-0.2, -0.3),
    'right_hip': (0.2, -0.3),
    'left_knee': (-0.2, -0.7),
    'right_knee': (0.2, -0.7),
    'left_foot': (-0.2, -1.0),
    'right_foot': (0.2, -1.0)
}

# Convert body points to a list in a specific order for the animation
point_order = [
    'head', 'neck', 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow',
    'left_hand', 'right_hand', 'torso', 'left_hip', 'right_hip', 'left_knee',
    'right_knee', 'left_foot', 'right_foot'
]
initial_positions = np.array([body_points[name] for name in point_order])

# Function to rotate points around the origin (torso)
def rotate_points(points, angle):
    rotation_matrix = np.array([
        [math.cos(angle), -math.sin(angle)],
        [math.sin(angle), math.cos(angle)]
    ])
    return np.dot(points, rotation_matrix)

# Add some slight movement to simulate walking/turning
def get_positions(frame):
    angle = frame * 0.05  # Slow rotation
    rotated = rotate_points(initial_positions, angle)
    
    # Add some slight vertical movement to simulate a heavy, sad walk
    vertical_shift = 0.1 * math.sin(frame * 0.2)
    rotated[:, 1] += vertical_shift
    
    # Add slight horizontal sway
    horizontal_shift = 0.05 * math.sin(frame * 0.15)
    rotated[:, 0] += horizontal_shift
    
    return rotated

# Update function for animation
def update(frame):
    positions = get_positions(frame)
    for i, point in enumerate(points):
        point.center = positions[i]
    return points

# Create the animation
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.tight_layout()
plt.show()
