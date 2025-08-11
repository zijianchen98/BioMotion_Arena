
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial (standing) 2D skeleton marker positions.
# 15 markers: 0=head,1=neck,2=sternum,3=L shoulder,4=R shoulder,
# 5=L elbow,6=R elbow,7=L wrist,8=R wrist,
# 9=L hip,10=R hip,11=L knee,12=R knee,13=L ankle,14=R ankle
base_positions = np.array([
    ( 0.0,  1.10),  # head
    ( 0.0,  1.00),  # neck
    ( 0.0,  0.90),  # sternum
    (-0.20, 1.00),  # L shoulder
    ( 0.20, 1.00),  # R shoulder
    (-0.20, 0.80),  # L elbow
    ( 0.20, 0.80),  # R elbow
    (-0.20, 0.60),  # L wrist
    ( 0.20, 0.60),  # R wrist
    (-0.10, 0.60),  # L hip
    ( 0.10, 0.60),  # R hip
    (-0.10, 0.10),  # L knee
    ( 0.10, 0.10),  # R knee
    (-0.10, -0.40), # L ankle
    ( 0.10, -0.40), # R ankle
])

# Compute hip center about which the upper body will rotate
hip_center = ((base_positions[9] + base_positions[10]) / 2.0)

# Animation parameters
num_frames = 120
interval = 40  # ms between frames
max_bow_angle = np.deg2rad(45)  # maximum forward flexion angle

# Set up the plot
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(-0.6, 1.2)
ax.axis('off')

# Initial scatter of the 15 points
scatter = ax.scatter(
    base_positions[:, 0],
    base_positions[:, 1],
    c='white',
    s=50
)

def rotate_point(pt, center, angle):
    """Rotate a 2D point pt around center by angle (radians)."""
    # Translate to origin
    x, y = pt - center
    # Rotation
    xr = x * np.cos(angle) - y * np.sin(angle)
    yr = x * np.sin(angle) + y * np.cos(angle)
    # Translate back
    return np.array((xr, yr)) + center

def update(frame):
    # Compute a smooth forward-and-back bow angle
    # We use a sine function that goes 0 -> max -> 0 over the cycle
    theta = max_bow_angle * np.sin(2 * np.pi * frame / num_frames)
    
    # Create a copy of the base positions
    new_positions = base_positions.copy()
    
    # Rotate only the upper body and arms (markers 0 through 8) around the hip center
    for i in range(0, 9):
        new_positions[i] = rotate_point(base_positions[i], hip_center, -theta)
    
    scatter.set_offsets(new_positions)
    return scatter,

# Build the animation
ani = FuncAnimation(
    fig, update, frames=num_frames, interval=interval, blit=True
)

plt.show()
