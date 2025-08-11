
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_waving_hand_animation(duration=10, frame_rate=30):
    """
    Generates a point-light animation of a man waving his hand.

    Args:
        duration (int): The duration of the animation in seconds.
        frame_rate (int): The number of frames per second.
    """

    # Define the number of points
    num_points = 15

    # Define the motion parameters (adjust these for different waving styles)
    # These values represent a simplified biomechanical model
    # You can modify them to change the appearance of the wave
    amplitude = 0.8
    frequency = 2.0
    phase = 0.0
    damping = 0.95

    # Create the figure and axes
    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.axis('off')

    # Create the points
    points = plt.scatter(0, 0, s=50, color='white')

    # Animation function
    def animate(frame):
        phase += frequency
        for i in range(num_points):
            x = np.cos(2 * np.pi * frequency * frame + phase) * amplitude
            y = np.sin(2 * np.pi * frequency * frame + phase) * amplitude
            points.set_offsets(np.array([[x, y]]) )
        return points,

    # Create the animation
    ani = animation.FuncAnimation(fig, animate, frames=int(duration * frame_rate), blit=True, repeat=True)

    # Save the animation (optional)
    # ani.save("waving_hand.gif", writer='pillow', fps=frame_rate)

    plt.show()


if __name__ == '__main__':
    generate_waving_hand_animation()
