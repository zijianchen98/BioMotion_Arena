
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define a function to create the point-light animation
def create_animation():
    # Create a black background
    fig, ax = plt.subplots()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-3, 1)
    ax.set_facecolor('black')

    # Define the positions of the points for the 'lying down' action
    # Positions represent a simplified stick figure of a woman lying down
    points = np.array([
        [0, 0],   # Head
        [-0.5, -0.5], [0.5, -0.5],  # Shoulders
        [-0.7, -1.0], [0.7, -1.0],  # Elbows
        [-1.0, -1.5], [1.0, -1.5],  # Hands
        [-0.5, -1.5], [0.5, -1.5],  # Hips
        [-0.5, -2.0], [0.5, -2.0],   # Knees
        [-0.5, -2.5], [0.5, -2.5],   # Feet
        [-1.0, -2.0], [1.0, -2.0],   # Weight (to indicate heavy weight)
    ])

    # Initialize points in the plot
    scat = ax.scatter(points[:, 0], points[:, 1], color='white')

    def update(frame):
        # Update point positions for animation effect (simple vertical oscillation)
        phase_offset = np.sin(frame / 10.0) * 0.1
        updated_points = points.copy()
        updated_points[:, 1] += phase_offset
        scat.set_offsets(updated_points)
        return scat,

    ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)
    plt.axis('off')  # Hide the axes
    plt.show()

# Call the function to create the animation
create_animation()
