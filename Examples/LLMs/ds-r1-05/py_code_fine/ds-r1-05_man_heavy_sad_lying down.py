
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the 15 body points in a neutral lying position (x, y, z)
points_list_neutral = np.array([
    [0.0, 0.0, 0.4],    # head
    [0.1, 0.0, 0.3],    # neck
    [0.1, -0.4, 0.1],   # left shoulder
    [0.1, 0.4, 0.1],    # right shoulder
    [-0.1, -0.6, 0.0],  # left elbow
    [-0.1, 0.6, 0.0],   # right elbow
    [-0.3, -0.6, 0.0],  # left wrist
    [-0.3, 0.6, 0.0],   # right wrist
    [0.4, 0.0, 0.0],    # torso
    [0.7, -0.2, 0.0],   # left hip
    [0.7, 0.2, 0.0],    # right hip
    [1.0, -0.2, 0.0],   # left knee
    [1.0, 0.2, 0.0],    # right knee
    [1.2, -0.2, 0.0],   # left ankle
    [1.2, 0.2, 0.0]     # right ankle
], dtype=float)

# Indices of points that move with breathing (head, neck, shoulders, torso)
breathing_indices = [0, 1, 2, 3, 8]

# Animation parameters
fps = 30  # Frames per second
amplitude = 0.06  # Breathing amplitude (z-axis movement)
period = 4.0  # Breathing cycle duration in seconds
total_duration = 10.0  # Total duration of animation in seconds
total_frames = int(total_duration * fps)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-0.6, 1.6)
ax.set_ylim(-0.1, 0.5)

# Initialize scatter plot for points
scat = ax.scatter([], [], s=70, c='white', edgecolors='none')

# Projection: Convert 3D (x, y, z) to 2D screen (x, y)
def project(points):
    screen_x = points[:, 0] - 0.3 * points[:, 1]  # Adjust for depth (y) using oblique projection
    screen_y = points[:, 2]  # Height (z) becomes screen y
    return screen_x, screen_y

# Update function for animation
def update(frame):
    t = frame / fps  # Time in seconds
    # Create a copy of the neutral points
    points_list = points_list_neutral.copy()
    # Adjust z-coordinates for breathing points
    for idx in breathing_indices:
        points_list[idx, 2] = points_list_neutral[idx, 2] + amplitude * np.sin(2 * np.pi * t / period)
    # Project to 2D
    x_proj, y_proj = project(points_list)
    # Update scatter plot
    scat.set_offsets(np.column_stack([x_proj, y_proj]))
    return scat,

# Initialize by projecting neutral points
def init():
    x_proj, y_proj = project(points_list_neutral)
    scat.set_offsets(np.column_stack([x_proj, y_proj]))
    return scat,

# Create animation
anim = FuncAnimation(
    fig,
    update,
    frames=total_frames,
    init_func=init,
    blit=True,
    interval=1000 // fps  # Frame delay in ms
)

plt.show()
