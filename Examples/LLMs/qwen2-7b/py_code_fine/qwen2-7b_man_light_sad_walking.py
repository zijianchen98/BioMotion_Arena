
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot( ( autoscale_on=False,
xlim=(-50, 100), ylim=(-50, 100))
ax.set_facecolor('black')

points = np.zeros((15, 2))

def animate(i):
    global points
    for j in range(15:
        angle = 2 * np.pi * i / 15 + 2 * np.pi * j / 15
        points[j] = ( 5 * np.cos(angle),  5 * np.sin(angle)
    ax.scatter(points[:,0], points[:,1], color='white')
    return [ax]

ani = animation.FuncAnimation(fig, animate, interval=50)
plt.show()

