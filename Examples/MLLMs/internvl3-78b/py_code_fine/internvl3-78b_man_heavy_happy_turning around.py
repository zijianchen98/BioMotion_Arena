
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.set_facecolor('black')

n_points = 15
points = [ax.plot([], [], 'wo')[0] for _ in range(n_points)]

def init():
    for point in points:
        point.set_data([], [])
    return points

def animate(i):
    center_x = 3 + 1.5 * np.cos(np.radians(i))
    center_y = 3
    angles = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
    x_points = center_x + 0.2 * np.cos(angles)
    y_points = center_y + 0.2 * np.sin(angles)
    for point, x, y in zip(points, x_points, y_points):
        point.set_data(x, y)
    return points

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=50, blit=True)
plt.show()
