
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
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
points = [Circle((0, 0), radius=0.03, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define the key positions for a lying down motion (e.g., slight breathing movement)
def get_positions(t):
    # Time-dependent parameters
    breathing_amplitude = 0.05 * math.sin(t * 2 * math.pi / 5)  # Slow breathing motion
    
    # Base positions (lying down, slightly curved)
    base_positions = np.array([
        [0.0, 0.6 + breathing_amplitude],    # Head
        [0.0, 0.5 + breathing_amplitude],    # Neck
        [0.0, 0.4 + breathing_amplitude],    # Shoulder center
        [-0.15, 0.35 + breathing_amplitude], # Left shoulder
        [0.15, 0.35 + breathing_amplitude],  # Right shoulder
        [-0.15, 0.2 + breathing_amplitude],  # Left elbow
        [0.15, 0.2 + breathing_amplitude],   # Right elbow
        [-0.15, 0.0 + breathing_amplitude],  # Left hand
        [0.15, 0.0 + breathing_amplitude],   # Right hand
        [0.0, 0.3 + breathing_amplitude],    # Spine center
        [0.0, 0.1 + breathing_amplitude],    # Hip center
        [-0.1, -0.1 + breathing_amplitude],  # Left knee
        [0.1, -0.1 + breathing_amplitude],   # Right knee
        [-0.1, -0.4 + breathing_amplitude],  # Left foot
        [0.1, -0.4 + breathing_amplitude]    # Right foot
    ])
    
    return base_positions

# Update function for animation
def update(t):
    positions = get_positions(t)
    for i, point in enumerate(points):
        point.set_center((positions[i, 0], positions[i, 1]))
    return points

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 5, 100), blit=True, interval=50)

plt.tight_layout()
plt.show()
