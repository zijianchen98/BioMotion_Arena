
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Number of points (15)
num_points = 15

# Initialize positions for the point-lights
# Create a simple model for a human posture sitting down
# This can be simplified into a vertical arrangement of points

# Initial coordinates for the point-lights
points = np.array([
    [0, 1],   # Head
    [-0.5, 0.75], [0.5, 0.75],  # Shoulders
    [-0.5, 0.5], [0.5, 0.5],     # Elbows
    [-0.75, 0.2], [0.75, 0.2],   # Hands
    [-0.25, 0], [0.25, 0],       # Hips
    [-0.5, -0.5], [0.5, -0.5],   # Knees
    [-0.25, -1], [0.25, -1],     # Feet
    [-0.1, -1.2], [0.1, -1.2]    # Weight indication (additional points)
])

# Function to update the points in the animation
def update(frame):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_xticks([])
    ax.set_yticks([])

    # Simulate sitting down motion by adjusting the y coordinates
    positions = points.copy()
    positions[:, 1] -= frame * 0.05  # Gradually lower the y-position

    # Plot the points
    ax.scatter(positions[:, 0], positions[:, 1], c='white', s=100)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 20), interval=100)

# Show the animation
plt.show()
