
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_lights = 15

# Define the size of the animation
width, height = 800, 600

# Define the position of the lights
positions = np.random.rand(num_lights, 2) * width
# Define the initial angle of the lights
angles = np.random.rand(num_lights, 1) * 2 * np.pi

# Define the animation function
def animate(i):
    # Update the positions of the lights
    positions[:, 0] += 0.01 * np.cos(angles[i])
    positions[:, 1] += 0.01 * np.sin(angles[i])

    # Create the figure and axes
    fig, ax = plt.subplots(figsize=(width / 100, height / 100))
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Plot the lights
    for i in range(num_lights):
        ax.plot(positions[i, 0], positions[i, 1], 'w', marker='o', markersize=5)

    return ax

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=10, blit=True)

# Show the animation
plt.show()
