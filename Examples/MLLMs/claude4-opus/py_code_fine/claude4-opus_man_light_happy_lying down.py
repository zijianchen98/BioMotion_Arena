
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Setup for the figure
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Define number of point lights and their initial positions
num_points = 15
points = np.zeros((num_points, 2))

# Initial configuration of the point-lights representing joints (lying down)
# Defining point-light positions for the "lying down" action
# (x, y) coordinates
points[:, 0] = np.array([0, -0.5, 0.5, -0.5, 0.5, -0.75, 0.75, -1, 1, 
                         -0.25, 0.25, 0, -0.1, 0.1, -0.8, 0.8])  # x-coordinates
points[:, 1] = np.array([-0.5, -0.8, -0.8, -1.2, -1.2, -1, -1, 
                         -1.2, -1.1, -0.9, -0.9, -0.6, -0.3, -0.3, -0.4])  # y-coordinates

# Create point lights
light_points, = ax.plot([], [], 'o', color='white', markersize=10)

# Animation function
def init():
    light_points.set_data([], [])
    return light_points,

def animate(frame):
    # Motion parameters for smooth animation
    amplitude = 0.05 * np.sin(frame / 10)
    # Adjusting y-coordinates to create a natural movement
    new_y = points[:, 1] + amplitude
    light_points.set_data(points[:, 0], new_y)
    return light_points,

# Call the animator
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=np.arange(0, 200), interval=50, blit=True)

# Show the animation
plt.show()
