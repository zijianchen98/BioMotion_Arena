
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MAN_SIZE = 50

# Define the point light source
def create_point_light(x, y, intensity):
    return np.array([x, y, intensity])

# Define the rotation function
def rotate_point_light(point_light, angle):
    x, y, intensity = point_light
    new_x = x + np.cos(angle) * 10
    new_y = y - np.sin(angle) * 10
    return create_point_light(new_x, new_y, intensity)

# Define the camera function
def camera(x, y):
    return np.array([x, y, 100])

# Create the point light sources
point_lights = []
for i in range(15):
    point_lights.append(create_point_light(100 + i * 50, 200, 50))

# Create the camera
camera_x, camera_y = 400, 300

# Create the figure and axis
fig, ax = plt.subplots()

# Define the rotation angle
angle = np.radians(45)

# Function to update the plot
def update(frame):
    global angle
    ax.clear()
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_aspect('equal')

    # Rotate the point lights
    rotated_lights = []
    for light in point_lights:
        rotated_light = rotate_point_light(light, angle)
        rotated_lights.append(rotated_light)

    # Draw the point lights
    for light in rotated_lights:
        ax.add_patch(plt.Rectangle((light[0], light[1]), 1, 1, color=WHITE, alpha=0.5))

    # Draw the camera
    ax.add_patch(plt.Rectangle((camera_x, camera_y), 1, 1, color=BLACK, alpha=0.5))

    # Update the plot
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_aspect('equal')
    ax.set_title(f'Frame {frame}')

ani = animation.FuncAnimation(fig, update, frames=100, interval=16, repeat=False)

plt.show()
