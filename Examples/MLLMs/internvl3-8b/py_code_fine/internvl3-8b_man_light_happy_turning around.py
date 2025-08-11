
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def update(frame):
    """Update the positions of the point-lights"""
    global points, ax, points_positions
    t = frame * 2 * np.pi / 30  # 30 frames per second
    points_positions = np.array([
        [np.cos(t * i), np.sin(t * i)] for i in range(15)
    ])
    for i in range(15):
        points[i].set_data(points_positions[i][:2])
    return points

fig, ax = plt.subplots()
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
points_positions = list()
points = list()
for i in range(15):
    point, = ax.plot([], [], 'o', color="white")
    points_positions.append([0, 0])  # starting position
    points.append(point)

ani = animation.FuncAnimation(fig, update, frames=300, interval=40, repeat=True)

plt.show()
