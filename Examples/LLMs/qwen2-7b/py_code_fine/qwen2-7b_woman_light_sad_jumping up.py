
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot((autoscale_on=False,
xlim=(-5, 10), ylim=(-1, 10))
ax.set_aspect('equal')
ax.grid()

points = np.zeros((15, 2))
scat = ax.scatter(points[:, 0], points[:, 1])

def update(data):
    for i in range(15:
        if data == 'jumping up':
            points[i, 0] += np.random.normal(scale=0.1)
            points[i, 1] += np.random.normal(loc=0.1, scale=0.05)
        else:
            points[i, 0] += np.random.normal(scale=0.05)
            points[i, 1] -= np.random.normal(loc=0.1, scale=0.05)
    scat.set_offsets(points)
    return scat,

ani = animation.FuncAnimation(fig, update, interval=50, blit=True)

plt.show()
