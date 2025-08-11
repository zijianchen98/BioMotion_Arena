
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_sitting_down():
    """
    Generates an animation of a man sitting down using point-lights.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)

    points = []
    for i in range(15):
        angle = np.random.uniform(0, 2 * np.pi)
        radius = np.random.uniform(1, 3)
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        points.append([x, y])

    light_points, = ax.plot(points[0][0], points[0][1], 'w', markersize=10)

    def init():
        light_points.set_data(points[0][0], points[0][1])
        return light_points,

    def animate(i):
        light_points.set_data(points[i % 15][0], points[i % 15][1])
        return light_points,

    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=30, interval=50, blit=True, repeat=True)

    plt.show()

if __name__ == '__main__':
    animate_sitting_down()
