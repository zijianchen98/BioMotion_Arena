
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()

# Define the parameters
num_lights = 15
light_radius = 0.05
background_color = 'black'
light_color = 'white'

# Create a list to hold the light positions
light_positions = np.zeros((num_lights, 2))

# Define the movement of the sadman
def sadman_movement(frame):
    # Define the movement of each light
    light_positions[:, 0] = np.sin(np.linspace(0, 4 * np.pi, num_lights, endpoint=False) + frame / 10)
    light_positions[:, 1] = np.cos(np.linspace(0, 4 * np.pi, num_lights, endpoint=False) + frame / 10)

    # Update the plot
    ax.clear()
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect('equal')
    ax.set_facecolor(background_color)

    # Plot the lights
    for i in range(num_lights):
        ax.plot(light_positions[i, 0], light_positions[i, 1], 'o', markersize=light_radius * 2, color=light_color)

# Create the animation
ani = animation.FuncAnimation(fig, sadman_movement, frames=range(100), interval=20)

# Display the animation
plt.show()
