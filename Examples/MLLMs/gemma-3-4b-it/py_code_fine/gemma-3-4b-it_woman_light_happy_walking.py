
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_walking_animation(duration=10, fps=30):
    """
    Generates a point-light animation of a walking woman.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): Frames per second.
    """

    # Number of points
    num_points = 15

    # Calculate the number of frames
    num_frames = int(duration * fps)

    # Define the walking motion parameters
    phase = np.linspace(0, 2 * np.pi, num_frames)
    speed = 0.2  # Adjust for walking speed
    amplitude = 0.5  # Adjust for step height
    offset = 0.2  # Adjust for leg offset

    # Create the figure and axes
    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    # Initialize the lights
    lights = []
    for i in range(num_points):
        light = ax.scatter(0, 0, s=100, color='white')
        lights.append(light)

    # Animation function
    def animate(frame):
        for i in range(num_points):
            angle = phase[frame]
            x = np.cos(angle)
            y = np.sin(angle)
            z = amplitude * np.cos(angle + offset) 
            lights[i].set_offsets([x, y, z])

        return lights

    # Create the animation
    ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=True, repeat=True)

    # Save the animation
    ani.save("walking_woman.gif", writer='pillow', fps=fps)

    plt.show()


if __name__ == '__main__':
    generate_walking_animation()
