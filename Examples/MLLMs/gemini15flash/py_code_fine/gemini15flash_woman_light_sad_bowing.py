
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the points
num_points = 15
points, = ax.plot([], [], 'wo', markersize=8)

# Define the initial positions of the points
initial_positions = np.array([
    [0, 4],
    [-1, 3],
    [0, 3],
    [1, 3],
    [-2, 2],
    [-1, 2],
    [0, 2],
    [1, 2],
    [2, 2],
    [-1, 1],
    [0, 1],
    [1, 1],
    [0, -1],
    [0, -2],
    [0, -3],

])


# Define the animation function
def animate(i):
    # Calculate the new positions of the points based on time
    #  This is a simple example, and you can modify it to create more complex animations.
    dt = 0.05
    t = i * dt
    positions = initial_positions.copy()
    positions[:, 1] -= np.sin(t) *2  #bowing motion

    # Update the points
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=20, blit=True)


# Show the animation
plt.show()

