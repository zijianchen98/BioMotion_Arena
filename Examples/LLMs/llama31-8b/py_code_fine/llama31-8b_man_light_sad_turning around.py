
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Set up the figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Create a circle to represent the body
body = patches.Circle((0, 0), 0.5, edgecolor='white', facecolor='none')
ax.add_patch(body)

# Create 15 point lights
lights = []
for i in range(15):
    x = np.sin(2 * np.pi * i / 15) * 0.4
    y = np.cos(2 * np.pi * i / 15) * 0.4
    light = patches.Circle((x, y), 0.02, edgecolor='white', facecolor='white')
    ax.add_patch(light)
    lights.append(light)

# Set the limits of the axis
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')

# Function to update the animation
def update(frame):
    for i, light in enumerate(lights):
        x = np.sin(2 * np.pi * (i + frame / 15) / 15) * 0.4
        y = np.cos(2 * np.pi * (i + frame / 15) / 15) * 0.4
        light.center = (x, y)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=300, blit=False, interval=20)

# Show the animation
plt.show()
