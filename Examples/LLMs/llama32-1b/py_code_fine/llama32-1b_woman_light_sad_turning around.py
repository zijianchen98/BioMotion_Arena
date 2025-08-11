
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Generate 15 white point-lights
lights = []
for i in range(15):
    angle = i * np.pi / 8
    x = WIDTH / 2 + np.cos(angle) * 100
    y = HEIGHT / 2 + np.sin(angle) * 100
    lights.append((x, y, i))

# Define the figure and axis
fig, ax = plt.subplots()

# Initialize the point-light positions
point_lights = []
for i in range(15):
    point_lights.append((WIDTH / 2, HEIGHT / 2))

# Function to update the point-light positions
def update(frame):
    for i, light in enumerate(point_lights):
        x, y = light
        angle = i * np.pi / 8
        x += np.cos(angle) * 5
        y += np.sin(angle) * 5
        point_lights[i] = (x, y)
    ax.clear()
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_aspect('equal')
    for light in lights:
        ax.add_patch(plt.Circle(light, 2, color=WHITE, alpha=0.5))
    plt.draw()

# Animate the point-light positions
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=10)

plt.show()
