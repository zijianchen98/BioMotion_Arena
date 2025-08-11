
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
points, = ax.plot([], [], 'wo', markersize=10)

# Define the initial positions of the points
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

# Animation function
def animate(i):
    #Simulate running motion with simple sinusoidal waves.  More sophisticated motion models could be implemented.

    x = initial_positions[:,0] + 2 * np.sin(i * 0.1 + np.linspace(0, 2*np.pi, num_points))
    y = initial_positions[:,1] + 2 * np.cos(i * 0.1 + np.linspace(0, 2*np.pi, num_points))

    #add a slight downward drift to simulate weight
    y -= 0.1*i

    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Show the animation
plt.show()

