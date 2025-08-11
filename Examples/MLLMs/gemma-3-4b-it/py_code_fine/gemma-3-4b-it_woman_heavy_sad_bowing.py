
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_bowing_motion_animation(duration=10, fps=30):
    """
    Creates a point-light animation representing a sadwoman bowing with a heavy weight.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): Frames per second.

    Returns:
        matplotlib.animation.FuncAnimation: The animation object.
    """

    fig, ax = plt.subplots()
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    ax.axis('off')

    points = []
    for i in range(15):
        angle = np.random.uniform(0, 2 * np.pi)
        radius = np.random.uniform(0.5, 1.5)
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        points.append([x, y])

    light = []
    for i in range(15):
        light.append([1, 1, 1]) # White light

    scat = ax.scatter(points, light, s=50, c='white', marker='o')

    def animate(frame):
        for i in range(len(points)):
            angle = np.random.uniform(0, 2 * np.pi)
            radius = np.random.uniform(0.5, 1.5)
            points[i][0] = radius * np.cos(angle)
            points[i][1] = radius * np.sin(angle)
        
        scat.set_offsets(points)
        return scat,

    ani = animation.FuncAnimation(fig, animate, frames=int(duration * fps), blit=True, repeat=True)
    return ani

if __name__ == '__main__':
    ani = create_bowing_motion_animation()
    ani.save("bowing_motion.gif", writer='pillow', fps=15)
    plt.show()
