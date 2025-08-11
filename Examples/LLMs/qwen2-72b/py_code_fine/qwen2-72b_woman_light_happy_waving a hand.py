
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
np.random.seed(0)
n_points = 15
points = np.random.rand(n_points, 2) * [100, 100]

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim([0, 100])
ax.set_ylim([0, 100])
ax.set_facecolor('black')

# Create scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

def update(frame_number):
    global points
    # Update the position of each point
    for i in range(n_points):
        # Simple wave-like motion for demonstration
        points[i, 1] += 1 + 2 * np.sin(points[i, 0] / 10 + frame_number / 20)
        points[i, 0] += 0.1 * np.cos(points[i, 1] / 10 + frame_number / 20)

    # Update the scatter plot
    scat.set_offsets(points)
    return scat,

ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.show()
