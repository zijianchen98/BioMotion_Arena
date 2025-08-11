
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# These positions are chosen to represent a person with a heavy weight
# The points are arranged to form a rough shape of a person with the weight
points = np.array([
    [0.1, 0.5],  # Head
    [0.2, 0.6],  # Right shoulder
    [0.1, 0.7],  # Right elbow
    [0.2, 0.8],  # Right hand
    [-0.1, 0.5],  # Left shoulder
    [-0.2, 0.6],  # Left elbow
    [-0.1, 0.7],  # Left hand
    [0.0, 0.4],  # Torso
    [0.1, 0.3],  # Right hip
    [0.2, 0.2],  # Right knee
    [0.1, 0.1],  # Right ankle
    [-0.1, 0.3],  # Left hip
    [-0.2, 0.2],  # Left knee
    [-0.1, 0.1],  # Left ankle
    [0.0, 0.0]  # Weight
])

# Define the animation function
def animate(frame):
    # Clear the previous frame
    ax.clear()
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(-0.1, 1.1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Update the positions of the points based on the frame number
    # These updates are chosen to create a smooth and natural rolling motion
    updated_points = points + np.array([
        [0.01 * np.sin(frame / 10.0), 0.01 * np.cos(frame / 10.0)],  # Head
        [0.02 * np.sin(frame / 10.0), 0.02 * np.cos(frame / 10.0)],  # Right shoulder
        [0.03 * np.sin(frame / 10.0), 0.03 * np.cos(frame / 10.0)],  # Right elbow
        [0.04 * np.sin(frame / 10.0), 0.04 * np.cos(frame / 10.0)],  # Right hand
        [-0.02 * np.sin(frame / 10.0), 0.02 * np.cos(frame / 10.0)],  # Left shoulder
        [-0.03 * np.sin(frame / 10.0), 0.03 * np.cos(frame / 10.0)],  # Left elbow
        [-0.04 * np.sin(frame / 10.0), 0.04 * np.cos(frame / 10.0)],  # Left hand
        [0.005 * np.sin(frame / 10.0), 0.005 * np.cos(frame / 10.0)],  # Torso
        [0.01 * np.sin(frame / 10.0), -0.01 * np.cos(frame / 10.0)],  # Right hip
        [0.02 * np.sin(frame / 10.0), -0.02 * np.cos(frame / 10.0)],  # Right knee
        [0.03 * np.sin(frame / 10.0), -0.03 * np.cos(frame / 10.0)],  # Right ankle
        [-0.01 * np.sin(frame / 10.0), -0.01 * np.cos(frame / 10.0)],  # Left hip
        [-0.02 * np.sin(frame / 10.0), -0.02 * np.cos(frame / 10.0)],  # Left knee
        [-0.03 * np.sin(frame / 10.0), -0.03 * np.cos(frame / 10.0)],  # Left ankle
        [0.0, -0.01 * frame / 10.0]  # Weight
    ])

    # Plot the updated points
    ax.scatter(updated_points[:, 0], updated_points[:, 1], c='white', s=10)

# Create a new figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

# Show the animation
plt.show()
