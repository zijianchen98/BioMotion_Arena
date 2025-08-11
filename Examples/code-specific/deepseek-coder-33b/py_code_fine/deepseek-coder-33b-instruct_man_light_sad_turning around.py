
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a 15 point-lights
points = np.random.rand(15, 3)
scat = ax.scatter(points[:, 0], points[:, 1], points[:, 2])

# Set the axis limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

# Animation function
def animate(i):
    points = np.random.rand(15, 3)
    scat._offsets3d = (points[:, 0], points[:, 1], points[:, 2])
    return scat,

# Animate
ani = animation.FuncAnimation(fig, animate, frames=60, interval=50, blit=True)

plt.show()
