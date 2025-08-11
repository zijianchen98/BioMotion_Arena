
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point lights
initial_positions = np.array([
    [0, 5], [ -1, 4], [0, 4], [1, 4], [-2, 3], [-1, 3], [0, 3], [1, 3], [2, 3],
    [-1, 2], [0, 2], [1, 2], [-1, 1], [0, 1], [0, 0]
])


# Define a function to update the positions of the point lights at each frame
def update(frame_num, points, line):
    #Simple rotation for demonstration
    angle = frame_num * 0.1  # Adjust speed here.
    rotated_points = points @ np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    line.set_data(rotated_points[:, 0], rotated_points[:, 1])  
    return line,


# Set up the figure and axes
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-5, 5), ylim=(-5, 10))
ax.set_facecolor('black')

# Create the point lights
points, = ax.plot([], [], 'wo', markersize=8)


# Create the animation
ani = animation.FuncAnimation(fig, update, fargs=(initial_positions, points),
                              frames=100, interval=50, blit=True)

# Show the animation
plt.show()

