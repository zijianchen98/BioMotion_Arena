
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up constants
num_points = 15  # Total number of point-lights
duration = 100  # Duration of one full animation loop in milliseconds
frames = 60  # Total number of frames in the animation

# Initial positions of the point-lights
# Define the structure of a happy man using 15 points
initial_positions = np.array([
    [0, 2],     # Head
    [-1, 1],    [1, 1],  # Shoulders
    [-1, 0],    [1, 0],   # Elbows
    [-1, -1],   [1, -1],  # Hands
    [0, -1],    # Waist
    [0, -2],    # Bottom
    [-0.5, -3], [0.5, -3],  # Legs
    [-0.5, -4], [0.5, -4],  # Foot position
    [-0.5, -2], [0.5, -2]    # Feet
])

# Animation function
def update(frame):
    plt.clf()  # Clear the current figure
    plt.xlim(-5, 5)  # Set x limits
    plt.ylim(-5, 5)  # Set y limits
    plt.axis('off')  # Hide axes

    # Calculate current positions for sitting down animation (smooth transition)
    displacement = np.sin(np.linspace(0, np.pi, 10)) * np.array([0, 0, 0, 0, 0.5, 0, 0, 0.5, 0, 0])
    current_positions = initial_positions.copy()
    current_positions[:, 1] -= displacement[frame % len(displacement)]

    # Plot each point-light
    plt.scatter(current_positions[:, 0], current_positions[:, 1], color='white')

# Create the figure for animation
fig = plt.figure()
ani = FuncAnimation(fig, update, frames=frames, interval=duration // frames, repeat=True)

# Set a black background
fig.patch.set_facecolor('black')

plt.show()
