
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to update the positions of the point-lights
def update(frame):
    plt.clf()  # Clear the current frame
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.axis('off')  # Turn off the axes

    # Define the positions of the point-lights
    sitting_positions = np.array([
        [0, 4],  # Head
        [-1, 3], [1, 3],  # Shoulders
        [-2, 2], [0, 2], [2, 2],  # Arms
        [-2, 1], [0, 1], [2, 1],  # Elbows
        [-1, 0], [1, 0],  # Knees
        [0, -1], [-1, -2], [1, -2],  # Feet
        [0, -3]  # Center of mass
    ])

    # Calculate the animated sitting motion (simplified realistic motion)
    sitting_positions[:, 1] -= frame * 0.05  # Move downwards to simulate sitting

    # Draw the point-lights
    plt.scatter(sitting_positions[:, 0], sitting_positions[:, 1], color='white', s=100)

# Setup the figure
fig = plt.figure(figsize=(6, 6), facecolor='black')

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

# Display the animation
plt.show()
