
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and the radius
num_points = 15
radius = 10

# Create a figure and axis object
fig, ax = plt.subplots()
ax.set_xlim(-radius*2, radius*2)
ax.set_ylim(-radius*2, radius*2)
ax.set_axis_off()

# Initialize the point objects
points, = ax.plot([], [], 'bo')

def init():
    # Initialize the points to a random position
    points.set_data([], [])
    return points,

def update(frame):
    # Compute the new position for each point
    theta = 2 * np.pi * frame / num_points
    x = radius * np.sin(theta)
    y = radius * np.cos(theta)
    
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_points, init_func=init, blit=True)

plt.show()
