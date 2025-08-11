
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters
num_points = 15
frames = 60
frame_duration = 50  # milliseconds

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the points
points, = ax.plot([], [], 'o', color='white')

def init():
    points.set_data([], [])
    return points,

def update(frame):
    # Clear previous positions
    points.set_data([], [])
    
    # Calculate new positions based on running motion
    x = np.linspace(-10, 10, num_points)
    y = np.sin(x + frame / 10.0) * 2
    
    # Add some variation for realism
    y += np.random.normal(0, 0.5, num_points)
    
    points.set_data(x, y)
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, interval=frame_duration, init_func=init)

plt.show()
