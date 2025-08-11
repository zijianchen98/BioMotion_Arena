
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_sadman_jump_animation(duration=10, fps=30):
    """
    Generates a point-light animation of a sadman jumping up.

    Args:
        duration (int): Duration of the animation in seconds.
        fps (int): Frames per second.

    Returns:
        matplotlib.animation.FuncAnimation: The animation object.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 10)
    ax.set_aspect('equal')
    ax.axis('off')

    num_frames = int(duration * fps)
    points = []

    for frame in range(num_frames):
        # Simulate jumping motion -  simple parabolic trajectory
        t = frame / fps
        x = np.sin(2 * np.pi * t) * 2  # Horizontal movement
        y = 2 * t**2 - 5 * t - 3  # Vertical movement (jumping up)

        # Create points
        for i in range(15):
            angle = (2 * np.pi * i) / 15
            x_point = x + np.cos(angle) * 1.5
            y_point = y + np.sin(angle) * 1.5
            points.append((x_point, y_point))

    lines, = ax.plot([], [], 'w.', markersize=10)

    def init():
        lines.set_data([], [])
        return lines,

    def animate(frame):
        x_data = [p[0] for p in points]
        y_data = [p[1] for p in points]
        lines.set_data(x_data, y_data)
        return lines,

    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=num_frames, blit=True, repeat=True)
    return ani


if __name__ == '__main__':
    ani = generate_sadman_jump_animation()
    plt.show()
