
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Set the axes limits and aspect ratio
ax.set_xlim((-10, 10))
ax.set_ylim((-10, 10))
ax.set_aspect('equal')

# Create 15 point-lights
points, = ax.plot([], [], 'o', color='white')

def update(num):
    # Update the point-lights positions
    x = np.sin(np.linspace(0, 2*np.pi, 15) + 0.01*num) * 10
    y = np.cos(np.linspace(0, 2*np.pi, 15) + 0.01*num) * 10
    points.set_data(x, y)
    return points,

ani = animation.FuncAnimation(fig, update, frames=1000, interval=50, blit=True)

plt.show()
