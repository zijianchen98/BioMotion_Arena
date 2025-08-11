
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot((projection='3d', autoscale_on=False,
                       xlim=(-4, 4), ylim=(-4, 4), zlim=(-4, 4))

points = [np.array([0, 0, 0]), np.array([1, 1, 1]),
          np.array([-1, -1, 1]), np.array([1, -1, -1]),
          np.array([-1, 1, -1])]
points = np.array(points)

def update(num):
    if num % 2 == 0:
        points[0] += np.array([np.cos(num / 20 * np.pi), np.sin(num / 20 * np.pi), 0])
    else:
        points[0] += np.array([np.sin(num / 20 * np.pi), np.cos(num / 20 * np.pi), 0])
    ax.clear()
    ax.set_title('A happy woman with heavy weight is running')
    ax.set_xlabel('X ')
    ax.set_ylabel(' Y ')
    ax.set_zlabel(' Z ')
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_zlim(-4, 4)
    for i in range(points.shape[0]):
        ax.plot([points[i][0], points[(i + 1) % points.shape[0]][0]],
                [points[i][1], points[(i + 1) % points.shape[0]][1]],
                zs=[points[i][2], points[(i + 1) % points.shape[0]][2]], marker='o')

anim = FuncAnimation(fig, update, frames=np.arange((-100, 1000, 1), interval=5, repeat=False)
plt.show()

