
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Total number of points
num_points = 15

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Define the initial positions of the point-lights (a simple render of a human shape)
# Assuming a simple representation of joint positions
initial_positions = np.array([
    [0, 1.5],   # Head
    [0, 1.0],   # Neck
    [-0.5, 0.5], [0.5, 0.5],  # Shoulders
    [-0.5, 0],   [0.5, 0],    # Elbows
    [-0.75, -1], [0.75, -1],  # Hands
    [-0.5, -1.5],   # Hip
    [0.5, -1.5],    # Hip
    [-0.3, -2.2], [0.3, -2.2],  # Knees
    [-0.5, -2.8], [0.5, -2.8]   # Feet
])

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Function to update each frame
def update(frame):
    # Simulate a rotation for the turning action
    angle = frame * np.pi / 40  # Adjust for smoothness
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], 
                                 [np.sin(angle),  np.cos(angle)]])
    
    # Rotate the points
    rotated_positions = initial_positions.dot(rotation_matrix)
    
    # Update the points data
    points.set_data(rotated_positions[:, 0], rotated_positions[:, 1])
    return points,

# Create the animation
anim = animation.FuncAnimation(fig, update, frames=80, init_func=init, blit=True, interval=100)

# Show the animation
plt.show()
