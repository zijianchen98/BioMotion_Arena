
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Define the number of lights and their positions
num_lights = 15
light_positions = np.random.rand(num_lights, 3) * 2 - 1  # Random positions between -1 and 1

# Define the animation function
def animate(i):
    # Clear the axes
    ax.clear()

    # Draw a black background
    ax.set_facecolor('black')

    # Calculate the light positions for the current frame
    light_positions[:, 0] += 0.05 * np.sin(i / 10)
    light_positions[:, 1] += 0.05 * np.cos(i / 10)
    light_positions[:, 2] += 0.05 * np.sin(i / 20)

    # Plot the lights
    for light in light_positions:
        ax.scatter(light[0], light[1], light[2], s=100, color='white')

# Create the figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(1000), interval=50)

# Show the animation
plt.show()
