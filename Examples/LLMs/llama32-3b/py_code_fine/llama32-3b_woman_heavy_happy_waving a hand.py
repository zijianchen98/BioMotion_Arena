
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Define the number of lights and their positions
num_lights = 15
light_positions = np.random.rand(num_lights, 3) * 2 - 1  # Random positions between -1 and 1

# Define the action (waving a hand)
def wave_hand(t):
    # Define the movement of each light
    movement = np.sin(t * 2 * np.pi / 10) * 0.1  # Move the light up and down

    # Update the light positions
    light_positions[:, 1] += movement  # Move the light up and down

    return light_positions

# Create a new figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the background color to black
ax.set_facecolor('black')

# Create the point lights
lights = []
for i, pos in enumerate(light_positions):
    light = ax.plot3D(pos[0], pos[1], pos[2], 'w-', linewidth=0.5, markersize=10)
    lights.append(light)

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_facecolor('black')
    light_positions = wave_hand(i)
    for light, pos in zip(lights, light_positions):
        light.set_data([pos[0]], [pos[1]])
        light.set_3d_properties([pos[2]])
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

# Show the animation
plt.show()
