
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_points = 15
duration = 5  # seconds
fps = 30
total_frames = duration * fps

# Initialize positions of the point-lights (15 points)
# For demonstration, we will create a simplistic representation
# of points in a standing bowing position. Adjust to your actual bowing positions.
initial_positions = np.array([
    [0, 4],  # Head
    [-1, 3], [1, 3],  # Shoulders
    [-2, 2], [0, 2], [2, 2],  # Elbows
    [-2, 1], [0, 1], [2, 1],  # Wrists
    [-1, 0], [0, 0], [1, 0],  # Hips
    [0, -1]  # Feet
])

# Bowing motion (simplified model)
def bowing_motion(frame):
    # Create a simple bowing effect by moving points down and inward
    # Adjust y-coordinate to simulate the bowing
    movement = np.clip(np.linspace(0, -3, total_frames)[frame], -3, None)
    pos = initial_positions.copy()
    pos[:, 1] += movement
    return pos

# Setup the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_facecolor('black')
ax.axis('off')

# Create the point-lights
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Animation update function
def update(frame):
    positions = bowing_motion(frame)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=total_frames, blit=True, interval=1000/fps)

# Show the animation
plt.show()
