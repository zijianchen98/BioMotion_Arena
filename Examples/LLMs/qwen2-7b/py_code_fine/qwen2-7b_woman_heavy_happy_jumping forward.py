
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_point_light():
    fig, ax = plt.subplots()
    ax.set_xlim((-10, 10)
    ax.set_ylim((-10, 10))
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Subject and Action
    subject = 'happy woman with heavy weight'
    action = 'jumping forward'

    # Visual Style
    num_lights_points = 15
    light_points = np.random.uniform(-5, 10, (num_light_points, 2)

    def update(frame):
        light_points[:, 1] += 0.1 * np.sin(frame / 10)
        light_points[:, 0] += 0.1 * np.cos(frame / 10)
        for i, ( in enumerate(light_points):
            ax.scatter(*point, c='white', s=50)

    ani = FuncAnimation(fig, update, frames=np.arange(, interval=20, blit=False)
    plt.title(f'{subject} performing {action}')
    plt.show()

animate_point_light()
