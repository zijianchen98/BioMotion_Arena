
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Number of points representing the happy character
num_points = 15
points = np.zeros((num_points, 2))

# Define initial positions of point-lights (y-axis positions)
initial_positions = np.array([
    0.7, 0.9, 1.0,  # Head and upper body
    0.5, 0.6, 0.75, 0.8,  # Mid body
    0.0, -0.1,  # Lower body
    -0.5, -0.6, -0.75, -0.8,  # Legs
    -0.9, -1.0, -0.8, -0.9,  # Feet
])

# Assign initial x and y coordinates
points[:, 0] = np.linspace(-0.1, 0.1, num_points)
points[:, 1] = initial_positions

# Create a scatter plot for the point lights
scatter = ax.scatter(points[:, 0], points[:, 1], color='white')

# Define the jumping motion
def update(frame):
    # Calculate vertical jump motion using a sine function
    jump_height = 0.2 * np.sin(np.pi * frame / 15)
    
    # Update Y position for jumping
    new_y_positions = initial_positions + jump_height

    # Update points and scatter plot
    points[:, 1] = new_y_positions
    scatter.set_offsets(points)
    return scatter,

# Create the animation
ani = FuncAnimation(fig, update, frames=30, interval=100, blit=True)

# Display the animation
plt.show()
