
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point-lights
num_points = 15

# Define initial positions for the point-lights in a downward bowing posture
# Example coordinates based on a simplistic representation of a person bowing
initial_positions = np.array([
    [0, 4],   # Head
    [-1, 3],  # Left shoulder
    [1, 3],   # Right shoulder
    [-1, 2.5],# Left elbow
    [1, 2.5], # Right elbow
    [-1, 1],  # Left wrist
    [1, 1],   # Right wrist
    [0, 0],   # Torso
    [-0.5, -1], # Left hip
    [0.5, -1], # Right hip
    [-0.5, -2], # Left knee
    [0.5, -2],  # Right knee
    [-0.5, -3], # Left ankle
    [0.5, -3],  # Right ankle
    [0, -4],    # Base (ground)
    [0, -2]     # Weight being held (on ground)
])

# Animation function
def update(frame):
    plt.clf()  # Clear the current frame
    plt.axis('equal')  # Maintain aspect ratio
    plt.xlim(-5, 5)  # x-limits
    plt.ylim(-5, 5)  # y-limits
    plt.gca().set_facecolor('black')  # Set background color to black

    # Calculate new positions for the animation
    # Bowing animation: frames will modify the y position
    bowing_offset = 0.1 * np.sin(frame / 10)  # Dynamic bowing motion
    positions = initial_positions.copy()
    positions[:, 1] -= bowing_offset  # Move downwards

    # Plot points representing the point-lights
    plt.scatter(positions[:, 0], positions[:, 1], color='white', s=100)

# Create the figure and axis
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200, 1), interval=100)

# Show the animation
plt.show()
