
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters
num_points = 15
num_frames = 100
frame_rate = 30

# Define the point positions
points = np.zeros((num_points, 2))
points[:, 0] = np.random.uniform(0, 1, num_points)
points[:, 1] = np.random.uniform(0, 1, num_points)

# Define the motion
theta = np.linspace(0, 2 * np.pi, num_frames)

# Define the radius and weight of the points
radius = 0.05
weight = 0.1

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
ax.set_aspect('equal')

# Initialize the point positions
def init():
    for i in range(num_points):
        ax.plot(points[i, 0], points[i, 1], 'o', markersize=radius * 2, color='white')
    return

# Update the point positions
def update(frame):
    for i in range(num_points):
        x = 0.5 + weight * np.cos(theta[frame]) * np.cos(i * 2 * np.pi / num_points)
        y = 0.5 + weight * np.cos(theta[frame]) * np.sin(i * 2 * np.pi / num_points)
        ax.plot(x, y, 'o', markersize=radius * 2, color='white')
    return

# Animate the points
ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init, interval=1000 / frame_rate, blit=False)

plt.show()
