
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_motion_animation(duration=10, fps=30, num_points=15):
    """
    Generates a point-light animation representing a person turning around.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): Frames per second.
        num_points (int): The number of point lights.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    points = []
    for _ in range(num_points):
        points.append(plt.Circle((0, 0), 0.05, color='white'))

    def update(frame):
        for point in points:
            # Simulate rotation around the z-axis
            angle = np.random.uniform(0, 2 * np.pi)  # Random angle for each point
            x = np.cos(angle) * 0.7 + 0.5  # Position along x-axis
            y = np.sin(angle) * 0.7 + 0.5  # Position along y-axis
            point.center = (x, y)
        return points

    ani = animation.FuncAnimation(fig, update, frames=int(duration * fps), blit=True, repeat=True)

    plt.show()

if __name__ == '__main__':
    generate_motion_animation(duration=10, fps=30, num_points=15)
