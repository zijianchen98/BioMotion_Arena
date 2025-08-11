
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

# Create a line for the light
line, = ax.plot([], [], 'ro', markersize=1)

# Create a list to store the light positions
light_positions_list = []

# Create a list to store the light colors
light_colors_list = []

# Create a list to store the light positions and colors
light_data = []

# Define the animation function
def animate(i):
    global light_positions_list, light_colors_list, light_data
    
    # Update the light positions and colors
    light_positions_list = light_positions
    light_colors_list = light_colors
    light_data = [light_positions_list, light_colors_list]
    
    # Update the plot
    line.set_data(light_positions_list[i], light_colors_list[i])
    
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=10, blit=True)

# Show the animation
plt.show()
