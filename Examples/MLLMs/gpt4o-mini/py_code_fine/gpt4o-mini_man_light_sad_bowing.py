
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of points
num_points = 15

# Define initial positions of the point lights for a "sadman" bowing
# The points represent key joints in the body
initial_positions = np.array([
    [0, 2],  # Head
    [-1, 1],  # Left Shoulder
    [1, 1],   # Right Shoulder
    [-1, 0],  # Left Elbow
    [1, 0],   # Right Elbow
    [-1, -1], # Left Hand
    [1, -1],  # Right Hand
    [0, 1],   # Neck
    [0, 0],   # Torso
    [0, -2],  # Pelvis
    [-0.5, -2], # Left Knee
    [0.5, -2],  # Right Knee
    [-0.5, -3], # Left Foot
    [0.5, -3],  # Right Foot
])

# Define bowing motion parameters
def bowing_motion(frame):
    # Define the amount of bowing (Y position)
    bow_amount = np.sin(frame / 10.0) * 0.5
    
    # Update Y coordinates for a bowing effect
    positions = initial_positions.copy()
    positions[:, 1] -= bow_amount
    
    return positions

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 2)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Create scatter plot
points, = ax.plot([], [], 'wo', ms=15)

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Animation update function
def update(frame):
    positions = bowing_motion(frame)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init, blit=True, interval=50)

# Display the animation
plt.show()
