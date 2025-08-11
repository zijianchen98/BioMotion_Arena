
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters for the animation
num_points = 15
frames = 100
speed = 0.1

# Create a figure and axis for the plot
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the positions of the points
points, = ax.plot([], [], 'o', color='white')

def init():
    points.set_data([], [])
    return points,

def update(frame):
    # Clear previous positions
    points.set_data([], [])
    
    # Calculate new positions for each point
    x = np.linspace(-10, 10, num_points)
    y = np.sin(2 * np.pi * (x + frame * speed))
    
    # Update the positions of the points
    points.set_data(x, y)
    
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)

plt.show()
