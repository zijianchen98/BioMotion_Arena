
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_lights = 15

# Define the animation parameters
frame_rate = 30  # Frames per second
duration = 1  # Duration of the animation in seconds

# Define the position of the point lights
positions = np.array([
    [0, 0],
    [1, 0],
    [2, 0],
    [3, 0],
    [4, 0],
    [5, 0],
    [6, 0],
    [7, 0],
    [8, 0],
    [9, 0],
    [10, 0],
    [11, 0],
    [12, 0],
    [13, 0],
    [14, 0],
    [15, 0],
])

# Define the movement parameters
speed = 0.1  # Speed of the movement
direction = np.array([0, 1])  # Direction of movement

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the point lights
point_lights = []
for i in range(num_lights):
    point_lights.append(plt.Circle((0, 0), 0.1, color='white', fill=False))

# Create the animation
def animate(i):
    for light in point_lights:
        light.center = positions[i]
    return point_lights,

ani = animation.FuncAnimation(fig, animate, frames=num_lights, interval=1000/frame_rate, blit=True)

# Show the animation
plt.show()
