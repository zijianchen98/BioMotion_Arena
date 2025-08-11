
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_running_animation(duration=10, fps=30):
    """
    Generates a point-light animation representing a running woman.

    Args:
        duration (int): Duration of the animation in seconds.
        fps (int): Frames per second.

    Returns:
        matplotlib.animation.FuncAnimation: The animation object.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_aspect('equal')
    ax.axis('off')

    points = np.random.rand(15, 2)  # 15 random points initially

    def update(frame):
        for i in range(15):
            # Simulate running motion (simplified)
            points[i, 0] += 0.05 * np.sin(frame * 2)
            points[i, 1] += 0.02 * np.cos(frame * 3)

            # Keep points within the bounds
            points[i, 0] = np.clip(points[i, 0], -1, 1)
            points[i, 1] = np.clip(points[i, 1], -1, 1)

        ax.clear()
        ax.set_facecolor('black')
        ax.scatter(points[:, 0], points[:, 1], s=50, color='white')
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.set_aspect('equal')
        ax.axis('off')
        return points,

    ani = animation.FuncAnimation(fig, update, frames=int(duration * fps), blit=True, repeat=True)
    return ani

if __name__ == '__main__':
    ani = generate_running_animation()
    ani.save('running_woman.gif', writer='pillow', fps=15) # save as gif
    plt.show()
