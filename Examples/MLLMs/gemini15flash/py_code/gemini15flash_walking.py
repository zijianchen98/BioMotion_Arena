
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the points
num_points = 15
points, = ax.plot([], [], 'wo', markersize=8)

# Define the initial positions of the points
initial_positions = np.array([
    [0, 5],
    [-1, 4],
    [1, 4],
    [-2, 3],
    [0, 3],
    [2, 3],
    [-2.5, 2],
    [-1.5, 2],
    [0, 2],
    [1.5, 2],
    [2.5, 2],
    [-1, 1],
    [1, 1],
    [-0.5, 0],
    [0.5, 0]
])

# Function to update the animation
def animate(i):
    # Define the walking motion (example)
    x = initial_positions[:, 0] + 2 * np.sin(i * 0.1)
    y = initial_positions[:, 1] + 0.5 * np.cos(i * 0.1) + 2*np.sin(i * 0.05)

    #add some noise to simulate biological motion
    noise = np.random.normal(0, 0.1, size=(num_points, 2))
    x += noise[:, 0]
    y += noise[:, 1]

    # Update the points
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Show the animation
plt.show()

