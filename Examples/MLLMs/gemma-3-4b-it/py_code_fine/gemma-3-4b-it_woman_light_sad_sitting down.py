
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def sad_woman_sitting_down_animation(duration=10):
    """
    Generates a point-light animation depicting a sadwoman sitting down.

    Args:
        duration (int): The duration of the animation in seconds.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    
    points = []
    for i in range(15):
        angle = np.random.uniform(0, 2 * np.pi)
        radius = np.random.uniform(0.3, 0.7)
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        points.append((x, y))

    light_points, = ax.plot(points[0][0], points[0][1], 'w', markersize=10)

    def init():
        light_points.set_data(points[0][0], points[0][1])
        return light_points,

    def animate(i):
        light_points.set_data(points[i % len(points)][0], points[i % len(points)][1])
        return light_points,

    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=int(duration * 30), blit=True, repeat=True)
    plt.show()

if __name__ == '__main__':
    sad_woman_sitting_down_animation()
