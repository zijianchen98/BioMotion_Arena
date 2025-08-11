
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def sad_woman_running_animation(duration=10, fps=30):
    """
    Generates an animation of a sad woman running, represented by 15 moving white points.

    Args:
        duration (int, optional): The duration of the animation in seconds. Defaults to 10.
        fps (int, optional): The frames per second. Defaults to 30.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    points = []
    for _ in range(15):
        points.append(plt.Circle((0, 0), 0.03, color='white'))  # Adjust radius for desired size

    def animate(frame):
        for point in points:
            # Simple running motion - adjust these parameters to change the movement
            x = np.sin(2 * np.pi * frame / fps) * 0.5  # Sine wave for horizontal movement
            y = np.cos(2 * np.pi * frame / fps) * 0.5  # Cosine wave for vertical movement
            point.center = (x, y)
        return points

    ani = animation.FuncAnimation(fig, animate, frames=int(duration * fps), blit=True, repeat=True)

    plt.show()

if __name__ == '__main__':
    sad_woman_running_animation()
