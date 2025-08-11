
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Initialize the point lights
num_lights = 15
lights = np.zeros((num_lights, 2))

# Define the initial positions of the point lights
# These positions are chosen to represent a person lying down
lights[:, 0] = np.array([0.1, 0.3, 0.5, 0.7, 0.9, 0.5, 0.7, 0.9, 0.1, 0.3, 0.5, 0.7, 0.5, 0.7, 0.5])
lights[:, 1] = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.3, 0.3, 0.3, 0.7, 0.7, 0.7, 0.7, 0.1, 0.9, 0.5])

# Define the movement of the point lights
def animate(i):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Move the point lights
    # These movements are chosen to represent a person lying down with a heavy weight
    lights[:, 0] += np.array([0.001, 0.002, 0.003, 0.004, 0.005, -0.003, -0.002, -0.001, 0.002, 0.003, 0.004, 0.005, 0, 0, 0])
    lights[:, 1] += np.array([0, 0, 0, 0, 0, -0.001, -0.002, -0.003, 0.001, 0.002, 0.003, 0.004, 0.005, -0.005, 0])
    
    # Keep the point lights within the boundaries
    lights[:, 0] = np.clip(lights[:, 0], 0, 1)
    lights[:, 1] = np.clip(lights[:, 1], 0, 1)
    
    # Plot the point lights
    ax.scatter(lights[:, 0], lights[:, 1], c='white', s=10)

ani = animation.FuncAnimation(fig, animate, interval=50)

plt.show()
