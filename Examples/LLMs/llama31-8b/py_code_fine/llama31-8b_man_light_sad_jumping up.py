
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Define the figure and axis
fig, ax = plt.subplots()

# Define the background color
ax.set_facecolor('black')

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
light_positions = np.zeros((num_lights, 2))
light_positions[:, 0] = np.linspace(-1, 1, num_lights)
light_positions[:, 1] = np.linspace(-1, 1, num_lights)

# Define the light colors
light_colors = np.ones((num_lights, 3)) * [1, 1, 1]

# Create the point lights
lights = []
for i in range(num_lights):
    light = patches.Circle(light_positions[i], 0.05, edgecolor='white', facecolor='white')
    ax.add_patch(light)
    lights.append(light)

# Define the sadman's movement
def jumping_up(t):
    # Define the movement of the point lights
    for i in range(num_lights):
        # Define the movement of each point light
        if i < 5:
            light_positions[i, 0] = np.sin(2 * np.pi * 0.5 * t)
            light_positions[i, 1] = np.cos(2 * np.pi * 0.5 * t) * 0.5
        elif i < 10:
            light_positions[i, 0] = np.sin(2 * np.pi * 0.5 * t + np.pi)
            light_positions[i, 1] = np.cos(2 * np.pi * 0.5 * t) * 0.5
        else:
            light_positions[i, 0] = np.sin(2 * np.pi * 0.5 * t)
            light_positions[i, 1] = np.cos(2 * np.pi * 0.5 * t) * 0.5 + 0.5

    # Update the positions of the point lights
    for i in range(num_lights):
        lights[i].center = light_positions[i]

# Animate the point lights
ani = animation.FuncAnimation(fig, jumping_up, frames=np.linspace(0, 10, 100), interval=50)

# Show the animation
plt.show()
