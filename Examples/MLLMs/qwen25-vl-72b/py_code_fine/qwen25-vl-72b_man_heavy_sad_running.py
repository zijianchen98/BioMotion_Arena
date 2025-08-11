
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')

# Create the point lights
points = []
for i in range(15):
    point, = ax.plot([], [], 'wo', markersize=5)
    points.append(point)

# Define the initial positions of the point lights
x = [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7]
y = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]

# Define the update function for the animation
def update(frame):
    global x, y
    # Update the positions of the point lights
    for i in range(len(points)):
        x[i] += np.random.normal(0, 0.1)
        y[i] += np.random.normal(0, 0.1)
        points[i].set_data(x[i], y[i])
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

# Show the animation
plt.show()
