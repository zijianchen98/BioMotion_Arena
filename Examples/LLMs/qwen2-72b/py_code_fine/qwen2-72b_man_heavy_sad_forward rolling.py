
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')

# Create 15 point lights
num_points = 15
points, = ax.plot([], [], 'o', color='white')

def init():
    points.set_data([], [])
    return points,

def animate(i):
    # Generate new positions for the points
    x = np.random.uniform(0, 10, num_points)
    y = np.random.uniform(0, 10, num_points)
    
    # Update the data for the points
    points.set_data(x, y)
    
    return points,

# Create the animation
ani = FuncAnimation(fig, animate, frames=200,
                    init_func=init, blit=True)

plt.show()
