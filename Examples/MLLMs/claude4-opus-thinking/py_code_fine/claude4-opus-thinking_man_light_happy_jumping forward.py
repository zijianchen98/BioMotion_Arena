
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-5, 15)
ax.set_facecolor('black')
ax.axis('off')

# Create point lights (15 points)
num_points = 15
points, = ax.plot([], [], 'o', color='white')

# Define initial positions
def init():
    points.set_data([], [])
    return points,

# Define the jumping motion
def update(frame):
    # Vertical and horizontal oscillation
    jump_height = np.sin(frame / 10) * 2
    forward_movement = frame / 10
    
    # Calculate new positions for the points
    # Example data for a jumping man's body parts
    shoulder_angle = forward_movement * 0.5
    positions = [
        (0, 0 + jump_height),   # center point (torso)
        (1, 2 + jump_height),   # right shoulder
        (-1, 2 + jump_height),  # left shoulder
        (1, 1 + jump_height),   # right elbow
        (-1, 1 + jump_height),  # left elbow
        (1, 0.5 + jump_height), # right hand
        (-1, 0.5 + jump_height),# left hand
        (1, -1 + jump_height),  # right hip
        (-1, -1 + jump_height), # left hip
        (1, -2 + jump_height),  # right knee
        (-1, -2 + jump_height), # left knee
        (1, -3 + jump_height),  # right foot
        (-1, -3 + jump_height), # left foot
        (2, 0 + jump_height),   # right shoulder second point
        (-2, 0 + jump_height),  # left shoulder second point
        (0, 4 + jump_height)    # head
    ]
    
    # Split position into x and y arrays
    x, y = zip(*positions)
    
    # Update points position
    points.set_data(x, y)
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init, blit=True)

# Show animation
plt.show()
