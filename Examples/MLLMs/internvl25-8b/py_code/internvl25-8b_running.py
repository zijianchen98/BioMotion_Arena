
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

def init():
    line.set_data([], [])
    return (line,)

def frame(i):
    x = np.linspace(3, -3, 15)
    y = np.sin(2 * np.pi * (0.5 + i / 10) * np.hypot(1, 1) * np.linspace(-1, 1, 150))
    line.set_data(x, y)
    return (line,)

line, = ax.plot([], [], 'o', markersize=10)
ax.set_xlim([-4, 4])
ax.set_ylim([-1.5, 1.5])
ax.set_axis_off()

ani = animation.FuncAnimation(fig, frame, init_func=init, frames=100, interval=20, blit=True)
plt.show()
