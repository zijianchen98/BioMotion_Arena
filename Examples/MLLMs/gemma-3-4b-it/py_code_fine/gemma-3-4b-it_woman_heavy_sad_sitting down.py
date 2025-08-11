
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_sad_woman_sitting_down_animation(duration=10, fps=30):
    """
    Generates a point-light animation of a sad woman sitting down.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): Frames per second.

    Returns:
        matplotlib.animation.FuncAnimation: The animation object.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)

    points = 15
    lights = []
    for i in range(points):
        light = plt.Point2D(np.random.normal(0, 1.5), np.random.normal(0, 1.5))
        lights.append(light)
    
    scat = ax.scatter([l[0] for l in lights], [l[1] for l in lights], s=50, c='white')


    def animate(frame):
        for i in range(points):
            # Simulate movement based on a simple sitting down motion
            lights[i][0] += np.sin(frame * 0.1) * 0.1  # Horizontal movement
            lights[i][1] += np.cos(frame * 0.1) * 0.1  # Vertical movement

        scat.set_offsets([l[0], l[1] for l in lights])
        return scat,

    ani = animation.FuncAnimation(fig, animate, frames=int(duration * fps), blit=True, repeat=True)
    return ani

if __name__ == '__main__':
    ani = generate_sad_woman_sitting_down_animation(duration=10, fps=30)
    ani.save("sad_woman_sitting_down.gif", writer='pillow', fps=30)  # Save as GIF
    plt.show()
