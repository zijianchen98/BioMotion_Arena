
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_walking_animation(duration=10):
    """
    Generates a point-light animation of a walking man with a heavy weight.

    Args:
        duration (int): Duration of the animation in seconds.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    points = 15
    lights = []
    for _ in range(points):
        lights.append(plt.scatter([], [], s=50, color='white'))

    def animate(frame):
        for i in range(points):
            # Define a simple walking trajectory for each light
            x = np.sin(2 * np.pi * frame / duration * 2) * 0.7  # Sinusoidal movement
            y = np.cos(2 * np.pi * frame / duration * 2) * 0.7  # Cosinusoidal movement
            z = 0.2  # Adjust height to represent the weight

            lights[i].set_offsets(np.array([x, y, z]))

        return lights

    ani = animation.FuncAnimation(fig, animate, frames=int(duration * 30), blit=True, repeat=True)

    plt.show()

if __name__ == '__main__':
    generate_walking_animation()
