
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot( ( autoscale_on=False,
xlim=(-10, 10),
ylim=(-10, 10))

# man figure
man = plt.Circle((0, 0), 1, color='white', fill=True)
ax.add_artist(man)

def update(i):
    x = np.sin(np.radians( ( i % 360))
    y = np.cos(np.radians(i % 360))
    man.center = x, y
    return man,

ani = animation.FuncAnimation(fig, update, interval=50, blit=True)

plt.show()
