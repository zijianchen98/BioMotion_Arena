
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_bowing_animation(duration=10, fps=30):
    """
    Generates a point-light animation of a woman bowing with a heavy weight.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): The frames per second of the animation.
    """

    # Define the number of points
    num_points = 15

    # Define the positions of the points (simple sinusoidal motion for demonstration)
    t = np.linspace(0, duration, int(duration * fps), endpoint=False)
    x = 1 + 0.5 * np.sin(2 * np.pi * t)
    y = 0.5 * np.sin(2 * np.pi * t)
    z = 0.5 * np.cos(2 * np.pi * t)  # Add a z component for 3D effect

    # Create the figure and axes
    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-0.5, 0.5)  # Set z-axis limits for better visualization
    ax.view_init(elev=30, azim=30)  # Adjust viewing angle for a better perspective

    # Create the points
    points, = ax.plot([], [], 'w.', markersize=10)

    # Animation function
    def animate(i):
        points.set_data(x[i], y[i])
        return points,

    # Create the animation
    ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=10, blit=True, repeat=True)

    # Save the animation as a GIF
    ani.save('bowing_animation.gif', writer='pillow', fps=fps)  # Use pillow writer for GIF

    plt.close(fig)


if __name__ == '__main__':
    generate_bowing_animation()
