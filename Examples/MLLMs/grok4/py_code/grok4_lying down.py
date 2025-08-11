
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Set the number of point lights
num_points = 15

# Set initial positions of point lights
# Representing a man lying down with a set of points
points_positions = np.array([
    [0, 7],   # head
    [-1, 6],  # left shoulder
    [1, 6],   # right shoulder
    [-1, 5],  # left elbow
    [1, 5],   # right elbow
    [0, 4],   # chest
    [-1, 4],  # left hip
    [1, 4],   # right hip
    [-1, 3],  # left knee
    [1, 3],   # right knee
    [-1, 2],  # left ankle
    [1, 2],   # right ankle
    [0, 3],   # spine
    [0, 5],   # stomach
    [0, 6],   # neck
    [0, 8]    # base point for gravity reference
])

# Setup figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(0, 10)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Initialization function for the animation
def init():
    points.set_data([], [])
    return points,

# Animation function
def animate(i):
    # Update the y-coordinates of the points to create a smooth lie-down motion
    new_positions = points_positions.copy()
    new_positions[:, 1] -= 0.05 * np.sin(i / 10.0)  # Simulate slight rocking
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=200, init_func=init, blit=True)

# Display the animation
plt.show()
