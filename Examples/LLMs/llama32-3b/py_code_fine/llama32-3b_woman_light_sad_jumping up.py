
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Define the figure and axis
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Define the number of lights and their positions
num_lights = 15
lights = np.zeros((num_lights, 3))

# Define the positions of the lights
for i in range(num_lights):
    lights[i, 0] = np.random.uniform(-2, 2)
    lights[i, 1] = np.random.uniform(-2, 2)
    lights[i, 2] = np.random.uniform(-2, 2)

# Define the action (jumping up)
action = np.linspace(0, 1, 100)

# Define the positions of the lights for the animation
light_positions = np.zeros((num_lights, len(action), 3))
for i in range(num_lights):
    light_positions[i, :, 0] = lights[i, 0] + action * 2
    light_positions[i, :, 1] = lights[i, 1] + action * 2
    light_positions[i, :, 2] = lights[i, 2] + action * 4

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_zlim(-4, 4)
    ax.set_facecolor('black')
    ax.set_axis_off()
    for j in range(num_lights):
        ax.scatter(light_positions[j, i, 0], light_positions[j, i, 1], light_positions[j, i, 2], s=10, c='white')
    ax.scatter(0, 0, 0, s=50, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(action), interval=50)

# Display the animation
plt.show()
