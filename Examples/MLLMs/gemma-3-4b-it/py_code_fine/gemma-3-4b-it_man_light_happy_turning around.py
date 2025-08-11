
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_turning_around_animation(duration=10, fps=30):
    """
    Generates a point-light animation of a person turning around.

    Args:
        duration (int): Duration of the animation in seconds.
        fps (int): Frames per second.

    Returns:
        matplotlib.animation.FuncAnimation: The animation object.
    """

    fig, ax = plt.subplots()
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])

    points = []
    for i in range(15):
        angle = i * 2 * np.pi / 15
        x = np.cos(angle)
        y = np.sin(angle)
        points.append((x, y))

    light_points, = ax.plot(points, 'w.', markersize=10)

    def animate(frame):
        for i in range(len(points)):
            angle = (frame / fps) * 2 * np.pi
            x = np.cos(angle)
            y = np.sin(angle)
            points[i] = (x, y)
            light_points.set_data(points)
        return light_points,

    ani = animation.FuncAnimation(fig, animate, frames=int(duration * fps), blit=True, repeat=True)
    return ani

if __name__ == '__main__':
    ani = generate_turning_around_animation()
    ani.save('turning_around.gif', writer='pillow', fps=15)  # Save as GIF
    plt.show()
