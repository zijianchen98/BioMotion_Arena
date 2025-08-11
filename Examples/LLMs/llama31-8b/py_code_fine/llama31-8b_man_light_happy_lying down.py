
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()

# Define the parameters for the animation
num_lights = 15
num_frames = 100
light_radius = 2
light_color = 'white'
background_color = 'black'

# Define the positions of the lights for the specified action (lying down)
lights_x = np.linspace(-5, 5, num_lights)
lights_y = np.linspace(-5, 5, num_lights)
lights_x, lights_y = np.meshgrid(lights_x, lights_y)
lights_x = lights_x.flatten()
lights_y = lights_y.flatten()

# Initialize the light positions
light_positions = np.array([lights_x, lights_y]).T

# Define the animation function
def animate(frame):
    # Update the light positions based on the specified action (lying down)
    light_positions[:, 0] = 5 * np.sin(2 * np.pi * frame / num_frames)
    light_positions[:, 1] = 5 * np.cos(2 * np.pi * frame / num_frames)

    # Clear the axis
    ax.clear()

    # Set the axis limits and background color
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_facecolor(background_color)

    # Plot the lights
    for i in range(num_lights):
        ax.scatter(light_positions[i, 0], light_positions[i, 1], s=light_radius*light_radius, color=light_color, alpha=1)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50)

# Show the animation
plt.show()
