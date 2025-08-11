
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Define the figure and axis
fig, ax = plt.subplots()

# Set the aspect ratio and the limits of the axis
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')

# Initialize the point lights
point_lights = []
for i in range(15):
    x = np.random.uniform(-2, 2)
    y = np.random.uniform(-2, 2)
    point_lights.append(Circle((x, y), 0.1, edgecolor='white', facecolor='white'))

# Add the point lights to the axis
for light in point_lights:
    ax.add_patch(light)

# Function to update the point lights
def update(i):
    # Update the position of the point lights
    for j in range(15):
        angle = 2 * np.pi * j / 15
        x = 0.5 * np.cos(angle)
        y = 0.5 * np.sin(angle)
        if j < 7:
            x += 0.2 * np.cos(i + j / 10)
            y += 0.2 * np.sin(i + j / 10)
        elif j < 10:
            x -= 0.2 * np.cos(i + j / 10)
            y -= 0.2 * np.sin(i + j / 10)
        elif j < 12:
            x += 0.2 * np.cos(i + j / 10)
            y += 0.2 * np.sin(i + j / 10)
        else:
            x -= 0.2 * np.cos(i + j / 10)
            y -= 0.2 * np.sin(i + j / 10)
        point_lights[j].center = (x, y)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=20)

# Show the animation
plt.show()
