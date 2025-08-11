
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Set up the figure and axis
fig, ax = plt.subplots()

# Set the axis limits and aspect ratio
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')

# Set the background color to black
ax.set_facecolor('black')

# Define the point-light positions
point_lights = np.array([
    [0.5, 0.2],  # Head
    [0.4, -0.2],  # Left shoulder
    [-0.4, -0.2],  # Right shoulder
    [0.3, -0.4],  # Left elbow
    [-0.3, -0.4],  # Right elbow
    [0.2, -0.6],  # Left wrist
    [-0.2, -0.6],  # Right wrist
    [0.1, -0.8],  # Left hand
    [-0.1, -0.8],  # Right hand
    [0.0, -0.9],  # Left hip
    [0.0, -0.9],  # Right hip
    [0.1, -0.7],  # Left knee
    [-0.1, -0.7],  # Right knee
    [0.0, -0.5],  # Left ankle
    [-0.0, -0.5],  # Right ankle
])

# Define the animation function
def animate(i):
    # Clear the previous frame
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Calculate the new positions of the point-lights
    new_positions = np.copy(point_lights)
    new_positions[:, 0] += np.sin(i/10) * 0.1  # Add a sinusoidal motion to the x-coordinates
    new_positions[:, 1] += np.cos(i/10) * 0.1  # Add a sinusoidal motion to the y-coordinates

    # Plot the point-lights
    for position in new_positions:
        ax.plot(position[0], position[1], 'o', markersize=10, color='white')

    # Plot the body outline
    body = patches.Rectangle((-0.5, -0.9), 1, 0.2, edgecolor='white', facecolor='none', linewidth=2)
    ax.add_patch(body)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(300), interval=20, repeat=False)

# Show the animation
plt.show()
