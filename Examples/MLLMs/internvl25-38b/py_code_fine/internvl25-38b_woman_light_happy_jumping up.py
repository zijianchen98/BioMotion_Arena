
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def get_position(t):
    t = t % 100
    if t < 25:
        return np.array([1, 1.5 * np.sin(np.pi * t / 25), 0])
    elif t < 50:
        return np.array([1, -1.5 * np.sin(np.pi * (t - 25) / 25), 0])
    elif t < 75:
        return np.array([1, -1.5 * np.sin(np.pi * (t - 50) / 25), 0])
    else:
        return np.array([1, 1.5 * np.sin(np.pi * (t - 75) / 25), 0])

def update_points(num, points, line):
    for i in range(len(points)):
        points[i].set_data(get_position(num + i * 5)[:2])
    return points

fig, ax = plt.subplots()
ax.set_xlim(0, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

points = [plt.plot([], [], 'o', markersize=10)[0] for _ in range(15)]
line_ani = animation.FuncAnimation(fig, update_points, frames=100, fargs=(points, None), interval=50, blit=True)

plt.show()
