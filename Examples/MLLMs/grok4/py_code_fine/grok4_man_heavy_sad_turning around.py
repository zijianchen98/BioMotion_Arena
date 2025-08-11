
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15  # Number of point-lights
frames = 60  # Number of frames in the animation

# Function to generate positions for the point-lights
def generate_positions(angle):
    # Basic structure for a sad man moving downwards and turning
    # Define the initial position of the points (15 points forming a rough body shape)
    positions = np.array([
        [0, 2],  # Head
        [-0.5, 1.5], [0.5, 1.5],  # Shoulders
        [-0.5, 1], [0.5, 1],  # Elbows
        [0, 0],  # Center of body
        [-0.5, -1], [0.5, -1],  # Knees
        [-0.75, -2], [0.75, -2],  # Feet
        [-0.5, -3], [0.5, -3],  # Lower body
        [-1.2, -2.5], [1.2, -2.5],  # Additional points for a more coherent motion
        [-0.8, -2.5], [0.8, -2.5]
    ])
    
    # Apply rotation to simulate turning around
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])

    return positions @ rotation_matrix.T

# Setup the figure
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-4, 3)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Update function for animation
def update(frame):
    angle = np.pi * frame / frames  # Calculate the rotation angle
    pos = generate_positions(angle)
    points.set_data(pos[:, 0], pos[:, 1])
    return points,

# Creating the animation
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=1000/30)

# Display the animation
plt.axis('off')  # Turn off the axis
plt.show()
