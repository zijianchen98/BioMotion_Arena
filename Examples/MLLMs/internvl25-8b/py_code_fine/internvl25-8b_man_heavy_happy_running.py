
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
n_points = 15
duration = 2.0
freq = 30
radius = 0.1

fig = plt.figure()
ax = fig.add_subplot(111, xlim=(-duration, duration), ylim=(-duration, duration))
ax.set_xticks(np.arange(-duration, duration, 0.2))
ax.set_yticks(np.arange(-duration, duration, 0.2))

points, = ax.plot([], [], 'o', color='w')

def initializer():
    points.set_data([], [])
    return points,

def animate(i):
    xs = np.linspace(-0.1, 0.1, n_points) + i/10
    ys = np.sin(xs) * radius
    points.set_data(xs, ys)
    return points,

anim = animation.FuncAnimation(fig, animate, np.arange(0, duration, 1/freq), 
                                init_func=initializer, blit=True, repeat=False)

plt.axis('off')
plt.show()
