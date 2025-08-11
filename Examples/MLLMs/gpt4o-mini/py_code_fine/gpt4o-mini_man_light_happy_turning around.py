
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to generate the coordinates for the 15 point-lights
def generate_positions(t):
    # Define the basic positions of the point-lights relative to a center
    positions = np.array([
        [0, 2],  # head
        [-1, 1], [0, 1], [1, 1],  # shoulders
        [-1, 0], [0, 0], [1, 0],  # upper body
        [-1, -1], [0, -1], [1, -1],  # lower body
        [0, -2],  # feet
    ])
    
    # Create a rotation matrix for the turning action
    angle = t * np.pi / 30  # Control the speed of rotation
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                 [np.sin(angle),  np.cos(angle)]])
    
    # Rotate the positions
    rotated_positions = positions @ rotation_matrix
    return rotated_positions

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Animation update function
def update(frame):
    pos = generate_positions(frame)
    points.set_data(pos[:, 0], pos[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360), init_func=init, blit=True, interval=1000/60)

# Display the animation
plt.show()
