
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def init():
    for point in points:
        point.set_data([], [])
    return points

def update(frame):
    x = np.zeros(15)
    y = np.zeros(15)
    
    x[0] = np.sin(frame / 10.0) * 2
    y[0] = np.cos(frame / 10.0) * 2

    x[1:4] = x[0] + 0.5 * np.cos(np.linspace(0, 2*np.pi, 3) + frame / 10.0)
    y[1:4] = y[0] + 0.5 * np.sin(np.linspace(0, 2*np.pi, 3) + frame / 10.0)

    x[4:7] = x[0] - 0.5 * np.cos(np.linspace(0, 2*np.pi, 3) + frame / 10.0)
    y[4:7] = y[0] - 0.5 * np.sin(np.linspace(0, 2*np.pi, 3) + frame / 10.0)

    x[7:10] = x[0] + 0.8 * np.cos(np.linspace(0, 2*np.pi, 3) + frame / 10.0)
    y[7:10] = y[0] + 0.8 * np.sin(np.linspace(0, 2*np.pi, 3) + frame / 10.0)

    x[10:13] = x[0] - 0.8 * np.cos(np.linspace(0, 2*np.pi, 3) + frame / 10.0)
    y[10:13] = y[0] - 0.8 * np.sin(np.linspace(0, 2*np.pi, 3) + frame / 10.0)

    x[13] = x[0] + 1.0
    y[13] = y[0] + 1.0 * np.sin(frame / 10.0)

    x[14] = x[0] - 1.0
    y[14] = y[0] + 1.0 * np.sin(frame / 10.0)

    for i, point in enumerate(points):
        point.set_data(x[i], y[i])
    return points

fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)

points = [ax.plot([], [], 'wo')[0] for _ in range(15)]

ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init, blit=True)

plt.show()
