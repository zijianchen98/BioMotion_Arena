
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def happy_man_forward_rolling(num_frames):
    fig, ax = plt.subplots()
    ax.set_xlim((-10, 10)
    ax.set_ylim((-10, 10))
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Define the happy man as a sequence of points
    happy_man_points = np.array([
        [1, 1],  # Head
        [1, -1],  # Left shoulder
        [-1, -1],  # Right shoulder
        [-1, 1],  # Left hip
        [1, 1]  # Right hip
    ])

    # Initialize the animation
    def init():
        return []

    # Define the update function for each frame of the animation
    def animate(i):
        global happy_man_points
        # Calculate the position of each point based on forward rolling motion
        happy_man_points[0] += 0.1 * np.sin(np.radians(i % 360))  # Head moves in a circle
        happy_man_points[1:] += 0.1 * np.sin(np.radians(i // 360))  # Other shoulder -> right shoulder -> left hip -> right hip
        happy_man_points %= 10  # Wrap around if it goes out of bounds
        
        # Clear the previous frame
        ax.clear()
        # Plot the points
        ax.plot(happy_man_points[:, 0], happy_man_points[:, 1], 'w.', markersize=10)
        
        return []

    # Create the animation
    ani = animation.FuncAnimation(fig, animate, frames=num_frames, init_func=init, blit=True)

    # Show the animation
    plt.show()

# Call the function to create the animation
happy_man_forward_roll(300)
