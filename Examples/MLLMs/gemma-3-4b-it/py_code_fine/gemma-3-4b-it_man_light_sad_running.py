
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_sadman_running_animation(duration=10, frame_rate=30):
    """
    Generates a point-light animation of a sadman running.

    Args:
        duration (int): The duration of the animation in seconds.
        frame_rate (int): The number of frames per second.

    Returns:
        matplotlib.animation.FuncAnimation: The animation object.
    """

    fig, ax = plt.subplots()
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])

    points = []
    for i in range(15):
        # Generate random positions for the points
        x = np.random.uniform(-3, 3)
        y = np.random.uniform(-3, 3)
        points.append([x, y])

    light_points, = ax.plot(points[0][0], points[0][1], 'w', markersize=10)

    def animate(frame):
        # Update the positions of the points for a more realistic animation
        for i in range(15):
            x = points[i][0] + np.sin(frame * 0.1) * 0.5 * (3 - np.abs(points[i][0]))
            y = points[i][1] + np.cos(frame * 0.1) * 0.5 * (3 - np.abs(points[i][1]))
            points[i] = [x, y]
            light_points.set_data(x, y)
        return light_points,

    ani = animation.FuncAnimation(fig, animate, frames=int(duration * frame_rate), blit=True, repeat=True)
    return ani

if __name__ == '__main__':
    ani = generate_sadman_running_animation()
    ani.save("sadman_running.gif", writer='pillow', fps=15)  # Save as GIF
    plt.show()
