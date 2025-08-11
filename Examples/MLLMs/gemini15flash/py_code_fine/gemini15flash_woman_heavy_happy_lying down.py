
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_facecolor('black')
ax.axis('off')

# Initialize the point-light positions
num_points = 15
points, = ax.plot([], [], 'wo', markersize=10)

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
    [-0.5, 0],
    [0.5, 0],
    [0, -1]
])


# Animation function
def animate(i):
    # Define the animation of the points
    new_positions = np.copy(initial_positions)

    # Simulate a simple lying-down motion
    amplitude = 0.5
    frequency = 0.1
    phase_shift = np.pi / 2

    for j in range(len(new_positions)):
        new_positions[j][0] += amplitude * np.sin(i * frequency + j * phase_shift)
        new_positions[j][1] += amplitude * np.cos(i * frequency + j * phase_shift)

    # Update the point positions
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation
plt.show()

