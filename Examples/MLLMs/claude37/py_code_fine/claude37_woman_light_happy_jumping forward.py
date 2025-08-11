
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
frames = 100

# Initial points representing the position of the lights
initial_positions = np.array([
    [0, 0],  # Center of gravity (pelvis)
    [0, 1],  # Head
    [-0.5, 0.5], [0.5, 0.5],  # Shoulders
    [-0.5, 0], [0.5, 0],  # Hips
    [-0.75, 0.5], [0.75, 0.5],  # Elbows
    [-0.75, 0], [0.75, 0],  # Knees
    [-0.5, -0.5], [0.5, -0.5],  # Hands
    [0, -1]  # Feet
]) * 0.1

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Update function for animation
def update(frame):
    # Calculate new positions for the lights
    jump_height = np.sin(frame / 10) * 0.5  # Jump effect
    forward_distance = frame / 50.0          # Forward movement

    # New positions based on the uniform motion model
    new_positions = initial_positions.copy()
    new_positions[:, 1] += jump_height        # Add vertical jump
    new_positions[:, 0] += forward_distance     # Add forward movement

    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

# Display the animation
plt.show()
