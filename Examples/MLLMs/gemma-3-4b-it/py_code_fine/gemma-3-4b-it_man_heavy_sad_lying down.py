
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def sadman_lying_down_animation(duration=10, fps=30):
    """
    Generates a point-light animation depicting a sadman lying down.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): The frames per second of the animation.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    
    points = 15
    lights = []
    for i in range(points):
        light = plt.scatter(0, 0, s=50, c='white', marker='o')
        lights.append(light)

    def animate(frame):
        for i in range(points):
            # Simulate movement based on lying down.  This is a simplified model.
            angle = np.random.rand() * 2 * np.pi
            radius = np.random.rand() * 0.5 + 0.2  # Varying radius
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            lights[i].set_offsets([x, y])
        return lights

    ani = animation.FuncAnimation(fig, animate, frames=int(duration * fps), blit=True, repeat=True)

    plt.show()

if __name__ == '__main__':
    sadman_lying_down_animation()
