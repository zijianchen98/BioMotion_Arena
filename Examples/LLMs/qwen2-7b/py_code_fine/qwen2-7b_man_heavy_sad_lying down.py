
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot( ( autoscale_on=True )
ax.set_facecolor (.25 * np.ones ((3,)))

def init():
    global points
    points = np.zeros ((15, 2))
    for i in range ( ( 15):
        points[i] = [np.random.uniform ( ( - 1, 1), np.random.uniform ( ( - 1, 1)]
    return points,

def animate ( ( frame ):
    global points
    for i in range ( ( 15):
        points[i] += [0, - .1]
        if points[i][1] < - 1:
            points[i] = [np.random.uniform ( ( - 1, 1), np.random.uniform ( ( - 1, 1)]
    return points,

anim = animation.FuncAnimation(fig, animate, frames = 100, interval = 20, blit = True, init_func = init)

plt.show()
