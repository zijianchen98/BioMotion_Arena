
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
points = np.array([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4],
                   [1, -1], [2, -2], [3, -3], [4, -4],
                   [-1, 1], [-2, 2], [-3, 3], [-4, 4],
                   [-1, -1], [-2, -2], [-3, -3]])

# Define the target positions of the points when sitting down
target_points = np.array([[0, -2], [1, -1], [2, 0], [3, 1], [4, 2],
                          [1, -3], [2, -4], [3, -5], [4, -6],
                          [-1, -1], [-2, 0], [-3, 1], [-4, 2],
                          [-1, -3], [-2, -4], [-3, -5]])

# Create a figure and axis with a black background
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-7, 5)

# Create a list of scatter objects for each point
scatters = []
for i in range(15):
    scatters.append(ax.scatter(points[i, 0], points[i, 1], color='white'))

# Define the update function for the animation
def update(num):
    global points
    # Move the points towards their target positions
    for i in range(15):
        direction = target_points[i] - points[i]
        distance = np.linalg.norm(direction)
        if distance > 0.1:
            points[i] += direction / distance * 0.1
        scatters[i].set_offsets(points[i])
    return scatters

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

plt.show()
