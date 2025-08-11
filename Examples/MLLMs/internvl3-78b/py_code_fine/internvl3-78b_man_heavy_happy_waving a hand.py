
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

# Create a new plot
fig = plt.figure()
ax = fig.add_subplot(111)

# Set the x and y data
x_data = np.array([0.25, 0.5, 0.5, 0.75, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, 1.0, 0.5, 0.5, 0.5, 0.5])
y_data = np.array([0.5, 0.25, 0.75, 0.5, 0.125, 0.375, 0.625, 0.875, 0.5, 0.55, 0.55, 0.45, 0.45, 0.55, 0.54])

# Create the line, we will update the xy-data later
scat = ax.scatter(x_data, y_data, s=50, c='w')

# Setting the axes properties (for visibility)
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1.1)
plt.axis('off')

# Animation function
def animate(i, scat, x_data, y_data):
    scat.set_offsets(np.column_stack(( [x + f(i) for x in x_data], y_data )))
    return scat,

# Generate a wave-like motion in the x-axis
def f(i):
    t = 0.1 * i
    return np.sin(t) * 0.2

# Initialize the animation
ani = animation.FuncAnimation(fig, animate, fargs=(scat, x_data, y_data), frames=100, interval=50)

# Show the plot
plt.show()
