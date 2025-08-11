
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_sadman_motion_animation(duration=10, fps=30):
    """
    Generates an animation of a sadman lying down, represented by 15 moving white point lights.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): The frames per second of the animation.

    Returns:
        matplotlib.animation.Animation: The animation object.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.axis('off')

    points = []
    for _ in range(15):
        points.append(plt.Circle((0, 0), radius=0.02, color='white'))

    def animate(frame):
        for i, point in enumerate(points):
            # Simulate lying down motion with simple sinusoidal movements
            x = np.sin(2 * np.pi * frame / fps) * 0.5 + 0.25  # Horizontal movement
            y = np.cos(2 * np.pi * frame / fps) * 0.5 + 0.25  # Vertical movement
            point.center = (x, y)
        return points

    ani = animation.FuncAnimation(fig, animate, frames=int(duration * fps), blit=True, repeat=True)
    return ani

if __name__ == '__main__':
    ani = generate_sadman_motion_animation()
    ani.save("sadman_motion.gif", writer='pillow', fps=15)  # Save as GIF for demonstration
    plt.show()
