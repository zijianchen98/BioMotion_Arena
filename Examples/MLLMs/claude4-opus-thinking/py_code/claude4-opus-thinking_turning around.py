
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
frames = 100
rotation_speed = 2 * np.pi / frames  # Full rotation over the number of frames

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=8)

# Example positions for the 15 point-lights (e.g., simulating a human shape)
initial_positions = np.array([
    [0, 1],  # Head
    [-0.5, 0.5], [0.5, 0.5],  # Shoulders
    [-0.5, 0], [0.5, 0],      # Arms
    [-0.5, -0.5], [0.5, -0.5],# Hips
    [0, -1],                   # Feet
    [-0.2, -0.75], [0.2, -0.75],  # Lower legs
    [-0.5, -1.2], [0.5, -1.2],  # Feet
    [-0.5, -0.75], [0.5, -0.75],  # Ankles
    [0, -1.5]                  # Extra point for detailed motion
])

# Initialize function for animation
def init():
    points.set_data([], [])
    return points,

# Function to update the animation frames
def update(frame):
    # Calculate rotation angle for current frame
    angle = frame * rotation_speed
    # Create rotation matrix
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                 [np.sin(angle), np.cos(angle)]])
    # Rotate the initial_positions
    rotated_positions = initial_positions.dot(rotation_matrix)
    points.set_data(rotated_positions[:, 0], rotated_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)

# Show the animation
plt.show()
