
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_sitting_down_animation(duration=10, fps=30):
    """
    Generates a point-light animation of a man sitting down.

    Args:
        duration (int): The duration of the animation in seconds.
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
        # Create a random position for the point light
        x = np.random.uniform(-8, 8)
        y = np.random.uniform(-8, 8)
        points.append([x, y])

    # Initialize the line
    line, = ax.plot([], [], 'w.', markersize=10)

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        # Update the positions of the points
        x_data = [p[0] for p in points]
        y_data = [p[1] for p in points]
        line.set_data(x_data, y_data)
        
        # Simulate the sitting down motion
        for p in points:
            # Simple animation of movement downwards and slightly inwards
            p[1] -= 0.05 * np.sin(i * 0.1)
            p[0] -= 0.01 * np.cos(i * 0.1) 
        
        return line,

    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=int(duration * fps), blit=True, repeat=True)
    return ani

if __name__ == '__main__':
    ani = generate_sitting_down_animation()
    ani.save("sitting_down.gif", writer='pillow', fps=15)
    plt.show()
