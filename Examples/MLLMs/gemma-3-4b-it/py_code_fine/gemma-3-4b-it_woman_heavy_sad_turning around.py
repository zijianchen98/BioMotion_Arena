
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_sad_woman_turning_around_animation(duration=10, fps=30):
    """
    Generates a point-light animation representing a sad woman turning around.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): Frames per second of the animation.
    """

    num_frames = int(duration * fps)
    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.set_aspect('equal')
    ax.axis('off')

    points = []
    for i in range(15):
        angle = i * 20  # Varying angles for a more natural look
        x = np.cos(np.radians(angle)) * 50
        y = np.sin(np.radians(angle)) * 50
        z = 0  # Keep points on the xy plane
        points.append([x, y, z])

    light = Light(points, color='white')

    ani = animation.FuncAnimation(fig, light.update, frames=num_frames, blit=True, repeat=True)

    plt.show()


class Light:
    def __init__(self, points, color='white'):
        self.points = points
        self.color = color

    def update(self, frame):
        # Simulate rotation around the z-axis
        for i in range(len(self.points)):
            # Simple rotation, can be improved with more sophisticated animation
            self.points[i][0] = 50 * np.cos(np.radians(frame * 360 / 10))
            self.points[i][1] = 50 * np.sin(np.radians(frame * 360 / 10))


if __name__ == '__main__':
    generate_sad_woman_turning_around_animation(duration=10, fps=30)
