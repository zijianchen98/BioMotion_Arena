
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
num_points = 15

# Create an initial position for the point lights
initial_positions = np.array([
    [0, 0],  # Center point (pelvis)
    [-0.1, 0.5], [0.1, 0.5],  # Shoulders
    [-0.2, 0.3], [0.2, 0.3],  # Elbows
    [-0.2, 0.1], [0.2, 0.1],  # Hands
    [-0.1, -0.2], [0.1, -0.2], # Knees
    [-0.1, -0.5], [0.1, -0.5], # Ankle
    [-0.3, 0.4], [0.3, 0.4],   # Hips
    [-0.2, 0.6], [0.2, 0.6],   # Head
])

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Function to animate
def update(frame):
    angle = np.radians(frame * 2)  # Adjust rotation speed
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                 [np.sin(angle), np.cos(angle)]])
    
    # Rotate each point around the center (0, 0)
    rotated_positions = initial_positions @ rotation_matrix
    
    points.set_data(rotated_positions[:, 0], rotated_positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 180, 1),
                              init_func=init, blit=True, interval=30)

plt.show()
