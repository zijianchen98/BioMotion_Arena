
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def bowing_animation():
    fig, ax = plt.subplots()
    ax.set_axis_off()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)

    def update(frame):
        global point_positions
        angle = frame * 0.4  # Angle of rotation in radians
        point_positions = np.array([[0, 0, 1],  # Head
                                   [0.5, 0.7, 1],
                                   [0.9, 0.1, 1],
                                   [0, -0.8, 1],
                                   [0.3, -0.25, 1],
                                   [0.7, -0.1, 1],
                                   [0.95, 0.15, 1],
                                   [0.1, -0.35, 1],
                                   [0.5, -0.9, 1],
                                   [0.9, -0.05, 1],
                                   [0.6, -0.6, 1],
                                   [-0.1, -0.85, 1],
                                   [-0.3, -0.25, 1],
                                   [0.7, -0.1, 1],
                                   [0.95, 0.15, 1]])
        point_positions[:, 1:] = np.around(np.dot(point_positions[:, :2], np.array([
            np.cos(angle), np.sin(angle), 0])) + np.array([0, 0, 0]))

        for idx, position in enumerate(point_positions):
            ax.plot([position[0]], [position[1]], 'o', c='w', ms=10)

    point_positions = np.array([[0, 0, 1],  # Head
                               [0.5, 0.7, 1],
                               [0.9, 0.1, 1],
                               [0, -0.8, 1],
                               [0.3, -0.25, 1],
                               [0.7, -0.1, 1],
                               [0.95, 0.15, 1],
                               [0.1, -0.35, 1],
                               [0.5, -0.9, 1],
                               [0.9, -0.05, 1],
                               [0.6, -0.6, 1],
                               [-0.1, -0.85, 1],
                               [-0.3, -0.25, 1],
                               [0.7, -0.1, 1],
                               [0.95, 0.15, 1]])

    ani = animation.FuncAnimation(fig, update, frames=range(-30, 31), interval=100, blit=True)
    plt.show()

bowing_animation()
