
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
duration = 5  # duration of animation in seconds
fps = 30  # frames per second

# Create figure with black background
fig, ax = plt.subplots()
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_aspect('equal', adjustable='box')
ax.set_facecolor('black')

# Initialize point positions
points = 10 * np.random.rand(num_points, 2)

# Create a list of point sizes in the animation
s = [200] * num_points
plots = ax.scatter(points[:,0], points[:,1], s=s, color='white')

# Updating function for animation
def update(num, points, plots):
    points[:, 1] = points[:, 1] + np.sin(num/10)
    plots.set_offsets(points)
    return plots,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=range(fps*duration),
                              fargs=(points, plots), interval=1000/fps)

# Display animation
plt.show()
