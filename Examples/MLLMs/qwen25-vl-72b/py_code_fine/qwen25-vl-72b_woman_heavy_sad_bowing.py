
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
points = np.array([
    [0, 0], [1, 1], [2, 2], [3, 3], [4, 4],
    [0, 1], [1, 2], [2, 3], [3, 4], [4, 5],
    [0, 2], [1, 3], [2, 4], [3, 5], [4, 6]
])

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 7)
ax.set_facecolor('black')

# Create the scatter plot
scatter = ax.scatter(points[:, 0], points[:, 1], color='white')

# Define the update function for the animation
def update(frame):
    global points
    # Apply a small random displacement to each point
    displacement = np.random.normal(0, 0.1, points.shape)
    points += displacement
    # Update the scatter plot
    scatter.set_offsets(points)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

# Show the animation
plt.show()
