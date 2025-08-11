
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
POINT_LIGHT_COLOR = (255, 255, 255)
LIGHT_COUNT = 15

# Generate white point lights
def generate_point_lights(x, y, z):
    points = np.zeros((LIGHT_COUNT, 3))
    for i, (x_light, y_light, z_light) in enumerate(zip(x, y, z)):
        points[i] = np.array([x_light, y_light, z_light])
    return points

# Plot the point lights
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
for i, points in enumerate(generate_point_lights(np.random.uniform(0, WIDTH, 3), np.random.uniform(0, HEIGHT, 3), np.random.uniform(0, 10, 3))):
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=WHITE, s=0.1)
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.set_zlim(0, HEIGHT)
plt.show()

# Generate the animation
def generate_animation(frame):
    global x, y, z
    x, y, z = np.random.uniform(0, WIDTH, 3), np.random.uniform(0, HEIGHT, 3), np.random.uniform(0, 10, 3)
    points = generate_point_lights(x, y, z)
    for i in range(frame):
        ax.clear()
        ax.set_xlim(0, WIDTH)
        ax.set_ylim(0, HEIGHT)
        ax.set_zlim(0, HEIGHT)
        ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=WHITE, s=0.1)
        plt.pause(0.01)

# Start the animation
frame = 0
generate_animation(frame)
