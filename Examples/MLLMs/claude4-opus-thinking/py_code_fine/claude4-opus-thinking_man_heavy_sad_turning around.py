
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black') # Set background to black
ax.set_xticks([])
ax.set_yticks([])

# Define the number of points
num_points = 15

# Create initial positions for the point-lights
initial_positions = np.array([
    [0, 5],   # Head
    [-2, 3],  # Left shoulder
    [2, 3],   # Right shoulder
    [-3, 1],  # Left elbow
    [3, 1],   # Right elbow
    [-3, -2], # Left hand
    [3, -2],  # Right hand
    [-1, -3], # Left hip
    [1, -3],  # Right hip
    [-2.5, -5], # Left knee
    [2.5, -5],  # Right knee
    [-2.5, -8], # Left foot
    [2.5, -8],  # Right foot
    [0, 0],     # Weight position
])

# Initialize the points
point_lights, = ax.plot(initial_positions[:, 0], initial_positions[:, 1], 'o', color='white')

# Function to update points
def update(frame):
    # Update the positions to simulate motion
    theta = np.radians(frame) # Angle of rotation
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                                [np.sin(theta), np.cos(theta)]])
    
    # Rotate all points around the weight at (0, 0)
    rotated_positions = initial_positions @ rotation_matrix.T
    
    # Update the point-lights
    point_lights.set_data(rotated_positions[:, 0], rotated_positions[:, 1])
    return point_lights,

# Create an animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 5), blit=True, interval=50)

# Display the animation
plt.show()
