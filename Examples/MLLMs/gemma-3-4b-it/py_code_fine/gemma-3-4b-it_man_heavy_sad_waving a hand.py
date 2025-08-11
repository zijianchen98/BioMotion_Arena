
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def sadman_waving_animation(duration=10, frame_rate=30):
    """
    Generates a point-light animation of a sadman waving a hand.

    Args:
        duration (int): The duration of the animation in seconds.
        frame_rate (int): The number of frames per second.
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
        points.append([x, y])

    scat = ax.scatter(points[:, 0], points[:, 1], s=50, c='white')

    def animate(frame):
        for i, point in enumerate(points):
            angle = np.random.uniform(0, 2 * np.pi)
            radius = np.random.uniform(0.3, 0.7)
            x = radius * np.cos(angle) + frame * 0.05  # Add some movement
            y = radius * np.sin(angle) + frame * 0.05 # Add some movement
            points[i] = [x, y]
            scat.set_offsets(points)
        return scat

    ani = animation.FuncAnimation(fig, animate, frames=int(duration * frame_rate), blit=True, repeat=True)

    plt.show()


if __name__ == '__main__':
    sadman_waving_animation()
