
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define parameters for the animation
num_points = 15
frames = 100
walking_speed = 0.05  # Speed of the walking animation
weight_offset = 0.4    # Offset downwards for 'heavy weight' representation

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Initialize position of points (representing joint locations)
# Define initial positions in a 2D structure
initial_positions = np.array([
    [0, 1.8],    # Head
    [0, 1.6],    # Neck
    [-0.2, 1.5], # Left shoulder
    [0.2, 1.5],  # Right shoulder
    [-0.2, 1.3], # Left elbow
    [0.2, 1.3],  # Right elbow
    [-0.2, 1.1], # Left wrist
    [0.2, 1.1],  # Right wrist
    [0, 1.0],    # Torso
    [-0.15, 0.8],# Left hip
    [0.15, 0.8], # Right hip
    [-0.1, 0.5], # Left knee
    [0.1, 0.5],  # Right knee
    [-0.15, 0.2],# Left ankle
    [0.15, 0.2], # Right ankle
    [0, 0.6]     # Weight held
])

# Animation update function
def update(frame):
    # Simulate walking motion by altering the y-coordinates over time
    walking_angle = frame * walking_speed
    movement = np.sin(walking_angle) * 0.1  # Y-axis movement
    weight_movement = -0.05 * np.sin(walking_angle)  # Weight bobbing effect

    # Update positions to simulate walking
    positions = initial_positions.copy()
    
    # Apply walking movement
    positions[:, 1] += movement
    positions[14, 1] += weight_movement + weight_offset  # Adjust weight position

    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50)
plt.show()
