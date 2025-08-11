
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_facecolor('black')
ax.axis('off')

# Initialize the point lights
num_points = 15
points, = ax.plot([], [], 'wo', markersize=8)

# Define the initial positions of the points
initial_positions = np.array([
    [0, 2], [-1, 1], [0, 1], [1, 1], [-1.5, 0], [-0.5, 0], [0.5, 0], [1.5, 0],
    [-1, -1], [0, -1], [1, -1], [-0.5, -2], [0.5, -2], [-0.5, -3], [0.5, -3]
])


# Define the animation function
def animate(i):
    # Generate new positions based on a simple animation model
    # This model simulates a person lying down and slightly moving
    new_positions = initial_positions.copy()
    time = i/100
    new_positions[:,1] -= 0.01*np.sin(time)

    # Update the point light positions
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=20, blit=True)

# Show the animation
plt.show()

