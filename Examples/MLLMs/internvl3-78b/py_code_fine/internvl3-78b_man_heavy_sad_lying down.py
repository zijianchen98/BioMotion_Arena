
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the points' positions over time
point_light_positions = np.array([
    # Each row represents a point light's positions over time (frames)
    # Format: [time_steps, x_positions, y_positions]

    # First set of points
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3], [10, 8, 6, 4, 2, 1, 0, 1, 3, 5, 7]],

    # Add more points as needed
])

# Extract time frames (assumes all points have equal time steps)
time = point_light_positions[0][0]

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-20, 20)  # set limit for X
ax.set_ylim(-10, 20)  # set limit for Y
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create a list to hold the point-light animation artists
linepoints, = ax.plot([], [], 'wo')

# Initialization function
def init():
    linepoints.set_data([], [])
    return linepoints,

# Update function for animation
def animate(i):
    x_data = np.array([point_light_positions[j][1][i] for j in range(len(point_light_positions))])
    y_data = np.array([point_light_positions[j][2][i] for j in range(len(point_light_positions))])
    linepoints.set_data(x_data, y_data)
    return linepoints,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=len(time), init_func=init, blit=True, repeat=False)

# Show animation
plt.show()
