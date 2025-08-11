
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
frames = 180
fps = 30
radius = 1.0

# Initial positions of the point-lights for a standing figure
initial_positions = np.array([
    [0, 0],  # Head
    [-0.2, 0.4], [-0.2, 0.8], [-0.2, 1.2],  # Left arm
    [0.2, 0.4], [0.2, 0.8], [0.2, 1.2],   # Right arm
    [-0.2, -0.4], [-0.2, -0.8],           # Left leg
    [0.2, -0.4], [0.2, -0.8],            # Right leg
    [0, -1.2],                           # Pelvis
    [-0.6, -1.6], [0.6, -1.6]             # Feet
])

# Function to create a circular path for each light
def circular_path(t, center, radius, phase):
    x = center[0] + radius * np.cos(t + phase)
    y = center[1] + radius * np.sin(t + phase)
    return x, y

# Generate paths for turning around
paths = []
for i in range(num_lights):
    phase = i * (2 * np.pi / num_lights)
    if i < 3:  # Left arm
        paths.append(lambda t, p=phase: circular_path(t, [-0.2, 0.4], 0.2, p))
    elif i < 6:  # Right arm
        paths.append(lambda t, p=phase: circular_path(t, [0.2, 0.4], 0.2, p))
    elif i < 9:  # Left leg
        paths.append(lambda t, p=phase: circular_path(t, [-0.2, -0.4], 0.2, p))
    elif i < 12:  # Right leg
        paths.append(lambda t, p=phase: circular_path(t, [0.2, -0.4], 0.2, p))
    else:  # Body parts
        paths.append(lambda t, p=phase: circular_path(t, initial_positions[i], 0.1, p))

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis('off')

# Create scatter plot for point-lights
scat = ax.scatter([], [], s=100, c='white')

# Update function for animation
def update(frame):
    t = frame / fps
    positions = np.array([path(t) for path in paths])
    scat.set_offsets(positions)

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Show plot
plt.show()
