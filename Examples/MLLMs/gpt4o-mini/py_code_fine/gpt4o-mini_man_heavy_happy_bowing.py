
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants for the animation
num_points = 15
duration = 10  # seconds
frames = 60 * duration  # 60 FPS
time = np.linspace(0, duration, frames)

# Define the initial positions of the point lights (15 points)
# Assume the arrangement is similar to a human body and bowing motion
points_initial = np.array([
    [0, 5],   # Head
    [-1, 4],  # Left shoulder
    [1, 4],   # Right shoulder
    [-1, 3],  # Left elbow
    [1, 3],   # Right elbow
    [-1, 2],  # Left wrist
    [1, 2],   # Right wrist
    [0, 1],   # Center of mass
    [-1, 0],  # Left hip
    [1, 0],   # Right hip
    [-1, -1], # Left knee
    [1, -1],  # Right knee
    [-0.5, -2], # Left foot
    [0.5, -2],  # Right foot
    [0, 3],   # Upper back
    [0, 2]    # Lower back
])

# Define a bowing motion
def bowing_motion(t):
    angle = np.pi * (0.5 + 0.5 * np.sin(2 * np.pi * t / duration))  # Bowing Action
    # Apply transformations to simulate a bowing action
    points_bowing = points_initial.copy()
    
    # Apply a downward motion for bowing
    for i in range(points_bowing.shape[0]):
        points_bowing[i, 1] -= angle * 2  # Adjust the y position
    
    return points_bowing

# Create animation function
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 6)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

def init():
    points.set_data([], [])
    return points,

def update(frame):
    current_points = bowing_motion(time[frame])
    points.set_data(current_points[:, 0], current_points[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)
plt.show()
