
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axis
fig, ax = plt.subplots()

# Set the axis limits
ax.set_xlim(( 0, 10))
ax.set_ylim((-1, 1))

# Create a list to hold the point-lights
points = []

# Create the point-lights
for i in range(15):
    point, = ax.plot([], [], 'o', color='white')
    points.append(point)

# Function to update the point-lights
def update(num):
    for i, point in enumerate(points):
        point.set_data([num, -1 + 2 * i / 14], [0, 0])
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=10, interval=100, blit=True)

# Show the animation
plt.show()
