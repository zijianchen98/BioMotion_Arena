
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the animation parameters
frame_rate = 30  # Frames per second
duration = 1  # Duration of the animation in seconds

# Define the movement parameters
walking_speed = 0.5  # Speed of the walk
walking_direction = np.array([1, 0])  # Direction vector for walking

# Create the points
points = np.zeros((num_points, 2))
for i in range(num_points):
    points[i, 0] = np.cos(i * 2 * np.pi / num_points) * walking_speed
    points[i, 1] = np.sin(i * 2 * np.pi / num_points) * walking_speed

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the point lights
point_lights = []
for i in range(num_points):
    point_lights.append(plt.Circle((0, 0), 0.1, color='white', fill=False))

# Create the animation
def animate(i):
    for light in point_lights:
        light.center = points[i]
    return point_lights

ani = animation.FuncAnimation(fig, animate, frames=int(duration * frame_rate), interval=1000 / frame_rate, blit=True)

# Show the animation
plt.show()
