
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters for the animation
num_points = 15
duration = 2000  # total duration of animation in milliseconds
fps = 30  # frames per second
steps = fps * (duration / 1000)  # total number of frames

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
ax.axis('off')  # Turn off the axis

# Initialize the pointlights
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Forward roll movement trajectory
def forward_roll(t):
    # Define the motion as a series of points in a forward roll
    # Adjust these arrays for more accurate movement simulation
    x = np.sin(t) * np.cos(t) * 2  # Adjust this for more accurate rolling path
    y = -t + 5 * np.sin(t)  # Motion in the y-axis to simulate movement
    return x, y

# Function to update the frame
def update(frame):
    t = frame / fps * np.pi * 2  # Time variable
    x, y = forward_roll(t)
    
    # Set the x, y coordinates for the points
    points.set_data(x[:num_points], y[:num_points])
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=steps, init_func=init, blit=True, repeat=True)

# Show the animation
plt.show()
