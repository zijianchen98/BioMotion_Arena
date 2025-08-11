
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Initialize the figure and plot
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
points, = ax.plot([], [], 'o', markersize=1)

# Define the initial positions of the points
center_x, center_y = 0, 0
radius = 2
initial_points = np.random.uniform(-1, 1, (num_points, 2)) + [center_x, center_y]

# Define the update function for the animation
def update(frame):
    # Update the positions of the points
    positions = [point + radius * np.cos(2 * np.pi * (frame / 20 + np.random.rand())) * np.array([np.cos(np.pi * frame / 40), np.sin(np.pi * frame / 40)])
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), blit=True)
plt.axis('off')
plt.show()
