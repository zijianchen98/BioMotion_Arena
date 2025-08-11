
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_running_animation(duration=5, fps=30):
    """
    Generates a point-light animation of a man running.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): Frames per second of the animation.
    """

    # Define the number of points representing the body
    num_points = 15

    # Define the trajectory of the points (simplified running motion)
    # This is a simplified representation of running motion. More complex models could be used
    # for increased realism.
    trajectory = np.array([
        [0, 0],
        [10, 0],
        [20, 5],
        [30, 10],
        [40, 15],
        [50, 10],
        [60, 5],
        [70, 0],
        [80, 0],
        [90, -5],
        [100, -10],
        [110, -15],
        [120, -10],
        [130, -5],
        [140, 0]
    ])

    # Create the figure and axes
    fig, ax = plt.subplots()
    ax.set_xlim(-5, 150)
    ax.set_ylim(-20, 20)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    ax.axis('off')

    # Create the point-lights
    points, = ax.plot([], [], 'w.', markersize=10)  # White points

    # Animation function
    def animate(i):
        x = trajectory[:i+1, 0]
        y = trajectory[:i+1, 1]
        points.set_data(x, y)
        return points,

    # Create the animation
    ani = animation.FuncAnimation(fig, animate, frames=int(duration * fps), blit=True, repeat=True)

    # Save the animation (optional)
    # ani.save("running_animation.gif", writer='pillow', fps=fps) 

    plt.show()


if __name__ == '__main__':
    generate_running_animation()
