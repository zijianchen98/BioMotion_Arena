
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')

# Create a white point-light stimulus array
num_points = 15
point_size = 0.1
points = np.empty((num_points, 2))
points[:, 0] = np.cos(np.linspace(0, 2 * np.pi, num_points) * 0.5)
points[:, 1] = np.sin(np.linspace(0, 2 * np.pi, num_points) * 0.5)

# Function to update the positions of the points
def update(frame):
    for i in range(num_points):
        x, y = points[i]
        angle = frame * 0.05 + np.pi / 2
        points[i] = np.array([x * np.cos(angle) - y * np.sin(angle),
                              x * np.sin(angle) + y * np.cos(angle)])
    
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    for i in range(num_points):
        ax.plot(points[i, 0], points[i, 1], 'o', color='white', markersize=point_size)
    return ax

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(60), interval=50, repeat=False)

plt.show()
