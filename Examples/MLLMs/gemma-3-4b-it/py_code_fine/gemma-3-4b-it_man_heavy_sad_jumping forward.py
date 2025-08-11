
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_sadman_jump_animation(duration=10, fps=30):
    """
    Generates a point-light animation depicting a sadman jumping forward.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): The frames per second of the animation.

    Returns:
        matplotlib.animation.FuncAnimation: The animation object.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    
    points = 15
    
    # Define the points
    xs = np.random.uniform(low=-0.8, high=0.8, size=points)
    ys = np.random.uniform(low=-0.8, high=0.8, size=points)
    zs = np.random.uniform(low=-0.5, high=0.5, size=points)  # Lower Z for depth

    # Initialize the point lights
    points_lights = ax.scatter(xs, ys, zs, s=20, c='white')

    def animate(frame):
        # Simulate jumping motion
        for i in range(points):
            # Simple forward jump simulation
            xs[i] += 0.02 * np.sin(frame * 2 * np.pi)
            ys[i] += 0.01 * np.cos(frame * 2 * np.pi)
            zs[i] += 0.01  # Slight upward movement

        points_lights.set_offsets(np.c_[xs, ys, zs])
        return points_lights

    ani = animation.FuncAnimation(fig, animate, frames=int(duration * fps), blit=True, repeat=True)
    return ani

if __name__ == '__main__':
    ani = generate_sadman_jump_animation(duration=5, fps=20)
    ani.save("sadman_jump.gif", writer='pillow', fps=20)  # Save as GIF
    plt.show()
