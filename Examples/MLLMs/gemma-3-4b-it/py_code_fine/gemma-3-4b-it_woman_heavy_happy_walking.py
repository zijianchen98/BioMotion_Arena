
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_walking_animation(duration=10):
    """
    Generates a point-light animation of a woman walking.

    Args:
        duration (int): The duration of the animation in seconds.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    
    points = []
    for i in range(15):
        points.append(plt.Circle((0, 0), 0.02, color='white'))

    def animate(frame):
        for i, point in enumerate(points):
            # Define a walking trajectory (example) - can be adjusted for more complex motion
            x = np.sin(2 * np.pi * frame / duration) * 0.8  # Simple sine wave for x-coordinate
            y = np.cos(2 * np.pi * frame / duration) * 0.8  # Simple sine wave for y-coordinate
            point.center = (x, y)
        return points

    ani = animation.FuncAnimation(fig, animate, frames=duration * 30, blit=True, repeat=True)
    plt.show()

if __name__ == '__main__':
    generate_walking_animation()
