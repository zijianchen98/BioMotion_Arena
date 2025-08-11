
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_sadwoman_turning_around_animation(duration=10, frame_rate=30):
    """
    Generates a point-light animation of a sadwoman turning around.

    Args:
        duration (int): Duration of the animation in seconds.
        frame_rate (int): Frames per second.
    """

    num_frames = int(duration * frame_rate)
    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    
    points = []
    for i in range(15):
        angle = np.random.uniform(0, 2 * np.pi)
        radius = np.random.uniform(1, 3)  # Varying light size
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        points.append((x, y))

    light_sources = ax.scatter(points, color='white', s=100)


    def animate(frame):
        for i in range(len(points)):
            angle = np.random.uniform(0, 2 * np.pi)
            radius = np.random.uniform(1, 3)  # Varying light size
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            points[i] = (x, y)
        light_sources.set_offsets(points)
        return light_sources

    ani = animation.FuncAnimation(fig, animate, frames=num_frames, repeat=True, blit=True)

    plt.show()

if __name__ == '__main__':
    generate_sadwoman_turning_around_animation(duration=10, frame_rate=30)
