
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Define the parameters
num_lights = 15
light_positions = np.random.rand(num_lights, 3) * 10 - 5  # Random positions between -5 and 5
light_sizes = np.random.rand(num_lights) * 0.1 + 0.05  # Random sizes between 0.05 and 0.15
action = 'jumping'

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the background color to black
ax.set_facecolor('black')

# Initialize the lights
lights = []
for i in range(num_lights):
    light = ax.scatter(light_positions[i, 0], light_positions[i, 1], light_positions[i, 2], s=light_sizes[i], c='white', marker='o')
    lights.append(light)

# Define the animation function
def animate(i):
    # Calculate the new positions of the lights
    if action == 'jumping':
        # Calculate the new positions of the lights based on the action
        light_positions[:, 0] = light_positions[:, 0] + np.sin(i / 10) * 0.1
        light_positions[:, 1] = light_positions[:, 1] + np.sin(i / 10) * 0.1
        light_positions[:, 2] = light_positions[:, 2] + np.sin(i / 10) * 0.5
    else:
        # If the action is not 'jumping', keep the positions the same
        pass

    # Update the lights
    for light in lights:
        light.set_offsets(light_positions[i, :])
        light.set_sizes(light_sizes[i])

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

# Show the animation
plt.show()
