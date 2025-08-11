
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Set up the figure and axis
fig, ax = plt.subplots()

# Set up the black background
ax.set_facecolor('black')

# Set up the point lights
lights = []
for i in range(15):
    light = patches.Circle((np.random.uniform(0, 1), np.random.uniform(0, 1)), 0.05, edgecolor='white', facecolor='white', alpha=0.5)
    lights.append(light)
    ax.add_patch(light)

# Set up the initial positions of the point lights
light_positions = np.array([np.random.uniform(0, 1), np.random.uniform(0, 1)]).reshape(-1, 2)

# Function to update the positions of the point lights
def update(frame):
    global light_positions
    # Move the point lights up and then down in a smooth and natural motion
    light_positions[:, 1] = np.sin(frame / 10.0)
    ax.clear()
    ax.set_facecolor('black')
    for i, light in enumerate(lights):
        ax.add_patch(light)
        x, y = light_positions[i]
        light.set_xy((x, y))

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
