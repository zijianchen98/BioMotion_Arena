
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_LIGHTS = 15
FRAMES = 100
FPS = 30

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create point lights
points, = ax.plot([], [], 'o', color='white', markersize=5)

# Generate initial positions
theta = np.linspace(0, 2 * np.pi, NUM_LIGHTS, endpoint=False)
x = np.cos(theta)
y = np.sin(theta)
z = np.zeros_like(x)

# Function to update frame
def update(frame):
    # Calculate angle based on frame
    angle = frame / FRAMES * 2 * np.pi
    
    # Apply rotation matrix for turning around
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])
    
    # Rotate points
    rotated_points = np.dot(rotation_matrix, np.vstack([x, y, z]))
    
    # Update positions
    points.set_data(rotated_points[0], rotated_points[1])
    return points,

# Create animation
animation = FuncAnimation(fig, update, frames=FRAMES, interval=1000/FPS, blit=True)

# Show animation
plt.show()
