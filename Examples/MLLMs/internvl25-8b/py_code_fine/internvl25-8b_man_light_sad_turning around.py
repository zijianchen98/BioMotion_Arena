
import matplotlib.pyplot as plt
import numpy as np

# Number of points
num_points = 15

# Angle speed in radians per second (we need to keep the simulation relatively fast)
angle_speed = 0.025

# Time duration in seconds
duration = 10

# Create a figure
fig = plt.figure()
ax = plt.Axes(fig, [0, 0, 1, 1], frame_on=False)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')
ax.set_axis_off()
plt.show()

# List to hold the point objects
points = []

# Define color and size
color = 'white'
size = 1

# Create the points
for i in range(num_points):
    circle = plt.Circle((0.5, 0.5), size, color=color)
    angle = i * angle_speed * duration
    angle_position = np.sin(angle)
    circle.center = (0.5, 0.5 + angle_position * 0.5)
    circle.set_clip_on(False)
    ax.add_patch(circle)
    points.append(circle)

# Animation loop
for i in range(1000):
    angle = i * angle_speed * duration
    angle_position = np.sin(angle)
    for j, point in enumerate(points):
        point.center = (0.5, 0.5 + angle_position * 0.5 + (j / (num_points - 1)) * 0.2)
    plt.draw()
    plt.pause(0.01)
