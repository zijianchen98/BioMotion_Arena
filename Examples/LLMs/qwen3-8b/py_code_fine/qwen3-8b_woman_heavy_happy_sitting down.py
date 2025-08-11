
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define the 15 points representing the body (simplified human figure)
# These are approximate joint positions for a sitting woman
body_points = np.array([
    [0.0, 0.0],        # Hip (center)
    [0.2, 0.0],        # Right hip
    [0.4, 0.1],        # Right knee
    [0.3, 0.3],        # Right ankle
    [-0.2, 0.0],       # Left hip
    [-0.4, 0.1],       # Left knee
    [-0.3, 0.3],       # Left ankle
    [0.0, 0.5],        # Torso
    [0.1, 0.7],        # Right shoulder
    [0.2, 0.9],        # Right elbow
    [0.0, 1.0],        # Right hand
    [-0.1, 0.7],       # Left shoulder
    [-0.2, 0.9],       # Left elbow
    [-0.0, 1.0],       # Left hand
    [0.0, 0.3]         # Spine (center)
])

# Normalize positions to fit in the [-1, 1] range
body_points = body_points / np.max(np.abs(body_points)) * 1.0

# Create circles for the point-lights
points = [Circle((body_points[i][0], body_points[i][1]), 0.02, color='white') for i in range(15)]
for p in points:
    ax.add_patch(p)

# Define a function to animate the movement
def animate(frame):
    # Define a simple realistic motion for sitting down
    # This is a simplified biomechanical model
    # We'll simulate a smooth descent of the body
    t = frame / 50.0  # Normalize time
    scale = 1.0 - 0.5 * (1 - np.cos(np.pi * t))  # Smooth transition
    body_points[:, 1] = body_points[:, 1] * scale  # Move down
    body_points[:, 0] = body_points[:, 0] * (1 - 0.5 * t)  # Slight horizontal shift

    # Update positions of the circles
    for i, p in enumerate(points):
        p.center = (body_points[i][0], body_points[i][1])

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=False)

# Show the animation
plt.show()
