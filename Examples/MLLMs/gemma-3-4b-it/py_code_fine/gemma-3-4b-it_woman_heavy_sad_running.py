
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_sad_woman_running_animation(duration=10, fps=30):
    """
    Generates a point-light animation depicting a sadwoman running.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): The frames per second of the animation.
    """

    # Define the number of points
    num_points = 15

    # Create a figure and axes
    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    # Create the point-lights
    points = plt.scatter(np.random.rand(num_points), np.random.rand(num_points), s=50, color='white')

    # Define the motion parameters
    x_speed = 0.02
    y_speed = 0.03
    z_speed = 0.01  # Add z-motion for depth perception

    def update(frame):
        """
        Updates the position of the point-lights for each frame.
        """
        for i in range(num_points):
            # Generate random initial positions
            x = np.random.rand()
            y = np.random.rand()
            z = np.random.rand()

            # Update the position of the point-light
            points[i].set_position((x * (frame / duration) + x_speed * frame,
                                    y * (frame / duration) + y_speed * frame,
                                    z * (frame / duration) + z_speed * frame))

        return points

    # Create the animation
    ani = animation.FuncAnimation(fig, update, frames=int(duration * fps), blit=True, repeat=True)

    # Save the animation
    ani.save("sad_woman_running.gif", writer='pillow', fps=fps)

    plt.close(fig)  # Close the figure to release memory

if __name__ == '__main__':
    generate_sad_woman_running_animation()
