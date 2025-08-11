
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Define the number of lights
num_lights = 15

# Define the figure size
fig = plt.figure(figsize=(8, 8))

# Create a 3D subplot
ax = fig.add_subplot(111, projection='3d')

# Define the light positions
lights = np.zeros((num_lights, 3))
for i in range(num_lights):
    lights[i, 0] = np.random.uniform(-2, 2)
    lights[i, 1] = np.random.uniform(-2, 2)
    lights[i, 2] = np.random.uniform(0, 4)

# Define the animation function
def animate(i):
    # Clear the previous frame
    ax.clear()

    # Set the background color to black
    ax.set_facecolor('black')

    # Calculate the light positions for the current frame
    for j in range(num_lights):
        x = lights[j, 0] + np.sin(i/10.0 + j/num_lights) * 0.5
        y = lights[j, 1] + np.sin(i/10.0 + j/num_lights + np.pi/2) * 0.5
        z = lights[j, 2] + np.sin(i/10.0 + j/num_lights + np.pi) * 0.5

        # Create a 3D point light
        ax.scatter(x, y, z, s=10, c='white', marker='o')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=20, repeat=False)

# Show the animation
plt.show()
