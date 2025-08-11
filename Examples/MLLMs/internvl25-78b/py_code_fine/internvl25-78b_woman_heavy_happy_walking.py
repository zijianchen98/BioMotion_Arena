
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')

# Generate initial points
points = np.random.rand(num_points, 2) * 10

# Create a scatter plot
sc = ax.scatter(points[:, 0], points[:, 1], color='white')

def update_points(num):
    # Update positions to simulate walking
    x = points[:, 0] + 0.1 * np.sin(num / 10.0)
    y = points[:, 1] + 0.1 * np.cos(num / 10.0)
    sc.set_offsets(np.c_[x, y])
    return sc,

# Create animation
ani = animation.FuncAnimation(fig, update_points, frames=100, interval=50, blit=True)

plt.show()
