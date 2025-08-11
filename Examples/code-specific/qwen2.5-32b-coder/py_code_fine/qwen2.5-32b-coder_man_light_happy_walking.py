
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_POINTS = 15
FPS = 30
DURATION = 5  # seconds
FRAME_COUNT = FPS * DURATION

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(-1, 1)
ax.set_ylim(-0.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Initial positions for the points (simplified walking pose)
initial_positions = np.array([
    [0, 0],   # Head
    [-0.1, -0.1], [0.1, -0.1],  # Shoulders
    [-0.2, -0.3], [0.2, -0.3],  # Elbows
    [-0.2, -0.6], [0.2, -0.6],  # Hands
    [0, -0.2],  # Torso
    [-0.1, -0.7], [0.1, -0.7],  # Hips
    [-0.2, -1.0], [0.2, -1.0],  # Knees
    [-0.2, -1.3], [0.2, -1.3],  # Feet
    [0, -0.9]   # Pelvis
])

# Create scatter plot for points
points, = ax.plot([], [], 'o', color='white', markersize=10)

def init():
    points.set_data([], [])
    return points,

def update(frame):
    t = frame / FPS
    
    # Simple walking motion
    x_offset = 0.2 * np.sin(2 * np.pi * (t / 2))  # Side-to-side sway
    y_offset = 0.1 * np.cos(2 * np.pi * (t / 2))  # Up-and-down bob
    
    # Update positions
    positions = initial_positions.copy()
    
    # Apply offsets for walking
    positions[:, 0] += x_offset
    positions[:, 1] += y_offset
    
    # Swing arms and legs
    arm_angle = 0.5 * np.sin(2 * np.pi * (t + 0.25))
    leg_angle = 0.5 * np.sin(2 * np.pi * t)
    
    # Rotate arms
    positions[2:4, 0] -= 0.1
    positions[2:4, 1] -= 0.1
    for i in range(2):
        angle = arm_angle * (-1 if i % 2 else 1)
        positions[2+i] = rotate_point(positions[2+i], positions[1+i], angle)
        positions[4+i] = rotate_point(positions[4+i], positions[2+i], angle)
    
    # Rotate legs
    positions[9:11, 0] -= 0.1
    positions[9:11, 1] -= 0.7
    for i in range(2):
        angle = leg_angle * (-1 if i % 2 else 1)
        positions[9+i] = rotate_point(positions[9+i], positions[8+i], angle)
        positions[11+i] = rotate_point(positions[11+i], positions[9+i], angle)
    
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

def rotate_point(point, center, angle):
    """
    Rotate a point around a center by a given angle.
    :param point: The point to rotate (x, y).
    :param center: The center of rotation (x, y).
    :param angle: The angle in radians.
    :return: The rotated point (x, y).
    """
    s, c = np.sin(angle), np.cos(angle)
    px, py = point
    cx, cy = center
    return np.array([c * (px - cx) - s * (py - cy) + cx,
                     s * (px - cx) + c * (py - cy) + cy])

# Create animation
ani = animation.FuncAnimation(fig, update, frames=FRAME_COUNT, init_func=init, blit=True, interval=1000/FPS)

plt.show()
