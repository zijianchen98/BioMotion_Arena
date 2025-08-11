
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Define the coordinates of the 15 point-lights representing the happyman
x = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7])
y = np.array([3, 4, 4.5, 4, 3.5, 3.5, 3, 2.5, 2.5, 3, 3.5, 3.5, 4, 4.5, 4])

# Define the function to update the point-lights positions at every frame
def update(frame):
    x = np.roll(x, 1)  # Move all points one step to the left
    y = np.roll(y, -1)  # Move all points one step to the right
    y = y + frame * 0.1  # Add an upward movement
    return points,

# Create a figure and axes
fig, ax = plt.subplots()

# Create the point-lights
points, = ax.plot([], [], 'bo', markersize=10)

# Set the view limit to fit the plot
ax.set_xlim(0, 7)
ax.set_ylim(-1, 5)

# Animate!
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 30, 0.1),
                              interval=33, blit=True)

plt.show()
