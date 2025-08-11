
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point lights
num_points = 15

# Setup figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-1, 10)
ax.axis('off')  # Remove axes

# Initialize the positions of the point lights
# Define a jumping trajectory for a sad man with 15 points
initial_positions = np.array([
    [0, 0],   # Head
    [-0.5, 1], [0.5, 1],  # Shoulders
    [-1, 2], [0, 2], [1, 2],  # Arms
    [-1, 3], [0, 3], [1, 3],  # Elbows
    [-0.5, 4], [0, 4], [0.5, 4],  # Waist
    [-0.5, 5], [0, 5], [0.5, 5],  # Upper Legs
    [-0.5, 6], [0, 6], [0.5, 6],  # Lower Legs
])

# Create scatter plot points
points = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

# Function to update the animation
def update(frame):
    # Define the jumping dynamic
    jump_height = np.sin(frame / 10.0) * 2  # Create a jumping effect
    new_positions = initial_positions + [0, jump_height]

    # Update the points position
    points.set_offsets(new_positions)
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

# Show the animation
plt.show()
