
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def create_animation():
    class PointLight:
        def __init__(self, num_points, x_init, y_init):
            self.num_points = num_points
            self.points = np.random.choice([0, 1, -1], (num_points, 2))
            self.points[:, 0] += x_init
            self.points[:, 1] += y_init

        def update(self, frame):
            self.points[:, 0] += 1
            self.points[:, 1] = np.sin(self.points[:, 0])

    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_facecolor('black')

    x_init, y_init = 0, 0
    point_light = PointLight(15, x_init, y_init)
    
    def init():
        ax.clear()
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_facecolor('black')

    def update(frame):
        point_light.update(frame)
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        for i in range(point_light.num_points):
            ax.plot(point_light.points[i, 0], point_light.points[i, 1], "o", color="w", markersize=6)
        return ax

    ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=50)
    plt.show()

create_animation()
