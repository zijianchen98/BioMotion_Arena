
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_bowing_man():
    """
    Generates a point-light animation of a man bowing with heavy weight.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    points = np.array([
        [-0.8, -0.5],
        [-0.4, -0.8],
        [0.2, -0.6],
        [0.8, -0.4],
        [0.5, 0.3],
        [-0.5, 0.6],
        [-0.9, 0.8],
        [-0.3, 0.6],
        [0.3, 0.4],
        [0.9, 0.2],
        [0.2, 0.8],
        [-0.2, 0.8],
        [-0.7, 0.4],
        [-0.6, -0.2],
        [-0.5, -0.6]
    ])

    colors = ['white'] * len(points)

    line, = ax.plot(points[:, 0], points[:, 1], 'w', linewidth=2)

    def update(frame):
        """Updates the animation frame."""
        for i in range(len(points)):
            # Simulate bowing motion - this is a simplified model
            x = points[i, 0] + np.sin(frame * 0.1) * 0.2 
            y = points[i, 1] + np.cos(frame * 0.1) * 0.1 
            points[i, 0] = x
            points[i, 1] = y
            line.set_data(points[:, 0], points[:, 1])

        return line,

    ani = animation.FuncAnimation(fig, update, frames=30, blit=True, repeat=True)

    plt.show()

if __name__ == '__main__':
    animate_bowing_man()
