
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_waving_hand():
    """
    Generates an animation of a sadwoman waving a hand using 15 white point-lights 
    against a black background, aiming for biomechanically plausible motion.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    points = []
    for _ in range(15):
        points.append(plt.Circle((0, 0), radius=0.03, color='white'))

    def update(frame):
        for i, point in enumerate(points):
            angle = np.linspace(0, 2 * np.pi, 100)[frame]
            x = 0.5 * np.cos(angle)
            y = 0.5 * np.sin(angle)
            point.center = (x, y)
        return points

    ani = animation.FuncAnimation(fig, update, frames=30, blit=True, repeat=True)

    plt.show()

if __name__ == '__main__':
    animate_waving_hand()
