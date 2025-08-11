
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
num_lights = 15

# Initialize the positions of the point lights
# Defined based on a sad woman sitting down posture
light_positions = np.array([
    [0, 5],  # Head
    [-1, 4], [1, 4],  # Shoulders
    [-1.5, 3], [0, 3], [1.5, 3],  # Upper body
    [-1.2, 2], [1.2, 2],  # Elbows
    [0, 1],  # Hands
    [-1, 0], [1, 0],  # Thighs
    [-0.5, -1], [0.5, -1],  # Knees
    [-0.3, -2], [0.3, -2],  # Feet
])

# Animation function to update the positions
def animate(frame):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 6)
    ax.axis('off')

    # Update light positions
    offsets = np.sin(np.linspace(0, 2 * np.pi, num_lights) + frame / 10) * 0.1
    new_positions = light_positions.copy()
    new_positions[:, 1] += offsets

    # Draw the point lights
    ax.scatter(new_positions[:, 0], new_positions[:, 1], color='white', s=100)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(5, 8))
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

plt.show()
