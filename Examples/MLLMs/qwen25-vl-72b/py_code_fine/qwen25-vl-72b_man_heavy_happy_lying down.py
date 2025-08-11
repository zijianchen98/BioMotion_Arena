
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
points = np.array([
    [0, 0], [1, 0], [2, 0],
    [0, 1], [1, 1], [2, 1],
    [0, 2], [1, 2], [2, 2],
    [0, 3], [1, 3], [2, 3],
    [0, 4], [1, 4], [2, 4]
])

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 3)
ax.set_ylim(-1, 5)
ax.set_facecolor('black')

# Create the scatter plot
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

def update(frame):
    # Update the positions of the points
    global points
    points += np.random.normal(0, 0.1, points.shape)
    scat.set_offsets(points)

ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)
plt.show()
