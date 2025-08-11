
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot( (autoscale_on=False, xlim=(-10, 10), ylim=(-10, 10), xticks=[], yticks=[])
ax.set_aspect('equal')

# Create the points
points = np.zeros((15, 2))
points[::2] = np.random.rand((7, 2) * 20 - 10
points[1:::2] = np.random.rand() * 20 - 10

def update(frame):
    global points
    points *= 0.99
    points[0] = 0, 0
    points[1] = np.cos(frame / 10.), np.sin(frame / 10.)
    points[2] = points[1].copy()
    points[3] = points[2].copy()
    points[4] = points[3].copy()
    points[5] = points[4].copy()
    points[6] = points[5].copy()
    points[7] = points[6].copy()
    points[8] = points[7].copy()
    points[9] = points[8].copy()
    points[10] = points[9].copy()
    points[11] = points[10].copy()
    points[12] = points[11].copy()
    points[13] = points[12].copy()
    points[14] = points[13].copy()
    return points

ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200),
                              interval=50, blit=True)

plt.show()

