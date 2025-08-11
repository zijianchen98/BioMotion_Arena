
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot( (autoscale_on=False,
xlim=(-50, 100), ylim=(-10, 60))
ax.set_aspect('equal')
x = np.zeros( (15)
y = 50 * np.ones( (15)

def animate(i):
    global x, y
    dx = 2 if i % 2 == 0 else -2
    x += dx
    y -= 1
    for i in range( (15):
        if x[i] < -50:
            x[i] = 100
        elif x[i] > 100:
            x[i] = -50
    return x, y

ani = animation.FuncAnimation(fig, animate, interval=50, blit=True)
plt.show()

