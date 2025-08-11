
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_sad_woman_waving_animation(duration=10, fps=30):
    """
    Generates a point-light animation of a sad woman waving her hand.

    Args:
        duration (int): Duration of the animation in seconds.
        fps (int): Frames per second.

    Returns:
        matplotlib.animation.FuncAnimation: The animation object.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis('off')

    points = np.random.rand(15, 2)  # Initial random positions for the points
    colors = 'white'
    sizes = 10  # Size of the points

    line, = ax.plot(points[:, 0], points[:, 1], 'w', markersize=sizes)

    def update(frame):
        # Simulate waving motion
        for i in range(15):
            # Simple waving motion based on frame number
            angle = np.sin(2 * np.pi * frame / duration) * np.pi / 4  # Wave amplitude
            x = points[i, 0] + sizes * np.cos(angle)
            y = points[i, 1] + sizes * np.sin(angle)
            points[i, 0] = x
            points[i, 1] = y
        
        line.set_data(points[:, 0], points[:, 1])
        return line,

    ani = animation.FuncAnimation(fig, update, frames=int(duration * fps), blit=True, repeat=True)
    return ani


if __name__ == '__main__':
    ani = generate_sad_woman_waving_animation()
    ani.save('sad_woman_waving.gif', writer='pillow', fps=15) # Save as GIF
    plt.show()
