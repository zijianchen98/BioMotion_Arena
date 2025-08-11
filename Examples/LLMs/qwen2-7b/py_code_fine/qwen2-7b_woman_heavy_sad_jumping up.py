
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot( (autoscale_on=False,
xlim=(-50, 150),
ylim=(-50, 150))
ax.set_aspect('equal')

# The subject
sadwoman = plt.Circle((40, 80), 10, color='w', fill=True)
ax.add_artist(sadwoman)

def init():
    sadwoman.center = (40, 80
    return sadwoman,

def animate(i):
    # Move the circle
    sadwoman.center = (40 + i * 0.5, 80 - i * 0.5
    return sadwoman,

ani = animation.FuncAnimation(fig, animate, frames=range((-150, 150),
init_func=init, blit=True, interval=20)

plt.show()
