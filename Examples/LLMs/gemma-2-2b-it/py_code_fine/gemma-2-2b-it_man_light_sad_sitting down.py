
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of lights
num_lights = 15

# Define light positions and colors
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

# Create a figure and axes
fig, ax = plt.subplots(1, 1, figsize=(8, 8))

# Create a black background
ax.set_facecolor('black')

# Create a line for the animation
line, = ax.plot([], [], 'k-', linewidth=1)

# Define the animation function
def animate(i):
    # Update the light positions
    for j in range(num_lights):
        light_positions[j] = np.array([
            light_positions[j][0] + np.random.uniform(-0.1, 0.1),
            light_positions[j][1] + np.random.uniform(-0.1, 0.1),
            light_positions[j][2] + np.random.uniform(-0.1, 0.1)
        ])

    # Update the line
    line.set_data(light_positions[:, 0], light_positions[:, 1])
    line.set_data(light_positions[:, 0], light_positions[:, 1])

    return line,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=10, blit=True)

# Show the animation
plt.show()
