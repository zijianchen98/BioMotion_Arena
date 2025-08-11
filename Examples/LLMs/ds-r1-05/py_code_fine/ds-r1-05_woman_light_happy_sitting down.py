
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib

# Set the background to black and figure size
matplotlib.rcParams['axes.facecolor'] = 'black'
fig, ax = plt.subplots(figsize=(7, 7))
ax.set_xlim(-1, 1)
ax.set_ylim(-0.5, 2)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])

# Initialize standing pose positions
standing_pose = [
    [0, 1.8],    # head (0)
    [0, 1.7],    # neck (1)
    [-0.4, 1.6], # left shoulder (2)
    [0.4, 1.6],  # right shoulder (3)
    [-0.5, 1.3], # left elbow (4)
    [0.5, 1.3],  # right elbow (5)
    [-0.6, 0.9], # left wrist (6)
    [0.6, 0.9],  # right wrist (7)
    [0, 1.0],    # mid-torso (hip center) (8)
    [-0.2, 1.0], # left hip (9)
    [0.2, 1.0],  # right hip (10)
    [-0.25, 0.5],# left knee (11)
    [0.25, 0.5], # right knee (12)
    [-0.25, 0.1],# left ankle (13)
    [0.25, 0.1]  # right ankle (14)
]

# Create a list for the point markers
points = [ax.plot([], [], 'o', color='white', markersize=8)[0] for _ in range(15)]

def init():
    for point in points:
        point.set_data([], [])
    return points

def update(frame):
    t = frame / 50  # 50 frames for 2 seconds
    current_points = []
    
    # Calculate positions for upper body (points 0 to 7)
    for i in range(8):
        x0, y0 = standing_pose[i]
        theta = np.radians(15 * t)  # convert degrees to radians
        # Apply translation and rotation
        x = 0.1 * t + x0 * np.cos(theta) - (y0 - 1.0) * np.sin(theta)
        y = 1.0 - 0.4 * t + x0 * np.sin(theta) + (y0 - 1.0) * np.cos(theta)
        current_points.append((x, y))
    
    # Calculate positions for mid-torso and hips (points 8, 9, 10)
    current_points.append((0.1 * t, 1.0 - 0.4 * t))  # mid-torso (8)
    current_points.append((-0.2 + 0.1 * t, 1.0 - 0.4 * t))  # left hip (9)
    current_points.append((0.2 + 0.1 * t, 1.0 - 0.4 * t))  # right hip (10)
    
    # Calculate positions for knees and ankles (points 11 to 14)
    current_points.append((-0.25 + 0.15 * t, 0.5 - 0.2 * t))  # left knee (11)
    current_points.append((0.25 - 0.15 * t, 0.5 - 0.2 * t))  # right knee (12)
    current_points.append((-0.25, 0.1))  # left ankle (13)
    current_points.append((0.25, 0.1))  # right ankle (14)
    
    # Update each point's position
    for i, point in enumerate(points):
        x, y = current_points[i]
        point.set_data([x], [y])
    
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=50, init_func=init, blit=True, interval=40)  # 25 fps for 2 seconds

plt.show()
