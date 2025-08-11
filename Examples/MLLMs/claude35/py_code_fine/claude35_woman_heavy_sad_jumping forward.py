
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point lights
num_points = 15

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=10)  # White points

# Initial position of points (representing sad woman)
# Adjust these to correspond to your desired representation.
initial_positions = np.array([
    [0, 0.5],  # Head
    [-0.1, 0.3], [0.1, 0.3],  # Shoulders
    [-0.3, 0.2], [0.3, 0.2],  # Arms
    [-0.2, 0.0], [0.2, 0.0],  # Hands
    [-0.2, -0.5], [0.2, -0.5],  # Hips
    [-0.5, -1.0], [0.5, -1.0],  # Knees
    [-0.5, -1.5], [0.5, -1.5],  # Feet
    [-0.1, -1.0], [0.1, -1.0],  # Center of mass
    [0, -0.7],  # Stable point (like a weight hanging down)
])

# Function to update points' position for each frame
def update(frame):
    # Update position to simulate jumping forward
    t = frame / 40  # Normalize time
    jump_height = 0.8 * np.sin(np.pi * t)  # Jump arc
    forward_distance = t - 1  # Forward motion

    # Calculate new positions
    new_positions = initial_positions.copy()
    new_positions[:, 0] += forward_distance  # Move forward
    new_positions[:, 1] += jump_height  # Move up/down

    # Update points
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
