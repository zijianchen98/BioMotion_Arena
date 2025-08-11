
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib

# Set up the figure and axis
matplotlib.rcParams['toolbar'] = 'None'
fig = plt.figure(figsize=(8, 8), facecolor='black')
ax = plt.axes(xlim=(-2.5, 2.5), ylim=(-2.0, 3.0))
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_axis_off()
plt.tight_layout()

# Define the body points (15 joints) in initial pose
base_points = np.array([
    [0, 1.7, 0],    # Head
    [0, 1.5, 0],    # Neck
    [-0.4, 1.5, 0], # Right shoulder
    [-0.8, 1.5, 0], # Right elbow
    [-1.2, 1.5, 0], # Right wrist
    [0.4, 1.5, 0],  # Left shoulder
    [0.8, 1.5, 0],  # Left elbow
    [1.2, 1.5, 0],  # Left wrist
    [0, 1.0, 0],    # Torso (waist)
    [-0.3, 0.0, 0], # Right hip
    [-0.3, -0.5, 0],# Right knee
    [-0.3, -1.0, 0],# Right ankle
    [0.3, 0.0, 0],  # Left hip
    [0.3, -0.5, 0], # Left knee
    [0.3, -1.0, 0]  # Left ankle
])

# Create scatter plot for the points
scatter = ax.scatter([], [], s=100, c='white', edgecolors='black')

# Animation parameters
frames = 120
rotation_speed = 2 * np.pi / frames
bounce_amplitude = 0.1

# Update function for animation
def update(frame):
    # Calculate rotation angle and bounce
    angle = frame * rotation_speed
    bounce = bounce_amplitude * np.sin(4 * angle)
    
    # Rotate points around y-axis (vertical)
    cos_theta = np.cos(angle)
    sin_theta = np.sin(angle)
    rotated_x = base_points[:, 0] * cos_theta - base_points[:, 2] * sin_theta
    rotated_z = base_points[:, 0] * sin_theta + base_points[:, 2] * cos_theta
    rotated_y = base_points[:, 1] + bounce
    
    # Project 3D to 2D with depth effect
    x_display = rotated_x + 0.6 * rotated_z
    y_display = rotated_y
    
    # Update scatter plot data
    scatter.set_offsets(np.column_stack((x_display, y_display)))
    return scatter,

# Create and show animation
anim = FuncAnimation(fig, update, frames=frames, interval=30, blit=True)
plt.show()
