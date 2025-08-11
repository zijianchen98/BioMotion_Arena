
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants for the animation
num_points = 15  # Total number of point lights
duration = 2000  # Duration of the entire animation in milliseconds
fps = 30  # Frames per second

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.axis('off')  # Turn off the axis

# Initialize point lights
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Define the initial positions of point lights
initial_positions = np.array([
    [0, 1],  # head
    [-0.5, 0.5], [0.5, 0.5],  # shoulders
    [-0.75, 0], [0.75, 0],  # elbows
    [-1, -0.5], [1, -0.5],  # hands
    [-0.5, -1], [0, -1], [0.5, -1],  # hips
    [-0.25, -1.5], [0.25, -1.5]  # feet
])

# Function to update points for each frame
def update(frame):
    # Define waving motion
    wave_amplitude = 0.5 * np.sin(2 * np.pi * (frame / (fps * 2)))
    
    # Alter hand position based on waving motion for realism
    positions = np.copy(initial_positions)
    positions[2, 1] += wave_amplitude  # Right elbow
    positions[6, 1] += wave_amplitude  # Right hand

    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, fps * (duration / 1000)), blit=True)

# Show the animation
plt.show()
