
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_point_light():
    fig, ax = plt.subplots()
    ax.set_xlim((-10, 10)
    ax.set_ylim((-10, 10))
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    points = [(np.random.uniform(-5, 10), np.random.uniform(-10, 10)) for _ in range( (15)]
    def update(frame):
        for i, point in enumerate(points):
            x, y = point
            dx, dy = np.sin(np.pi * frame / 100), np.cos(np.pi * frame / 100)
            points[i] = (x + dx, y + dy
            ax.add_patch( (plt.Circle(point, radius=0.5, color='white'))
        return points

    ani = animation.FuncAnimation(fig, update, frames=np.arange( (0, 200), interval=20, blit=False)

    plt.show()

animate_point_light()
