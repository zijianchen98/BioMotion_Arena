
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point lights
num_points = 15
points, = ax.plot([], [], 'wo', markersize=8)

# Define the initial positions of the point lights
initial_positions = np.array([
    [0, 5],
    [-1, 4],
    [0, 4],
    [1, 4],
    [-2, 3],
    [-1, 3],
    [0, 3],
    [1, 3],
    [2, 3],
    [-1, 2],
    [0, 2],
    [1, 2],
    [0, 1],
    [-0.5, 0],
    [0.5, 0]
])

# Define a function to update the positions of the point lights
def animate(i):
    # Generate new positions based on a simple running motion
    positions = initial_positions.copy()
    positions[:, 0] += np.sin(i * 0.1) * 2  # horizontal movement
    positions[:, 1] += np.cos(i * 0.1) * 1 # vertical movement + some bounce

    # Add some noise to the movement
    positions += np.random.randn(num_points, 2) * 0.2

    # Update the point lights' positions
    points.set_data(positions[:, 0], positions[:, 1])
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Show the animation
plt.show()

