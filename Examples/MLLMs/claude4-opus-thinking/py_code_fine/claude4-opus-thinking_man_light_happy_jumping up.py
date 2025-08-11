
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Define the number of point-lights
num_points = 15
frames = 60  # Total frames for the animation

# Define point-light positions (this can be adjusted for realistic representation)
initial_positions = np.array([
    [0, 1.5],  # head
    [-0.5, 1], [0.5, 1],  # shoulders
    [-0.5, 0.5], [0.5, 0.5],  # elbows
    [-0.3, 0], [0.3, 0],  # hands
    [0, 0],  # center of mass
    [-0.4, -0.5], [0.4, -0.5],  # knees
    [-0.2, -1], [0.2, -1],  # feet
])

# Setup the figure
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Initialize the plot
def init():
    points.set_data([], [])
    return points,

# Update function for animation
def update(frame):
    jump_height = 2 * np.sin(np.pi * frame / (frames / 2))  # Simulate jump
    positions = initial_positions + np.array([[0, jump_height]]).repeat(num_points, axis=0)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, repeat=True)

# Show the animation
plt.show()
