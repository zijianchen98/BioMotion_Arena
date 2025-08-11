
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the number of point lights
num_points = 15

# Initial positions of the point lights for a woman lying down
# These points roughly represent a human's important joints (head, shoulders, hips, etc.)
positions = np.array([[0, 1], [-0.5, 0.5], [0.5, 0.5], [-0.5, 0], [0.5, 0],
                      [-0.5, -0.5], [0.5, -0.5], [0, 0.2], [-0.3, 0.1],
                      [0.3, 0.1], [-0.3, -0.1], [0.3, -0.1], [0, -0.2],
                      [-0.4, -0.3], [0.4, -0.3], [0, -0.4]])

# Function to update the positions for each frame
def update(frame):
    # Simulate slight movement (right at shoulders and hips for realism)
    # This can be adjusted for more realistic body motion
    movement = 0.05 * np.sin(np.linspace(0, 2 * np.pi, num_points) + frame / 5.0)
    updated_positions = positions.copy()
    updated_positions[:, 1] += movement  # Update vertical positions

    # Clear the plot
    plt.clf()
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.gca().set_facecolor('black')
    plt.gca().set_xticks([])
    plt.gca().set_yticks([])

    # Draw the point lights
    plt.scatter(updated_positions[:, 0], updated_positions[:, 1], color='white', s=100)

# Create a figure for the animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

# Show the animation
plt.show()
