
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 50], [ -10, 40], [10, 40], [-20,30], [0,30], [20,30], [-30, 20], [-10, 20], [10, 20], [30,20],
    [0, 10], [10, 10], [0, 0], [-10, -10], [10, -10]
])


# Function to update the positions of the point-lights for each frame
def update(frame, points, line):
    # Simulate a simple rolling motion for demonstration. Replace with more complex biomechanically plausible motion.

    #adjusting the y-axis positions to simulate rolling up
    new_y_axis = np.array([y + 0.5 * np.sin(0.1 * frame) for y in initial_positions[:,1]])

    new_positions = np.column_stack((initial_positions[:,0],new_y_axis))

    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,


# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-50, 50])
ax.set_ylim([-20, 100])
ax.set_aspect('equal')
ax.set_facecolor('black')


# Create the point-light scatter plot
points, = ax.plot([], [], 'wo', markersize=8)

# Create the animation
ani = animation.FuncAnimation(fig, update, fargs=(points, points,), frames=range(100), interval=50, blit=True)


# Show the animation
plt.show()

