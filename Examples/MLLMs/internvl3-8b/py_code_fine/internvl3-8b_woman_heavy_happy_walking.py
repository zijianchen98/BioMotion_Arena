
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def get_walking_points(n_points=15):
    x = [-0.5, -0.5, -1, -1, 0, 0, -1, -1, -0.5, -0.5, -1, -1, -1, 0.5, -1]
    y = [0.5, 0.5, 0.5, 0, 0, 0.75, 1, 1.25, 1, 1, 0.75, 0.75, 1.25, 1, 0.75]
    x = x * n_points
    y = y * n_points
    x = np.append(x, np.zeros((n_points, n_points)))
    y = np.append(y, np.zeros((n_points, n_points)))
    return x, y

def animate(n):
    global xdata, ydata, line
    points = get_walking_points()
    xdata, ydata = points
    line.set_data(xdata[:n], ydata[:n])
    return line,

# Initial figure setup
fig, ax = plt.subplots()
line, = ax.plot([], [], 'bo', markersize=10)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 2)
ax.axis('off')

# Animation
n_points = 15
n_steps = 15 * n_points
ani = animation.FuncAnimation(
    fig, animate, n_steps, interval=50, blit=True, repeat=True
)

plt.show()
