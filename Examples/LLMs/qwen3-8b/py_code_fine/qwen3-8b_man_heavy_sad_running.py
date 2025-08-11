
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Define the number of points and the action
num_points = 15
action = 'running'
subject = 'sadman'

# Define biomechanically plausible joint angles for a running human (simplified)
# These are approximate angles in radians for key joints during running
joint_angles = {
    'hip': [0.0, 0.5, -0.3, 0.0, -0.5, 0.3, 0.0, 0.5, -0.3, 0.0, -0.5, 0.3, 0.0, 0.5, -0.3],
    'knee': [0.0, -0.8, -0.5, 0.0, -0.8, -0.5, 0.0, -0.8, -0.5, 0.0, -0.8, -0.5, 0.0, -0.8, -0.5],
    'ankle': [0.0, 0.5, 0.8, 0.0, 0.5, 0.8, 0.0, 0.5, 0.8, 0.0, 0.5, 0.8, 0.0, 0.5, 0.8],
    'shoulder': [0.0, 0.5, -0.3, 0.0, 0.5, -0.3, 0.0, 0.5, -0.3, 0.0, 0.5, -0.3, 0.0, 0.5, -0.3],
    'elbow': [0.0, -0.8, -0.5, 0.0, -0.8, -0.5, 0.0, -0.8, -0.5, 0.0, -0.8, -0.5, 0.0, -0.8, -0.5],
    'wrist': [0.0, 0.5, 0.8, 0.0, 0.5, 0.8, 0.0, 0.5, 0.8, 0.0, 0.5, 0.8, 0.0, 0.5, 0.8],
}

# Define body segments (lengths in arbitrary units)
body_segments = {
    'hip': 0.3,
    'knee': 0.25,
    'ankle': 0.2,
    'shoulder': 0.3,
    'elbow': 0.25,
    'wrist': 0.2,
}

# Define body structure (simplified as a chain)
body_structure = [
    ('hip', 'knee', 'ankle'),
    ('shoulder', 'elbow', 'wrist'),
]

# Define initial positions
positions = {}
for joint in joint_angles:
    positions[joint] = np.array([0.0, 0.0])

# Function to update positions based on joint angles
def update_positions(joint_angles, body_segments, positions):
    for segment in body_structure:
        for i, joint in enumerate(segment):
            if i == 0:
                # Start from the origin
                pos = np.array([0.0, 0.0])
            else:
                # Previous joint position
                pos = positions[segment[i - 1]]
            # Apply rotation based on joint angle
            rotation = np.array([
                [np.cos(joint_angles[joint][frame]), -np.sin(joint_angles[joint][frame])],
                [np.sin(joint_angles[joint][frame]), np.cos(joint_angles[joint][frame])]
            ])
            # Apply segment length
            pos = pos + body_segments[joint] * rotation @ np.array([1.0, 0.0])
            positions[joint] = pos

# Define the points (approximate locations on the body)
point_positions = {
    'hip': 'hip',
    'knee': 'knee',
    'ankle': 'ankle',
    'shoulder': 'shoulder',
    'elbow': 'elbow',
    'wrist': 'wrist',
    'chest': 'shoulder',
    'head': 'shoulder',
    'neck': 'shoulder',
    'spine': 'hip',
    'elbow': 'elbow',
    'wrist': 'wrist',
    'ankle': 'ankle',
    'knee': 'knee',
    'hip': 'hip',
}

# Create a list of point names
point_names = list(point_positions.keys())

# Initialize figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.axis('off')

# Create point light patches
points = [patches.Circle((0, 0), 0.05, color='white') for _ in range(num_points)]
for p in points:
    ax.add_patch(p)

# Function to animate
def animate(frame):
    update_positions(joint_angles, body_segments, positions)
    for i, name in enumerate(point_names):
        joint = point_positions[name]
        x, y = positions[joint]
        points[i].center = (x, y)

# Create animation
ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=False)

plt.show()
