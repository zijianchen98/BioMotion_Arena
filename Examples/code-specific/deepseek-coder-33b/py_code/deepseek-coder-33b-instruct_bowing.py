
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Set the limits of the x and y axis
ax.set_xlim(( 0, 2))
ax.set_ylim((-2, 2))

# Create a list of 15 point-lights
points = np.random.rand(2, 15)

# Create a scatter plot of the point-lights
scat = ax.scatter(points[0], points[1])

# Define the update function for the animation
def update(i):
    points[1] = np.sin(points[0] + i/10.0)
    scat.set_offsets(points.T)

# Create the animation
ani = animation.FuncAnimation(fig, update, interval=50)

# Show the animation
plt.show()
