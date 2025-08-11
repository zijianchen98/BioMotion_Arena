
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_jump(subject='sadman', action='jumping forward', duration=50):
    fig, ax = plt.subplots()
    ax.set_xlim((-100, 100)
    ax.set_ylim((-100, 100))
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Set up the subject's and action labels
    label_text = f'{subject} {action}'
    ax.text((-80, -90, label_text, ha='center', va='center', color='white')

    # Create the initial position of the points
    points = np.random.rand((15, 2) * 200 - 100
    points = points / 100 * 200 - 100

    def update(frame):
        global points
        new_points = np.copy(points)

        for i, p in enumerate(new_points):
            if frame % 2 == 0:
                # Simulate jumping forward
                p[0] += 0.5
            else:
                # Simulate landing
                p[0] -= 0.2
            p[1] += 0.1

        points = new_points

        ax.clear()
        ax.set_xlim(-100, 100)
        ax.set_ylim(-100, 100)
        ax.set_aspect('equal')
        ax.set_facecolor('black')

        ax.scatter(points[:, 0], points[:, 1], s=10, c='white')

    ani = FuncAnimation(fig, update, frames=np.arange(0, duration), interval=20)
    plt.show()

animate_jump()
