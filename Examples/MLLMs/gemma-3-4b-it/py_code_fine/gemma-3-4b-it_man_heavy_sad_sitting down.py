
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def sadman_sitting_down_animation(duration=10, fps=30):
    """
    Generates a point-light animation of a sadman sitting down.

    Args:
        duration (int): Duration of the animation in seconds.
        fps (int): Frames per second of the animation.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    points = 15
    lights = []
    for i in range(points):
        light = plt.scatter(0, 0, s=50, color='white', marker='o')
        lights.append(light)

    def animate(frame):
        for i in range(points):
            # Simulate the movement of the sadman sitting down
            # This is a simplified representation and can be adjusted
            # for more realistic movement
            x = np.sin(2 * np.pi * frame / fps) * 0.5 + 0.25
            y = np.sin(2 * np.pi * frame / fps) * 0.5 + 0.25
            z = np.cos(2 * np.pi * frame / fps) * 0.5 + 0.5

            lights[i].set_offsets( (x, y, z) )

        return lights

    ani = animation.FuncAnimation(fig, animate, frames=int(duration * fps), blit=True, repeat=True)

    plt.show()

if __name__ == '__main__':
    sadman_sitting_down_animation()
