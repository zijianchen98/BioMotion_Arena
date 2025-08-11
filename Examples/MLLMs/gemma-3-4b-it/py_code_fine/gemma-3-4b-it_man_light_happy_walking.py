
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_walking_animation(duration=10, fps=30):
    """
    Generates a point-light animation of a walking human.

    Args:
        duration (int): Duration of the animation in seconds.
        fps (int): Frames per second.
    """

    # Define the number of lights
    num_lights = 15

    # Create an empty figure and axes
    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_aspect('equal')
    ax.axis('off')

    # Create the lights
    lights = []
    for _ in range(num_lights):
        light = plt.Circle((0, 0), radius=0.03, color='white')
        lights.append(light)
        ax.add_artist(light)

    # Define the walking motion
    def walk_motion(frame):
        # Calculate the angle of rotation for each light
        angles = np.linspace(0, 2 * np.pi, num_lights)
        for i, light in enumerate(lights):
            light.center = (np.cos(angles[i]), np.sin(angles[i]))
            light.set_alpha(0.8)

    # Create the animation
    ani = animation.FuncAnimation(fig, walk_motion, frames=int(duration * fps), blit=True, repeat=True)

    # Save the animation
    ani.save("walking_animation.gif", writer='pillow', fps=fps)
    plt.close(fig)  # Close the figure to prevent display

if __name__ == '__main__':
    generate_walking_animation()
