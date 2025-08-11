
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_sadman_walking_animation(duration=10, fps=30):
    """
    Generates a point-light animation of a sadman walking.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): The frames per second of the animation.
    """

    # Define the number of frames
    num_frames = int(duration * fps)

    # Initialize the figure and axes
    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    # Define the point lights
    num_lights = 15
    lights = []
    for i in range(num_lights):
        x = np.random.uniform(-0.8, 0.8)
        y = np.random.uniform(-0.8, 0.8)
        z = 0  # Initial z-coordinate
        lights.append([x, y, z])

    # Define the walking motion parameters
    walk_speed = 0.02
    step_height = 0.1
    step_duration = 0.5

    # Animation function
    def animate(frame):
        for i in range(num_lights):
            # Update the position of each light based on the walking motion
            lights[i][0] += walk_speed * np.sin(frame * 2 * np.pi)
            lights[i][1] -= walk_speed * np.cos(frame * 2 * np.pi)
            lights[i][2] += step_height * np.sin((frame % step_duration) * 2 * np.pi)  # Simulate a step

        # Plot the lights
        for light in lights:
            ax.plot(light[0], light[1], 'w', markersize=10)

        return lights

    # Create the animation
    ani = animation.FuncAnimation(fig, animate, frames=num_frames, repeat=True)

    # Save the animation as a GIF
    ani.save('sadman_walking.gif', writer='pillow', fps=fps)

    plt.show()


if __name__ == '__main__':
    generate_sadman_walking_animation()
