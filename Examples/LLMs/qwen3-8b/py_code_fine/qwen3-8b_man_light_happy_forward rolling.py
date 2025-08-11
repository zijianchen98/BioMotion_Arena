
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define the 15 body points (approximate human body points)
body_points = [
    [0, 0],        # Hip
    [0.2, 0.2],    # Knee
    [0.4, 0.4],    # Ankle
    [0.1, 0.1],    # Shoulder
    [0.3, 0.3],    # Elbow
    [0.5, 0.5],    # Wrist
    [0.0, 0.0],    # Head
    [0.05, 0.05],  # Neck
    [0.1, 0.1],    # Spine
    [0.15, 0.15],  # Spine
    [0.2, 0.2],    # Spine
    [0.25, 0.25],  # Spine
    [0.3, 0.3],    # Spine
    [0.35, 0.35],  # Spine
    [0.4, 0.4]     # Spine
]

# Define the motion parameters for a forward rolling motion
def forward_rolling(t):
    # Simulate a rolling motion with periodic sine waves
    # Each point moves with a different phase and amplitude
    points = []
    for i, (x, y) in enumerate(body_points):
        # Define motion parameters for each point
        phase = i * 0.2
        amplitude = 0.1
        x_offset = amplitude * np.sin(t + phase)
        y_offset = amplitude * np.cos(t + phase)
        points.append([x + x_offset, y + y_offset])
    return points

# Create the point lights
points = []
for x, y in body_points:
    point = ax.scatter(x, y, color='white', s=50, zorder=5)
    points.append(point)

# Animation function
def animate(t):
    positions = forward_rolling(t)
    for i, (x, y) in enumerate(positions):
        points[i].set_offsets([x, y])

# Create the animation
ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=False)

plt.show()
