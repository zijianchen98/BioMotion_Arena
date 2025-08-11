
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point light sources
n_points = 15
point_light_positions = np.random.rand(n_points, 3)

# Define the black background
black_background = np.zeros((n_points, 3))

# Define the man's pose
pose = np.array([
    [0.1, 0.2, 0.3],  # x, y, z
    [-0.1, 0.2, 0.3],  # x, y, z
    [0.1, -0.2, 0.3],  # x, y, z
    [-0.1, -0.2, 0.3]   # x, y, z
])

# Define the animation function
def animate(i):
    global point_light_positions, black_background, pose

    # Update the point light positions
    point_light_positions = np.random.rand(n_points, 3)

    # Update the black background
    black_background = np.zeros((n_points, 3))

    # Update the man's pose
    pose[0, 2] -= 0.01 * i  # decrease z position
    pose[1, 2] -= 0.01 * i  # decrease z position
    pose[2, 2] -= 0.01 * i  # decrease z position
    pose[3, 2] -= 0.01 * i  # decrease z position

    # Normalize the pose
    pose = pose / np.linalg.norm(pose, axis=1, keepdims=True)

    # Create the figure and axis
    fig, ax = plt.subplots()

    # Plot the point lights
    for i, point_light in enumerate(point_light_positions):
        ax.scatter(point_light[0], point_light[1], point_light[2], c='w', s=10)

    # Plot the black background
    ax.scatter(0, 0, 0, c='k', s=10)

    # Plot the man's pose
    ax.scatter(pose[:, 0], pose[:, 1], pose[:, 2], c='r', s=20)

    # Set the axis limits
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect('equal')

    # Set the axis labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Update the plot
    plt.draw()

    # Wait for 1 second
    plt.pause(1)

ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=20)
plt.show()
