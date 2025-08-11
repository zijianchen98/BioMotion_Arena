
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math

plt.rcParams['toolbar'] = 'None'

# Set up the figure and axis
fig = plt.figure(facecolor='black')
ax = plt.axes(xlim=(-1, 1), ylim=(-0.4, 1.0), aspect='equal')
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Total frames and max rotation angle
total_frames = 75
max_angle = 25 * math.pi / 180  # 25 degrees in radians

# Initial points (x, y) for standing position: 15 points
points = np.array([
    [0.0, 0.9],     # Head
    [0.0, 0.8],     # Neck
    [-0.15, 0.8],    # Left Shoulder
    [0.15, 0.8],     # Right Shoulder
    [-0.25, 0.65],   # Left Elbow
    [0.25, 0.65],    # Right Elbow
    [-0.35, 0.5],    # Left Wrist
    [0.35, 0.5],     # Right Wrist
    [0.0, 0.65],     # Torso (center)
    [-0.15, 0.45],   # Left Hip
    [0.15, 0.45],    # Right Hip
    [-0.15, 0.25],   # Left Knee
    [0.15, 0.25],    # Right Knee
    [-0.15, 0.05],   # Left Ankle
    [0.15, 0.05]     # Right Ankle
])

# Create scatter plot with white points
scat = ax.scatter(points[:,0], points[:,1], s=50, c='white', edgecolor='white', marker='o')

def rotate_point(point, hip_center, angle):
    """Rotate a point around a pivot point."""
    px, py = hip_center
    ox, oy = point
    qx = px + math.cos(angle) * (ox - px) - math.sin(angle) * (oy - py)
    qy = py + math.sin(angle) * (ox - px) + math.cos(angle) * (oy - py)
    return [qx, qy]

def update(frame):
    """Update function for animation frames."""
    global points
    
    # Calculate the current angle for bowing using sinusoidal pattern
    angle = max_angle * math.sin(frame * math.pi / total_frames)
    
    pivot_point = [0.0, 0.45]  # Hip center
    
    # Update points: rotate only upper body (points 0 to 8)
    new_points = points.copy()
    for i in range(9):  # Rotate head to torso points
        new_points[i] = rotate_point(points[i], pivot_point, angle)
    
    scat.set_offsets(new_points)
    return scat,

# Create animation
ani = FuncAnimation(fig, update, frames=total_frames, interval=40, blit=True)

plt.tight_layout()
plt.show()
