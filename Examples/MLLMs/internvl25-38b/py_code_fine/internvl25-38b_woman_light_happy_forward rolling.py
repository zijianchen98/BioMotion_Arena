
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure, the axis, and the plot element
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
points, = ax.plot([], [], 'wo', markersize=10)

# Number of points
n_points = 15

# Initial positions of the points
positions = np.array([
    [5, 5],
    [5.2, 5.2],
    [5.4, 4.8],
    [5.6, 5.3],
    [5.8, 4.7],
    [6, 5.1],
    [6.2, 4.5],
    [6.4, 5.2],
    [6.6, 4.8],
    [6.8, 5.3],
    [7, 4.7],
    [7.2, 5.1],
    [7.4, 4.5],
    [7.6, 5.2],
    [7.8, 4.8]
])

# Velocity vectors (initially set to zero)
velocities = np.zeros((n_points, 2))

# Function to update the positions of the points
def update(frame):
    global positions, velocities

    # Update the velocity vectors to simulate forward rolling motion
    velocities[:, 0] += 0.02 * np.cos(np.linspace(0, np.pi * 2, n_points))
    velocities[:, 1] += 0.02 * np.sin(np.linspace(0, np.pi * 2, n_points))

    # Update the positions of the points
    positions += velocities

    # Apply boundary conditions to make it cyclic
    positions = positions % 10

    # Update the plot
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Show the plot
plt.axis('off')
plt.show()
