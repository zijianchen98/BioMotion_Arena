
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Define the dimensions of the animation
width, height = 800, 600

# Define the number of point lights
num_lights = 15

# Define the positions and sizes of the point lights
light_positions = np.array([
    [0, 0, 0],
    [width / 2 - 100, height / 2 - 50, 0],
    [width / 2 - 100, height / 2 + 50, 0],
    [width / 2 + 100, height / 2 - 50, 0],
    [width / 2 + 100, height / 2 + 50, 0],
    [width / 4, height / 2 - 100, 0],
    [width - width / 4, height / 2 - 100, 0],
    [width / 4, height / 2 + 100, 0],
    [width - width / 4, height / 2 + 100, 0],
    [width / 4, height / 2 - 150, 0],
    [width - width / 4, height / 2 - 150, 0],
    [width / 4, height / 2 + 150, 0],
    [width - width / 4, height / 2 + 150, 0],
    [width / 2, height / 4, 0],
    [width / 2, height - height / 4, 0]
])

light_sizes = np.array([20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20])

# Define the angles and velocities of the point lights
angles = np.linspace(0, 2 * np.pi, 100)
velocities = np.linspace(0.01, 0.1, 100)

# Create a figure and axis
fig, ax = plt.subplots()

# Set the axis limits and aspect ratio
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.set_aspect('equal')

# Create a black background
background = np.zeros((height, width, 3), dtype=np.uint8)
background[:, :, 0] = 0
background[:, :, 1] = 0
background[:, :, 2] = 0

# Plot the point lights
for i in range(num_lights):
    light_x, light_y, _ = light_positions[i]
    light_size = light_sizes[i]
    ax.plot([light_x, light_x + light_size * np.cos(angles[i])], [light_y, light_y + light_size * np.sin(angles[i])], color=(1, 1, 1), lw=1)

# Animate the point lights
for frame in range(100):
    ax.clear()
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    ax.imshow(background, cmap='gray')
    for i in range(num_lights):
        light_x, light_y, _ = light_positions[i]
        light_size = light_sizes[i]
        velocity = velocities[i]
        angle = angles[i] + velocity
        ax.plot([light_x, light_x + light_size * np.cos(angle)], [light_y, light_y + light_size * np.sin(angle)], color=(1, 1, 1), lw=1)
    plt.pause(0.01)

plt.show()
