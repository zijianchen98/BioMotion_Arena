
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# Define the figure and axis
fig, ax = plt.subplots()

# Define the point lights
lights = []
for i in range(15):
    x = np.random.uniform(0, 1)
    y = np.random.uniform(0, 1)
    lights.append(ax.plot(x, y, 'w', markersize=10)[0])

# Define the initial positions of the lights
initial_positions = np.random.uniform(0, 1, size=(15, 2))
for i, light in enumerate(lights):
    light.set_data(initial_positions[i, 0], initial_positions[i, 1])

# Define the action
def walk(frame):
    global initial_positions
    # Update the positions of the lights
    initial_positions[:, 0] += 0.05 * np.sin(frame * 0.1)
    initial_positions[:, 1] += 0.05 * np.cos(frame * 0.1)
    for i, light in enumerate(lights):
        light.set_data(initial_positions[i, 0], initial_positions[i, 1])

# Create the animation
ani = animation.FuncAnimation(fig, walk, frames=range(1000), interval=50)

# Show the animation
plt.show()
