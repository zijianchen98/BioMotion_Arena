
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of lights
num_lights = 15

# Define light positions and movement parameters
light_positions = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [2, 0, 0],
    [3, 0, 0],
    [4, 0, 0],
    [5, 0, 0],
    [6, 0, 0],
    [7, 0, 0],
    [8, 0, 0],
    [9, 0, 0],
    [10, 0, 0],
    [11, 0, 0],
    [12, 0, 0],
    [13, 0, 0],
    [14, 0, 0],
])

# Define light colors
light_colors = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
])

# Define the animation function
def animate(i):
    # Update light positions based on a simple walking motion
    for j in range(num_lights):
        light_positions[j] = light_positions[j] + np.array([
            0.1 * np.cos(i * 0.05 * j),
            0.1 * np.sin(i * 0.05 * j),
            0
        ])

    # Update light colors based on a simple color gradient
    for j in range(num_lights):
        light_colors[j] = np.array([
            1 - (i / 100),
            1 - (i / 100),
            1 - (i / 100)
        ])

    return light_positions, light_colors

# Create the figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the point lights
light_objects = []
for i in range(num_lights):
    light_objects.append(ax.scatter(light_positions[i][0], light_positions[i][1], light_positions[i][2], s=0.1, c=light_colors[i]))

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=10, blit=True)

# Show the animation
plt.show()
