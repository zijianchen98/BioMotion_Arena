
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
num_frames = 100
weight_y = -0.4  # Vertical position of "heavy weight", higher means heavier
base_positions = np.array([
    [0, 1],  # Head
    [-0.5, 0.5], [0.5, 0.5],  # Shoulders
    [-0.5, 0.2], [0.5, 0.2],  # Hips
    [-0.7, -0.1], [0.7, -0.1],  # Knees
    [-0.9, -0.3], [0.9, -0.3],  # Feet
]) * 0.5
weight_position = np.array([0, weight_y])

# Function to create the animation
def update(frame):
    plt.clf()  # Clear the previous frame
    plt.axis('equal')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.gca().set_facecolor('black')  # Black background

    # Calculate movement; simple oscillation to simulate running
    offset_x = np.sin(frame * 0.1) * 0.1
    offset_y = -abs(np.cos(frame * 0.1)) * 0.1 - weight_y

    # Calculate new positions
    positions = base_positions + np.array([offset_x, offset_y]).T
    positions = np.vstack([positions, weight_position])  # Include the weight

    # Plot points
    plt.scatter(positions[:, 0], positions[:, 1], color='white', s=100)

# Create the animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)
plt.show()
