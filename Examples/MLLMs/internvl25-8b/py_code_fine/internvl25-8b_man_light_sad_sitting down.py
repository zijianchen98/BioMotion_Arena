
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots(figsize=(6, 12))

points = [3, 5, 6, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20]
colors = "white"

def init():
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 12)
    for point in points:
        ax.plot((point, point), (0, 10), "o", color=colors, markersize=20)
    return [point.get_path() for point in points]

def animate(frame):
    for point in points:
        point.set_y(10 - 7 * np.sin(np.pi * frame / 60 * (point - 3) / 17))
    return [point.get_path() for point in points]

ani = animation.FuncAnimation(fig, animate, frames=60, init_func=init, blit=True)

plt.axis("off")
plt.xlim(0, 20)
plt.ylim(0, 12)
plt.show()
