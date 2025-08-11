
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Parameters
num_points = 15
num_frames = 100
fps = 30

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define keyframes for sitting down motion (simplified)
def get_position(frame, point_idx):
    t = frame / num_frames
    
    # Key joint positions (simplified for a sitting motion)
    if point_idx == 0:  # Head
        x = 0.1 * np.sin(2 * np.pi * t)
        y = 1.0 - 0.8 * t
    elif point_idx == 1:  # Neck
        x = 0.05 * np.sin(2 * np.pi * t)
        y = 0.9 - 0.7 * t
    elif point_idx == 2:  # Left shoulder
        x = -0.3 + 0.1 * np.sin(2 * np.pi * t)
        y = 0.8 - 0.6 * t
    elif point_idx == 3:  # Right shoulder
        x = 0.3 + 0.1 * np.sin(2 * np.pi * t)
        y = 0.8 - 0.6 * t
    elif point_idx == 4:  # Left elbow
        x = -0.4 + 0.1 * np.sin(2 * np.pi * t)
        y = 0.6 - 0.5 * t
    elif point_idx == 5:  # Right elbow
        x = 0.4 + 0.1 * np.sin(2 * np.pi * t)
        y = 0.6 - 0.5 * t
    elif point_idx == 6:  # Left hand
        x = -0.5 + 0.1 * np.sin(2 * np.pi * t)
        y = 0.4 - 0.3 * t
    elif point_idx == 7:  # Right hand
        x = 0.5 + 0.1 * np.sin(2 * np.pi * t)
        y = 0.4 - 0.3 * t
    elif point_idx == 8:  # Torso (mid)
        x = 0.0
        y = 0.7 - 0.7 * t
    elif point_idx == 9:  # Hip
        x = 0.0
        y = 0.5 - 0.5 * t
    elif point_idx == 10:  # Left knee
        x = -0.2
        y = 0.3 - 0.3 * t
    elif point_idx == 11:  # Right knee
        x = 0.2
        y = 0.3 - 0.3 * t
    elif point_idx == 12:  # Left foot
        x = -0.2
        y = 0.1 - 0.1 * t
    elif point_idx == 13:  # Right foot
        x = 0.2
        y = 0.1 - 0.1 * t
    elif point_idx == 14:  # Additional point (e.g., back)
        x = 0.0 + 0.05 * np.sin(2 * np.pi * t)
        y = 0.6 - 0.6 * t
    
    return x, y

# Update function for animation
def update(frame):
    for i, point in enumerate(points):
        x, y = get_position(frame, i)
        point.center = (x, y)
    return points

# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, interval=1000/fps, blit=True
)

plt.tight_layout()
plt.show()
