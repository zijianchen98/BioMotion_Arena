
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the subject and action parameters
subject = 'happyman'
action = 'lying down'
weight = 'heavy'

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim((-50, 120)
ax.set_ylim((-50, 120))
ax.set_aspect('equal')
ax.axis('off')

# Define the points for the subject
points = np.array([
    [0, 60],   # Head
    [15, 75], # Chest
    [30, 80], # Waist
    [45, 80], # Hip
    [60, 70], # Knee
    [70, 60], # Ankle
    [80, 50] # Foot
])

# Define the number of frames and frame interval
num_frames = 15
frame_interval = 200  # milliseconds

# Initialize the animation
def init():
    ax.set_facecolor('#000000')  # Set background color to black
    return []

# Define the update function for each frame
def update(frame):
    ax.clear()  # Clear previous frame
    ax.set_facecolor('#000000')  # Set background color to black
    
    # Calculate the position of each point based on the action
    if action == 'lying down':
        angles = np.linspace((0, np.pi, num_points)
        positions = points * np.array([np.cos(angles), np.sin(angles)]).T
    
    # Plot each point
    for i, pos in enumerate(positions):
        circle = plt.Circle(pos, radius=5, color='w', fill=True)
        ax.add_patch(circle)
    
    return []

# Create the animation
ani = FuncAnimation(fig, update, init_func=init, frames=num_frames, interval=frame_interval)

plt.show()

