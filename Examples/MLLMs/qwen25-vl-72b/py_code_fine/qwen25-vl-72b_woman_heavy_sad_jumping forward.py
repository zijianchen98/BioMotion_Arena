
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
points = np.array([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4],
                   [1, -1], [2, -2], [3, -3], [4, -4],
                   [-1, 1], [-2, 2], [-3, 3], [-4, 4],
                   [-1, -1], [-2, -2], [-3, -3]])

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')

# Create the scatter plot of the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Define the update function for the animation
def update(frame):
    global points
    # Update the positions of the points
    points[:, 0] += 0.1 * np.sin(frame / 10)
    points[:, 1] += 0.1 * np.cos(frame / 10)
    scat.set_offsets(points)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
