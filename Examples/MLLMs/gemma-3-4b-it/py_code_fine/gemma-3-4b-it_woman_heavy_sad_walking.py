
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def sad_woman_walking_animation(duration=10, fps=30):
    """
    Generates a point-light animation of a sad woman walking with a heavy weight.

    Args:
        duration (int): Duration of the animation in seconds.
        fps (int): Frames per second.
    """

    # Define the number of points
    num_points = 15

    # Create a figure and axes
    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    # Create the point-lights
    points = plt.scatter([], [], s=200, c='white')

    # Define the walking motion parameters
    phase = 0
    amplitude = 0.3
    frequency = 0.1
    x_offset = 0.5
    y_offset = 0.2

    # Define the walking animation function
    def animate(frame):
        nonlocal phase
        phase += frequency

        # Calculate the positions of the points
        x_positions = [x_offset + amplitude * np.sin(frequency * phase) for _ in range(num_points)]
        y_positions = [y_offset + 0.2 * np.sin(frequency * phase) for _ in range(num_points)]
        
        # Update the point positions
        points.set_offsets(np.column_stack((x_positions, y_positions)))

        return points,

    # Create the animation
    ani = animation.FuncAnimation(fig, animate, frames=int(duration * fps), blit=True, repeat=True)

    # Save the animation (optional)
    # ani.save("sad_woman_walking.gif", writer='pillow', fps=fps)

    plt.show()

if __name__ == '__main__':
    sad_woman_walking_animation()
