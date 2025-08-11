
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Set the figure size
fig, ax = plt.subplots(figsize=(10, 10))

# Set the background color to black
ax.set_facecolor('black')

# Define the point-light stimulus parameters
num_lights = 15
light_positions = np.random.uniform(-1, 1, num_lights, dtype=float) + 1
light_sizes = np.random.uniform(0.01, 0.1, num_lights, dtype=float)
light_colors = np.random.uniform(0, 1, num_lights, dtype=float)

# Create the point-light stimulus
def create_light(i):
    light = patches.Circle((light_positions[i], 0), light_sizes[i], color=light_colors[i], alpha=0.8)
    ax.add_patch(light)

# Create the animation
def animate(i):
    for j in range(num_lights):
        if j == i:
            ax.add_patch(patches.Circle((light_positions[j], 0), light_sizes[j], color=light_colors[j], alpha=0.8))
            ax.add_patch(patches.Circle((light_positions[j], 0.5), light_sizes[j], color=light_colors[j], alpha=0.8))
        else:
            ax.add_patch(patches.Circle((light_positions[j], 0), light_sizes[j], color=light_colors[j], alpha=0.8))
            ax.add_patch(patches.Circle((light_positions[j], 0.5), light_sizes[j], color=light_colors[j], alpha=0.8))
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1.5)
    ax.set_aspect('equal')

ani = animation.FuncAnimation(fig, animate, frames=num_lights, interval=500)

plt.show()
