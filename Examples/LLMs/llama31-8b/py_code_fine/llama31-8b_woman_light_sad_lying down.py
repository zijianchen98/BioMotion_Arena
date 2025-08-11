
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters of the animation
num_lights = 15
light_radius = 5
num_frames = 60

# Define the position of the point lights
lights_x = np.linspace(-8, 8, num_lights)
lights_y = np.linspace(-6, 6, num_lights)
lights_z = np.linspace(-2, 2, num_lights)

# Create a grid of positions for the lights
x, y, z = np.meshgrid(lights_x, lights_y, lights_z)

# Initialize the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the function to animate
def animate(i):
    ax.clear()
    ax.set_axis_off()

    # Calculate the new positions of the lights
    theta = np.linspace(0, 2*np.pi, num_lights) + i/10
    x_new = 6 * np.cos(theta)
    y_new = 4 * np.sin(theta)
    z_new = -1 * np.sin(theta)

    # Plot the new positions of the lights
    ax.scatter(x_new, y_new, z_new, s=light_radius*2, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50)

# Display the animation
plt.show()
