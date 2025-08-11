
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Create a new figure
fig, ax = plt.subplots()

# Set the axis limits and aspect ratio
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')

# Create a black background
ax.set_facecolor('black')

# Create a list of 15 point lights
lights = []
for i in range(15):
    x = np.random.uniform(0, 10)
    y = np.random.uniform(0, 10)
    lights.append(ax.scatter(x, y, s=50, c='white'))

# Define the movement of the point lights
def animate(i):
    # Lying down motion
    for j, light in enumerate(lights):
        if j < 5:
            light.set_offsets([0.5 + 0.2 * np.sin(np.radians(10 * i)), 0.5 + 0.2 * np.cos(np.radians(10 * i))])
        elif j < 10:
            light.set_offsets([0.5 + 0.2 * np.sin(np.radians(20 * i)), 0.5 + 0.2 * np.cos(np.radians(20 * i))])
        else:
            light.set_offsets([0.5 + 0.2 * np.sin(np.radians(30 * i)), 0.5 + 0.2 * np.cos(np.radians(30 * i))])

    # Draw the body
    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    body = patches.Rectangle((0, 0), 10, 2, edgecolor='white', facecolor='none')
    ax.add_patch(body)

ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
