
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of point-lights
num_lights = 15

# Figure and axis setup
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')

# Points initialization
points, = ax.plot([], [], 'wo', markersize=10)  # white points

# Function to initialize the plot
def init():
    points.set_data([], [])
    return points,

# Function to update the points for each frame
def update(frame):
    # Calculate the position of each point-light with a sad walking configuration
    x = np.array([0, -0.5, 0.5, -1.0, 1.0, -0.5, 0.5, 0, 0])
    y = np.array([-3, -2.5, -2.5, -1.5, -1.5, -1.0, -1.0, -4, -4.5])
    
    # Create a walking effect
    y += 0.1 * np.sin(np.linspace(0, 2 * np.pi, num_lights) + frame / 10)

    # Update point positions
    points.set_data(x, y)
    return points,

# Animation setup
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init,
                    blit=True, interval=50)

# Show the animation
plt.show()
