
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_jumping_man_animation(duration=10, fps=30):
    """
    Generates a point-light animation of a man jumping forward.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): Frames per second.

    Returns:
        matplotlib.animation.FuncAnimation: The animation object.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 3)
    ax.set_aspect('equal')
    ax.axis('off')

    points = 15
    lights = []
    for _ in range(points):
        lights.append(plt.scatter([], [], s=100, color='white'))

    def animate(frame):
        # Simulate jumping motion
        time = frame / fps
        # Jump height and speed parameters
        jump_height = 1.5
        jump_speed = 10 * np.sin(time * 2 * np.pi)
        forward_speed = 2 * np.cos(time * 2 * np.pi)

        # Update positions of the lights
        for i in range(points):
            x = np.cos(i * np.pi / (points - 1)) * forward_speed * time
            y = np.sin(i * np.pi / (points - 1)) * forward_speed * time
            z = jump_speed * time
            lights[i].set_offsets(np.array([x, y, z]))
        return lights

    ani = animation.FuncAnimation(fig, animate, frames=int(duration * fps), blit=True, repeat=True)
    return ani

if __name__ == '__main__':
    ani = generate_jumping_man_animation()
    ani.save('jumping_man.gif', writer='pillow', fps=15)
    plt.show()
