
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_sad_woman_motion():
    """
    Generates a point-light animation representing a sad woman lying down.

    Returns:
        matplotlib.animation.FuncAnimation: The animation object.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    points = np.random.rand(15, 2)  # 15 random points
    colors = 'white'
    sizes = 50  # Size of each point

    scat = ax.scatter(points[:, 0], points[:, 1], s=sizes, c=colors, marker='o')

    def update(frame):
        """Updates the scatter plot for each frame of the animation."""
        # Simulate realistic motion for a lying down action
        for i in range(15):
            # Simple sine wave motion for each point
            points[i, 0] += np.sin(frame * 0.1 + i * 0.05) * 0.2
            points[i, 1] += np.cos(frame * 0.1 + i * 0.05) * 0.15
        scat.set_offsets(points)
        return scat

    ani = animation.FuncAnimation(fig, update, frames=30, blit=True, repeat=True)
    return ani


if __name__ == '__main__':
    ani = generate_sad_woman_motion()
    plt.show()
