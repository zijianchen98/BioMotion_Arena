
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_jumping_animation(duration=10, fps=30):
    """
    Generates a point-light animation of a happy woman jumping forward.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): The frames per second.

    Returns:
        matplotlib.animation.FuncAnimation: The animation object.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 2)
    ax.set_aspect('equal')
    ax.axis('off')

    points = []
    for i in range(15):
        points.append(plt.scatter(0, 0, s=50, color='white'))

    def animate(frame):
        for i, point in enumerate(points):
            # Simulate jumping motion - sine wave for vertical movement
            y = np.sin(2 * np.pi * frame / fps) * 1.2  # Amplitude of 1.2 for jumping
            point.set_offsets([0, y])
        return points

    ani = animation.FuncAnimation(fig, animate, frames=int(duration * fps), blit=True, repeat=True)
    return ani

if __name__ == '__main__':
    jumping_animation = generate_jumping_animation()
    jumping_animation.save('jumping_animation.gif', writer='pillow', fps=15)
    plt.show()
