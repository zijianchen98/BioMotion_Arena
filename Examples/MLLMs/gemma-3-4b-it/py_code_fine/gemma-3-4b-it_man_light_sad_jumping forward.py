
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_sadman_jump_animation(duration=10, fps=30):
    """
    Generates a point-light stimulus animation depicting a sadman jumping forward.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): Frames per second.
    """

    # Define the number of points
    num_points = 15

    # Define the initial positions of the points (slightly offset to create a dynamic effect)
    points = np.random.rand(num_points, 2) * 0.5 + 0.5  # Normalized to [0, 1]

    # Define the animation function
    def animate(frame):
        # Update the positions of the points based on the frame number
        for i in range(num_points):
            # Simulate jumping motion.  The sine wave creates a smooth, oscillating movement
            x = points[i, 0] + np.sin(frame / 10) * 0.2
            y = points[i, 1] + np.cos(frame / 10) * 0.2
            points[i, 0] = x
            points[i, 1] = y

        # Clear the previous frame
        img.clear()

        # Plot the points on a black background
        img = plt.imshow(np.zeros((100, 100)), cmap='gray', interpolation='nearest')

        # Plot the points
        plt.scatter(points[:, 0], points[:, 1], s=50, c='white')

        # Set the background to black
        plt.gca().set_facecolor('black')
        plt.axis('off')
        return img

    # Create the figure and axes
    fig, ax = plt.subplots()

    # Initialize the animation
    ani = animation.FuncAnimation(fig, animate, frames=int(duration * fps), blit=True)

    # Save the animation (optional)
    # ani.save("sadman_jump.gif", writer='pillow', fps=fps)

    # Display the animation
    plt.show()

if __name__ == '__main__':
    generate_sadman_jump_animation()
