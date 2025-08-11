
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_animation(duration=10, fps=30):
    """
    Generates a point-light animation depicting a woman lying down with a heavy weight.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): The frames per second of the animation.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1.5, 1.5])

    points = []
    for i in range(15):
        # Generate random positions and sizes for the points
        x = np.random.uniform(-0.8, 0.8)
        y = np.random.uniform(-0.8, 0.8)
        size = np.random.uniform(0.1, 0.3)
        points.append([x, y, size])

    # Create the light source (woman's head)
    head_x = 0
    head_y = 0
    head_size = 0.4
    points.append([head_x, head_y, head_size])

    # Create the weight
    weight_x = 0.5
    weight_y = -0.5
    weight_size = 0.6
    points.append([weight_x, weight_y, weight_size])

    # Initialize the light elements
    lights = []
    for x, y, size in points:
        light = ax.scatter(x, y, s=size * 200, color='white')
        lights.append(light)

    def animate(frame):
        """
        Animation function to update the positions of the points.
        """
        for i, (x, y, size) in enumerate(points):
            # Simulate realistic motion based on the lying down action
            x += np.random.normal(0, 0.03)
            y += np.random.normal(0, 0.03)
            size *= 0.99  # Slight size reduction over time

            lights[i].set_offsets([x, y])

        return lights

    ani = animation.FuncAnimation(fig, animate, frames=int(duration * fps), blit=True, repeat=True)

    plt.show()

if __name__ == '__main__':
    generate_animation()
