
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
ax.set(xlim=(0, 10, 15), ylim=(-5, 5), aspect='auto')
ax.axis('off')

points = [ax.plot([], [], 'o', color='white') for _ in range(15)]
points_colors = ['white' for _ in range(15)]

def update_points(frame):
    for point, point_color in zip(points, points_colors):
        x = np.array([3, 3, 4.5, 5, 6, 6, 6, 7.5, 8, 7.5, 6, 4.5, 3, 2, 1.5, 1])
        y = np.array([1.2, 0.8, 0.4, 0.0, -0.4, -0.8, -1.2, -1.2, -1.2, -1.2, -1.2, -1.2, -1.6, -1.2, -0.8, 0])
        point[0].set_data(x + frame % 1, y)
        point[0].set_color(point_color)
    return points

ani = animation.FuncAnimation(fig, update_points, frames=30, interval=30, blit=True)
plt.show()
