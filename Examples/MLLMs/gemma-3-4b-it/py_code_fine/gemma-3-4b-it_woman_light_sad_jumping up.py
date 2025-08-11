
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def generate_sad_woman_jump_animation(duration=5, fps=30):
    """
    Generates a point-light stimulus animation depicting a sad woman jumping up.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): Frames per second.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.set_aspect('equal')
    ax.axis('off')

    points = []
    for i in range(15):
        angle = np.random.uniform(0, 2 * np.pi)
        radius = np.random.uniform(10, 30)
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        points.append([x, y])

    light_points, = ax.plot(points[0][0], points[0][1], 'w', markersize=10)

    def animate(frame):
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            
            # Simulate jumping motion
            x = x + np.sin(frame * 2) * 5  # Added sine wave for jumping
            y = y + np.cos(frame * 3) * 3  # Added cosine wave for height change

            light_points.set_data(x, y)
        return light_points,

    ani = animation.FuncAnimation(fig, animate, frames=int(duration * fps), blit=True, repeat=True)

    plt.show()

if __name__ == '__main__':
    generate_sad_woman_jump_animation()
