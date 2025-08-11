
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def happyman_bowing_animation():
    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    points = []
    for i in range(15):
        points.append(ax.plot([], [], 'o', color='white')[0])

    def init():
        for point in points:
            point.set_data([], [])
        return points

    def update(frame):
        for i, point in enumerate(points):
            x = np.cos(2 * np.pi * (frame + i) / 5)
            y = np.sin(2 * np.pi * (frame + i) / 5)
            point.set_data(x, y)
        return points

    anim = animation.FuncAnimation(fig, update, frames=range(120), init_func=init, blit=True, interval=30)
    plt.show()

happyman_bowing_animation()
