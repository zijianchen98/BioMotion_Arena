
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_bowing_animation(duration=10, fps=30):
    """
    Generates a point-light animation representing a bowing action.

    Args:
        duration (int): Duration of the animation in seconds.
        fps (int): Frames per second of the animation.

    Returns:
        matplotlib.animation.FuncAnimation: The animation object.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_aspect('equal')
    ax.axis('off')

    points = np.random.rand(15, 2) * 20 - 10  # Random initial positions

    def update(frame):
        """Updates the positions of the points for each frame."""
        for i in range(15):
            # Bowing motion:  Simple sinusoidal motion
            points[i, 0] = 5 * np.sin(np.pi * frame / duration) + 5
            points[i, 1] = 2 * frame / duration  # Vertical movement
        return points

    ani = animation.FuncAnimation(fig, update, frames=int(duration * fps), blit=True, repeat=True)
    return ani


if __name__ == '__main__':
    ani = create_bowing_animation()
    ani.save("bowing_animation.gif", writer='pillow', fps=15) #Save as gif.
    plt.show()
