
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters for the animation
num_lights = 15
light_radius = 0.1
light_color = 'white'
background_color = 'black'

# Create a figure and an axes object
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor(background_color)

# Create a list to store the light positions
light_positions = []

# Define the animation function
def animate(i):
    global light_positions
    # Generate random positions for the lights
    for j in range(num_lights):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        light_positions.append([x, y])

    # Draw the lights
    for i, position in enumerate(light_positions):
        ax.plot(position[0], position[1], 'o', color=light_color, markersize=light_radius)

    return ax,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=10, blit=True)

# Show the animation
plt.show()
