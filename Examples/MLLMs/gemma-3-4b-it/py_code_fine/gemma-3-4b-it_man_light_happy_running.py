
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_running_animation(duration=10, fps=30):
    """
    Generates a point-light animation representing a running man.

    Args:
        duration (int): Duration of the animation in seconds.
        fps (int): Frames per second of the animation.

    Returns:
        matplotlib.animation.FuncAnimation: The animation object.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    points = []
    for _ in range(15):
        angle = np.random.uniform(0, 2 * np.pi)
        radius = np.random.uniform(0.3, 0.7)
        points.append((radius * np.cos(angle), radius * np.sin(angle)))

    light_sources = points

    def update(frame):
        for i, light in enumerate(light_sources):
            x, y = light
            # Simulate running motion
            x += np.sin(frame * 2) * 0.5  # Simple sinusoidal movement
            y += np.cos(frame * 2) * 0.5  # Simple sinusoidal movement
            light_sources[i] = (x, y)

        ax.clear()
        ax.set_facecolor('black')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.scatter(*zip(*light_sources), s=50, c='white')  # Adjust size as needed

        return light_sources

    ani = animation.FuncAnimation(fig, update, frames=int(duration * fps), blit=False)
    return ani

if __name__ == '__main__':
    ani = generate_running_animation()
    ani.save("running_animation.gif", writer='pillow', fps=15) #save as gif for quality.
    plt.show()
