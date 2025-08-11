
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def sadman_turning_around_animation(duration=10, fps=30):
    """
    Generates an animation of a sadman turning around.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): Frames per second.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    points = 15
    light_positions = np.random.rand(points, 2) * 2 - 1  # Random positions within -1 to 1

    def update(frame):
        for i in range(points):
            light_positions[i, 0] = np.sin(2 * np.pi * frame / duration)
            light_positions[i, 1] = np.cos(2 * np.pi * frame / duration)
        
        for i in range(points):
            ax.plot(light_positions[i, 0], light_positions[i, 1], 'w', markersize=10)

        return light_positions

    ani = animation.FuncAnimation(fig, update, frames=int(duration * fps), blit=True, repeat=True)

    plt.show()

if __name__ == '__main__':
    sadman_turning_around_animation()
