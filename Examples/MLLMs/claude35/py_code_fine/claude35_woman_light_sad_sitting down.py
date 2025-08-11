
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
frames = 100

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')

# Initialize point-lights
points, = ax.plot([], [], 'o', color='white')

# Define the initial position of the lights
initial_positions = np.array([
    [0, 0.8],   # Head
    [-0.2, 0.5], [0.2, 0.5],  # Shoulders
    [-0.4, 0.3], [0.4, 0.3],  # Elbows
    [-0.5, 0],   [0.5, 0],   # Hands
    [-0.3, -0.5], [0.3, -0.5], # Knees
    [-0.2, -1],  [0.2, -1],   # Feet
])

# Create a sitting down motion over frames
def update(frame):
    # Simulate a simple sitting down motion
    sitting_positions = initial_positions.copy()
    sitting_positions += np.array([0, -0.01 * frame])  # Move downwards
    
    points.set_data(sitting_positions[:, 0], sitting_positions[:, 1])
    return points,

# Creating the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

# Show the animation
plt.show()
