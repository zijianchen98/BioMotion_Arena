
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Set up the figure and axis
fig, ax = plt.subplots()

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
x_coords = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
y_coords = np.array([0, 0.3, 0.6, 0.3, -0.3, -0.6, -0.3, 0, 0.3, 0.6, 0.3, -0.3, -0.6, -0.3, 0])

# Define the light colors
light_colors = ['w'] * num_lights

# Define the background color
background_color = 'k'

# Create the point lights
lights = []
for i in range(num_lights):
    light = patches.Circle((x_coords[i], y_coords[i]), 0.05, color=light_colors[i])
    ax.add_patch(light)
    lights.append(light)

# Set the background color
ax.set_facecolor(background_color)

# Set the axis limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Set the axis aspect ratio to be equal
ax.set_aspect('equal')

# Define the animation function
def animate(frame):
    # Update the x and y coordinates of the point lights
    x_coords[:] = np.sin(np.linspace(0, 2 * np.pi, num_lights, endpoint=False) + frame / 10)
    y_coords[:] = np.sin(np.linspace(0, 2 * np.pi, num_lights, endpoint=False) + frame / 10) * 0.6 + 0.3

    # Update the light positions
    for i in range(num_lights):
        lights[i].center = (x_coords[i], y_coords[i])

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=20)

# Display the animation
plt.show()
