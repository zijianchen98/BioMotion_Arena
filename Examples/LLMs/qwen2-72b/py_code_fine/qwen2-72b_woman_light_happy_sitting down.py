
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and their initial positions
num_points = 15
points = np.random.rand(num_points, 2)

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_facecolor('black')

# Create a scatter plot for the points
scatter = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

def update(frame):
    # Update the position of each point
    global points
    velocity = np.random.normal(0, 0.01, size=(num_points, 2))
    points += velocity

    # Wrap around if any point goes out of bounds
    points %= 1

    # Update the scatter plot data
    scatter.set_offsets(points)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=30, blit=True)

plt.show()
