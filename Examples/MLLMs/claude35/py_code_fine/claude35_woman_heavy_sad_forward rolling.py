
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define number of point lights
num_points = 15

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-15, 15)
ax.set_ylim(-10, 20)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Initial positions for the point lights
# A simple configuration resembling a sad woman rolling
initial_positions = np.array([[-2, 2], [0, 5], [2, 2], [0, 0], [-1, -1], [1, -1], [-3, -3],
                             [3, -3], [-4, -4], [4, -4], [-2, -6], [2, -6], [0, -8], [0, -10],
                             [0, -12]])

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Function to update the points for each frame
def update(frame):
    # Simulate forward rolling motion; modify y values to create a rolling effect
    y_offset = -0.2 * frame
    new_positions = initial_positions + np.array([0, y_offset])
    
    # Create a smooth rolling motion
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create an animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init, blit=True, interval=50)

# Show the animation
plt.show()
