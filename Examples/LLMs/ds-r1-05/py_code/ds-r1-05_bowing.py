
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 points (upright pose)
points0 = np.array([
    [0.0, 1.0],    # 0: head
    [0.0, 0.7],    # 1: neck
    [-0.3, 0.7],   # 2: left shoulder
    [0.3, 0.7],    # 3: right shoulder
    [-0.4, 0.3],   # 4: left elbow
    [0.4, 0.3],    # 5: right elbow
    [-0.5, 0.0],   # 6: left wrist
    [0.5, 0.0],    # 7: right wrist
    [0.0, 0.0],    # 8: waist (center)
    [-0.3, 0.0],   # 9: left hip
    [0.3, 0.0],    # 10: right hip
    [-0.3, -0.5],  # 11: left knee
    [0.3, -0.5],   # 12: right knee
    [-0.3, -1.0],  # 13: left ankle
    [0.3, -1.0]    # 14: right ankle
])

# Total duration of the animation in seconds
total_duration = 2.0
# Frames per second
fps = 30
# Total frames
total_frames = int(total_duration * fps)
# Maximum rotation angle (45 degrees in radians)
max_angle = 45.0 * np.pi / 180.0

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')
fig.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the scatter plot for the points with white color and larger size
scat = ax.scatter([], [], color='white', s=40)

def update(frame):
    """Update function for each frame of the animation."""
    t = frame / total_frames
    # Calculate rotation angle using sinusoidal function for smooth motion
    theta = max_angle * np.sin(np.pi * t)
    
    # Copy the initial points to avoid modifying the original
    points = points0.copy()
    
    # Apply rotation to the upper body points (0 to 7) around the waist (point 8)
    for i in range(8):
        dy = points0[i, 1] - points0[8, 1]  # Translate to waist's y
        new_y = points0[8, 1] + dy * np.cos(theta)  # Rotate around the waist
        points[i, 1] = new_y
    
    # Update scatter plot data
    scat.set_offsets(points)
    return scat,

# Create the animation
anim = FuncAnimation(
    fig, update, frames=total_frames, interval=1000/fps, blit=True
)

plt.tight_layout()
plt.show()
