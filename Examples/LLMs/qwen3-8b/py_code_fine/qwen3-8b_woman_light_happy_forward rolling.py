
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

# Define the 15 body points (approximate human body points for a woman)
body_points = np.array([
    [0.0, 0.0],     # Spine (center)
    [0.1, 0.1],     # Head
    [0.2, 0.05],    # Right shoulder
    [0.3, 0.0],     # Right elbow
    [0.4, -0.05],   # Right wrist
    [-0.2, 0.05],   # Left shoulder
    [-0.3, 0.0],    # Left elbow
    [-0.4, -0.05],  # Left wrist
    [0.1, -0.2],    # Right hip
    [0.15, -0.4],   # Right knee
    [0.1, -0.6],    # Right ankle
    [-0.1, -0.2],   # Left hip
    [-0.15, -0.4],  # Left knee
    [-0.1, -0.6],   # Left ankle
    [0.0, -0.8]     # Pelvis
])

# Define a biomechanically plausible motion for a forward rolling motion
def forward_rolling(t, amplitude=0.1, frequency=0.1, phase=0):
    # Create a rolling motion with a sine wave
    body_points[:, 1] += amplitude * np.sin(2 * np.pi * frequency * t + phase)
    body_points[:, 0] += amplitude * np.cos(2 * np.pi * frequency * t + phase)

# Create the point lights
points = [Circle((0, 0), 0.02, color='white') for _ in range(15)]
for point in points:
    ax.add_patch(point)

# Animation function
def animate(t):
    for i, point in enumerate(points):
        x, y = body_points[i]
        point.set_center((x, y))
    forward_rolling(t)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=False)

plt.show()
